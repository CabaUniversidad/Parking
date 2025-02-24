import flet as ft
from view import Home 
def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    Home.main(page)
ft.app(target=main)
