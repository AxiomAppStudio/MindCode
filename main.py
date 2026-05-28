import flet as ft

def main(page: ft.Page):
    page.title = "MindCode Academy"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Фиксированные размеры для имитации мобильного экрана на ПК
    page.window_width = 450
    page.window_height = 850
    
    # Исходное состояние
    user_xp = 150
    max_xp = 500
    current_primary = ft.colors.BLUE_ACCENT
    
    # Функция динамической смены темы
    def update_theme(color):
        nonlocal current_primary
        current_primary = color
        page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=color))
        xp_bar.color = color
        header_text.color = color
        page.update()

    # Компоненты UI для системы рейтинга
    xp_label = ft.Text(f"XP: {user_xp} / {max_xp}", size=16, weight="bold")
    xp_bar = ft.ProgressBar(value=user_xp/max_xp, width=350, height=10, color=current_primary)
    
    def adjust_xp(amount):
        nonlocal user_xp
        user_xp = max(0, min(max_xp, user_xp + amount))
        xp_label.value = f"XP: {user_xp} / {max_xp}"
        xp_bar.value = user_xp / max_xp
        xp_bar.color = ft.colors.RED_ACCENT if user_xp < 100 else current_primary
        page.update()

    # Функция вызова модального окна с Политикой конфиденциальности
    def show_privacy_policy(e):
        page.dialog = privacy_dialog
        privacy_dialog.open = True
        page.update()

    def close_privacy_policy(e):
        privacy_dialog.open = False
        page.update()

    # Текст политики конфиденциальности
    privacy_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Политика конфиденциальности", size=20, weight="bold"),
        content=ft.Container(
            content=ft.Column([
                ft.Text("1. Сбор данных", weight="bold", size=14, color=ft.colors.AMBER_ACCENT),
                ft.Text("Приложение обрабатывает ваш текущий игровой прогресс (XP), выбранные цветовые настройки и текст вводимого вами кода локально на вашем устройстве.", size=12),
                ft.Divider(height=10),
                ft.Text("2. Использование ИИ", weight="bold", size=14, color=ft.colors.AMBER_ACCENT),
                ft.Text("Введенный вами код передается на защищенные сервера ИИ-ментора исключительно для синтаксического анализа, генерации рецензий и исправления ошибок.", size=12),
                ft.Divider(height=10),
                ft.Text("3. Безопасность", weight="bold", size=14, color=ft.colors.AMBER_ACCENT),
                ft.Text("Мы не собираем персональные данные (имена, email, пароли) без вашего явного согласия. Исходный код ваших решений не передается третьим лицам.", size=12),
            ], scroll=ft.ScrollMode.ALWAYS, spacing=10),
            height=300,
            width=400,
        ),
        actions=[
            ft.TextButton("Я согласен", on_click=close_privacy_policy)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Палитра выбора цвета темы
    theme_selector = ft.Row([
        ft.IconButton(ft.icons.CIRCLE, icon_color=c, on_click=lambda e, color=c: update_theme(color))
        for c in [ft.colors.BLUE_ACCENT, ft.colors.GREEN_ACCENT, ft.colors.PURPLE_ACCENT, ft.colors.ORANGE_ACCENT, ft.colors.PINK_ACCENT]
    ], alignment="center")

    # База языков и задач от ИИ
    languages = [
        {"name": "Python", "task": "Напишите функцию, которая принимает список строк и возвращает только те, у которых длина больше 5 символов.", "icon": ft.icons.TERMINAL},
        {"name": "JavaScript", "task": "Напишите обработчик события 'click' для кнопки, который плавно скрывает блок с id='alert'.", "icon": ft.icons.CODE},
        {"name": "Go (Golang)", "task": "Создайте структуру User и реализуйте для неё метод, возвращающий строку с полным именем.", "icon": ft.icons.SPEED},
    ]

    # Сетка курсов
    lang_list = ft.ListView(expand=True, spacing=15, padding=5)
    for lang in languages:
        lang_list.controls.append(
            ft.Container(
                bgcolor=ft.colors.SURFACE_VARIANT,
                border_radius=15,
                padding=15,
                border=ft.border.all(1, ft.colors.GREY_800),
                content=ft.Column([
                    ft.ListTile(
                        leading=ft.Icon(lang['icon'], color=ft.colors.WHITE), 
                        title=ft.Text(lang['name'], weight="bold", size=18)
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("🤖 Задание от ИИ-Ментора:", size=12, weight="bold", color=ft.colors.AMBER_ACCENT),
                            ft.Text(lang['task'], italic=True, size=13),
                        ]),
                        padding=10,
                        bgcolor=ft.colors.BLACK26,
                        border_radius=8,
                    ),
                    ft.TextField(label="Вставьте ваш код решения", multiline=True, min_lines=2, text_style=ft.TextStyle(font_family="monospace")),
                    ft.Row([
                        ft.TextButton("Пропустить (-30 XP)", on_click=lambda e: adjust_xp(-30), color=ft.colors.RED_300),
                        ft.ElevatedButton("Сдать на проверку (+25 XP)", on_click=lambda e: adjust_xp(25)),
                    ], alignment="end", spacing=10)
                ])
            )
        )

    header_text = ft.Text("MindCode", size=28, weight="bold", color=current_primary)

    # Главная разметка приложения
    page.add(
        ft.SafeArea(
            content=ft.Column([
                # Хедер
                ft.Row([
                    ft.Row([header_text, ft.Text("Academy", size=28, weight="bold")]),
                    ft.Icon(ft.icons.AUTO_AWESOME, size=24)
                ], alignment="spaceBetween"),
                
                ft.Text("Кастомизация темы приложения:", size=12, color=ft.colors.GREY_400),
                theme_selector,
                
                # Виджет профиля и прогресс-бара
                ft.Container(
                    content=ft.Column([xp_label, xp_bar], alignment="center", horizontal_alignment="center"),
                    padding=15, 
                    bgcolor=ft.colors.BLACK26, 
                    border_radius=15,
                    border=ft.border.all(1, ft.colors.GREY_900)
                ),
                
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                ft.Text("Доступные ИИ-курсы:", size=18, weight="bold"),
                
                # Основной список курсов
                lang_list,
                
                ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                
                # Обновленный футер по вашему запросу
                ft.Container(
                    content=ft.Column([
                        ft.TextButton(
                            text="Политика конфиденциальности", 
                            style=ft.ButtonStyle(color=ft.colors.GREY_500),
                            on_click=show_privacy_policy
                        ),
                        ft.Text("Создано xormeta, разработчиком из Axiom App Studio • 2026", size=10, color=ft.colors.GREY_600)
                    ], horizontal_alignment="center", spacing=0),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=5, bottom=5)
                )
            ], expand=True)
        )
    )

ft.app(target=main)
