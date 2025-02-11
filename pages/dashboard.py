import flet as ft

def dashboard_view(page: ft.Page):
    # Definindo o título da página
    page.title = "Dashboard - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título na página
    title = ft.Text("Dashboard", size=30, weight=ft.FontWeight.BOLD)

    # Adicionando o título à página
    page.add(title)

def main(page: ft.Page):
    # Chama a função que adiciona o título à página
    dashboard_view(page)

if __name__ == "__main__":
    ft.app(target=main)
