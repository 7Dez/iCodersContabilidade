import flet as ft
from cadastro_empresa import tela_cadastro
from dashboard import dashboard_view

# Função para a página inicial (Home)
def home_view(page: ft.Page):
    page.title = "Home - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título da Home
    title = ft.Text("Bem-vindo ao Sistema Contábil", size=30, weight=ft.FontWeight.BOLD)

    # Função para navegar para o Menu
    def go_to_menu(e):
        page.clean()
        dashboard_menu(page)

    # Botão de navegação para o Menu
    btn_dashboard = ft.ElevatedButton("Ir para o Dashboard", on_click=go_to_menu)

    page.add(title)
    page.add(btn_dashboard)

# Função para o Dashboard
def dashboard_menu(page: ft.Page):
    page.title = "Menu - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título do Dashboard
    title = ft.Text("Dashboard", size=30, weight=ft.FontWeight.BOLD)

    # Função para navegar para a página de Cadastro de Empresa
    def go_to_cadastrar_empresa(e):
        page.clean()  # Limpa a página
        tela_cadastro(page)  # Chama a função tela_cadastro

    # Função para navegar para a página de Contas a Pagar
    def go_to_contas_pagar(e):
        page.clean()  # Limpa a página
        page.add(ft.Text("Adicionar Contas a Pagar", size=30, weight=ft.FontWeight.BOLD))

    # Função para navegar para a página de Contas a Receber
    def go_to_contas_receber(e):
        page.clean()  # Limpa a página
        page.add(ft.Text("Adicionar Contas a Receber", size=30, weight=ft.FontWeight.BOLD))

    # Função para navegar para a página de Contas a Receber
    def go_to_dashboard(e):
        page.clean()  # Limpa a página
        dashboard_view(page)
        

    # Botões de navegação
    btn_cadastrar_empresa = ft.ElevatedButton("Cadastrar Empresa", on_click=go_to_cadastrar_empresa)
    btn_contas_pagar = ft.ElevatedButton("Contas a Pagar", on_click=go_to_contas_pagar)
    btn_contas_receber = ft.ElevatedButton("Contas a Receber", on_click=go_to_contas_receber)
    btn_dashboard = ft.ElevatedButton("Dashboard", on_click=go_to_dashboard)

    # Adicionando o título e os botões na página
    page.add(title)
    page.add(ft.Column(
        [btn_cadastrar_empresa, btn_contas_pagar, btn_contas_receber,btn_dashboard],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    ))

if __name__ == "__main__":
    ft.app(target=home_view)