import flet as ft

def main(page: ft.Page):
    page.title = "YouTube Video in Flet"
    
    youtube_url = "https://www.youtube.com/embed/dQw4w9WgXcQ"  # URL de inserción de YouTube

    webview = ft.WebView(
        url=youtube_url,
        expand=True
    )

    page.add(webview)

ft.app(main)
