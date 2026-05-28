import flet as ft

def main(page: ft.Page):
    page.title = "MindCode Academy"
    page.theme_mode = ft.ThemeMode.DARK
    page.alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Container(
            content=ft.Text("MindCode Academy Запущена!", size=24, weight="bold", color=ft.colors.GREEN_ACCENT),
            alignment=ft.alignment.center
        )
    )

ft.app(target=main)
