import flet as ft

# Словарь локализации для поддержки двух языков без ошибок
LOCALIZATION = {
    "ru": {
        "title": "MindCode Academy",
        "theme_title": "Кастомизация темы приложения:",
        "lang_title": "Язык / Language:",
        "xp_text": "XP: {user_xp} / {max_xp}",
        "courses_title": "Доступные ИИ-курсы:",
        "ai_task_prefix": "🤖 Задание от ИИ-Ментора:",
        "tf_label": "Вставьте ваш код решения",
        "btn_skip": "Пропустить (-30 XP)",
        "btn_submit": "Сдать на проверку (+25 XP)",
        "footer_policy": "Политика конфиденциальности",
        "footer_credits": "Создано xormeta, разработчиком из Axiom App Studio • 2026",
        "dialog_title": "Политика конфиденциальности",
        "dialog_btn": "Я согласен",
        "policy_1_title": "1. Сбор данных",
        "policy_1_text": "Приложение обрабатывает ваш текущий игровой прогресс (XP), выбранные цветовые настройки и текст вводимого вами кода локально на вашем устройстве.",
        "policy_2_title": "2. Использование ИИ",
        "policy_2_text": "Введенный вами код передается на защищенные сервера ИИ-ментора исключительно для синтаксического анализа, генерации рецензий и исправления ошибок.",
        "policy_3_title": "3. Безопасность",
        "policy_3_text": "Мы не собираем персональные данные (имена, email, пароли) без вашего явного согласия. Исходный код ваших решений не передается третьим лицам.",
        "tasks": [
            {"name": "Python", "task": "Напишите функцию, которая принимает список строк и возвращает только те, у которых длина больше 5 символов."},
            {"name": "JavaScript", "task": "Напишите обработчик события 'click' для кнопки, который плавно скрывает блок с id='alert'."},
            {"name": "Go (Golang)", "task": "Создайте структуру User и реализуйте для неё метод, возвращающий строку с полным именем."}
        ]
    },
    "en": {
        "title": "MindCode Academy",
        "theme_title": "App Theme Customization:",
        "lang_title": "Language / Язык:",
        "xp_text": "XP: {user_xp} / {max_xp}",
        "courses_title": "Available AI Courses:",
        "ai_task_prefix": "🤖 Task from AI Mentor:",
        "tf_label": "Paste your solution code here",
        "btn_skip": "Skip (-30 XP)",
        "btn_submit": "Submit for Review (+25 XP)",
        "footer_policy": "Privacy Policy",
        "footer_credits": "Created by xormeta, developer from Axiom App Studio • 2026",
        "dialog_title": "Privacy Policy",
        "dialog_btn": "I Agree",
        "policy_1_title": "1. Data Collection",
        "policy_1_text": "The application processes your current game progress (XP), selected color settings, and the text of your entered code locally on your device.",
        "policy_2_title": "2. Use of AI",
        "policy_2_text": "Your entered code is transmitted to secure AI mentor servers solely for syntax analysis, review generation, and bug fixing.",
        "policy_3_title": "3. Security",
        "policy_3_text": "We do not collect personal data (names, emails, passwords) without your explicit consent. The source code of your solutions is not shared with third parties.",
        "tasks": [
            {"name": "Python", "task": "Write a function that takes a list of strings and returns only those with a length greater than 5 characters."},
            {"name": "JavaScript", "task": "Write a 'click' event handler for a button that smoothly hides a block with id='alert'."},
            {"name": "Go (Golang)", "task": "Create a User structure and implement a method for it that returns a string with the full name."}
        ]
    }
}

def main(page: ft.Page):
    page.title = "MindCode Academy"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Задаем размеры окна ТОЛЬКО если запускаем на ПК (Windows/macOS/Linux)
    if page.platform not in [ft.PagePlatform.ANDROID, ft.PagePlatform.IOS]:
        page.window_width = 450
        page.window_height = 850
    
    # Глобальные переменные состояния приложения
    user_xp = 150
    max_xp = 500
    current_lang = "ru"
    current_primary = ft.colors.BLUE_ACCENT
    
    # Базовая инициализация темы
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=current_primary))

    # Ссылки на иконки языков (статичные)
    lang_icons = {
        "Python": ft.icons.TERMINAL,
        "JavaScript": ft.icons.CODE,
        "Go (Golang)": ft.icons.SPEED
    }

    # Инициализация пустых элементов UI для последующего динамического изменения
    header_title_main = ft.Text("MindCode", size=28, weight="bold", color=current_primary)
    header_title_sub = ft.Text("Academy", size=28, weight="bold")
    theme_label_text = ft.Text("", size=12, color=ft.colors.GREY_400)
    lang_label_text = ft.Text("", size=12, color=ft.colors.GREY_400)
    xp_label = ft.Text("", size=16, weight="bold")
    xp_bar = ft.ProgressBar(value=user_xp/max_xp, width=350, height=10, color=current_primary)
    courses_header_text = ft.Text("", size=18, weight="bold")
    lang_list = ft.ListView(expand=True, spacing=15, padding=5)
    footer_policy_btn = ft.TextButton(text="", style=ft.ButtonStyle(color=ft.colors.GREY_500))
    footer_credits_text = ft.Text("", size=10, color=ft.colors.GREY_600)

    # Элементы диалогового окна
    dialog_title_text = ft.Text("", size=20, weight="bold")
    dialog_p1_title = ft.Text("", weight="bold", size=14, color=ft.colors.AMBER_ACCENT)
    dialog_p1_text = ft.Text("", size=12)
    dialog_p2_title = ft.Text("", weight="bold", size=14, color=ft.colors.AMBER_ACCENT)
    dialog_p2_text = ft.Text("", size=12)
    dialog_p3_title = ft.Text("", weight="bold", size=14, color=ft.colors.AMBER_ACCENT)
    dialog_p3_text = ft.Text("", size=12)
    dialog_close_btn = ft.TextButton(text="")

    # Функция полного обновления текстового содержимого на основе выбранного языка
    def render_language_content():
        lang_data = LOCALIZATION[current_lang]
        
        # Обновление текстов на главном экране
        theme_label_text.value = lang_data["theme_title"]
        lang_label_text.value = lang_data["lang_title"]
        xp_label.value = lang_data["xp_text"].format(user_xp=user_xp, max_xp=max_xp)
        courses_header_text.value = lang_data["courses_title"]
        footer_policy_btn.text = lang_data["footer_policy"]
        footer_credits_text.value = lang_data["footer_credits"]

        # Обновление текстов в диалоговом окне политики конфиденциальности
        dialog_title_text.value = lang_data["dialog_title"]
        dialog_p1_title.value = lang_data["policy_1_title"]
        dialog_p1_text.value = lang_data["policy_1_text"]
        dialog_p2_title.value = lang_data["policy_2_title"]
        dialog_p2_text.value = lang_data["policy_2_text"]
        dialog_p3_title.value = lang_data["policy_3_title"]
        dialog_p3_text.value = lang_data["policy_3_text"]
        dialog_close_btn.text = lang_data["dialog_btn"]

        # Динамическая перерисовка списка курсов
        lang_list.controls.clear()
        for item in lang_data["tasks"]:
            # Сохраняем имя для поиска правильной иконки
            icon_key = item["name"]
            
            # Элементы управления внутри карточки курса
            tf_solution = ft.TextField(
                label=lang_data["tf_label"], 
                multiline=True, 
                min_lines=2, 
                text_style=ft.TextStyle(font_family="monospace")
            )
            btn_skip_task = ft.TextButton(
                text=lang_data["btn_skip"], 
                color=ft.colors.RED_300,
                on_click=lambda e: adjust_xp(-30)
            )
            btn_submit_task = ft.ElevatedButton(
                text=lang_data["btn_submit"], 
                on_click=lambda e: adjust_xp(25)
            )

            lang_list.controls.append(
                ft.Container(
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    border_radius=15,
                    padding=15,
                    border=ft.border.all(1, ft.colors.GREY_800),
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(lang_icons.get(icon_key, ft.icons.CODE), color=ft.colors.WHITE), 
                            title=ft.Text(item['name'], weight="bold", size=18)
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text(lang_data["ai_task_prefix"], size=12, weight="bold", color=ft.colors.AMBER_ACCENT),
                                ft.Text(item['task'], italic=True, size=13),
                            ]),
                            padding=10,
                            bgcolor=ft.colors.BLACK26,
                            border_radius=8,
                        ),
                        tf_solution,
                        ft.Row([btn_skip_task, btn_submit_task], alignment="end", spacing=10)
                    ])
                )
            )

    # Функция динамической смены цветовой темы
    def update_theme(color):
        nonlocal current_primary
        current_primary = color
        page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=color))
        xp_bar.color = color
        header_title_main.color = color
        page.update()

    # Изменение XP и прогресс-бара
    def adjust_xp(amount):
        nonlocal user_xp
        user_xp = max(0, min(max_xp, user_xp + amount))
        xp_label.value = LOCALIZATION[current_lang]["xp_text"].format(user_xp=user_xp, max_xp=max_xp)
        xp_bar.value = user_xp / max_xp
        xp_bar.color = ft.colors.RED_ACCENT if user_xp < 100 else current_primary
        page.update()

    # Изменение языка в выпадающем списке
    def on_language_change(e):
        nonlocal current_lang
        current_lang = e.control.value
        render_language_content()
        page.update()

    # Функции модального окна политики конфиденциальности
    def show_privacy_policy(e):
        page.dialog = privacy_dialog
        privacy_dialog.open = True
        page.update()

    def close_privacy_policy(e):
        privacy_dialog.open = False
        page.update()

    # Привязка обработчика закрытия к кнопке модального окна
    dialog_close_btn.on_click = close_privacy_policy

    privacy_dialog = ft.AlertDialog(
        modal=True,
        title=dialog_title_text,
        content=ft.Container(
            content=ft.Column([
                dialog_p1_title, dialog_p1_text, ft.Divider(height=10),
                dialog_p2_title, dialog_p2_text, ft.Divider(height=10),
                dialog_p3_title, dialog_p3_text
            ], scroll=ft.ScrollMode.ALWAYS, spacing=10),
            height=300,
            width=400,
        ),
        actions=[dialog_close_btn],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Кнопка открытия политики конфиденциальности
    footer_policy_btn.on_click = show_privacy_policy

    # Палитра выбора цвета темы
    theme_selector = ft.Row([
        ft.IconButton(ft.icons.CIRCLE, icon_color=c, on_click=lambda e, color=c: update_theme(color))
        for c in [ft.colors.BLUE_ACCENT, ft.colors.GREEN_ACCENT, ft.colors.PURPLE_ACCENT, ft.colors.ORANGE_ACCENT, ft.colors.PINK_ACCENT]
    ], alignment="center")

    # Переключатель языков (Dropdown меню)
    language_dropdown = ft.Dropdown(
        value=current_lang,
        options=[
            ft.dropdown.Option("ru", "Русский"),
            ft.dropdown.Option("en", "English"),
        ],
        width=140,
        height=45,
        content_padding=10,
        on_change=on_language_change
    )

    # Первичный рендеринг текстового контента перед выводом на экран
    render_language_content()

    # Сборка и вывод интерфейса в SafeArea
    page.add(
        ft.SafeArea(
            content=ft.Column([
                # Хедер
                ft.Row([
                    ft.Row([header_title_main, header_title_sub]),
                    ft.Icon(ft.icons.AUTO_AWESOME, size=24)
                ], alignment="spaceBetween"),
                
                # Настройки интерфейса (Тема и Язык в одну строку для экономии места)
                ft.Row([
                    ft.Column([theme_label_text, theme_selector], spacing=2),
                    ft.Column([lang_label_text, language_dropdown], spacing=2)
                ], alignment="spaceBetween"),
                
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),

                # Виджет профиля и прогресс-бара
                ft.Container(
                    content=ft.Column([xp_label, xp_bar], alignment="center", horizontal_alignment="center"),
                    padding=15, 
                    bgcolor=ft.colors.BLACK26, 
                    border_radius=15,
                    border=ft.border.all(1, ft.colors.GREY_900)
                ),
                
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                courses_header_text,
                
                # Основной прокручиваемый список курсов
                lang_list,
                
                ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                
                # Футер приложения
                ft.Container(
                    content=ft.Column([
                        footer_policy_btn,
                        footer_credits_text
                    ], horizontal_alignment="center", spacing=0),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=5, bottom=5)
                )
            ], expand=True)
        )
    )

if __name__ == '__main__':
    ft.app(target=main)
