import flet as ft
from cadastro_empresa import tela_cadastro
from dashboard import dashboard_view

# Função para a página inicial (Home)
def home_view(page: ft.Page):
    page.title = "Home - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título da Home
    title = ft.Text("Bem-vindo ao Sistema Contábil", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800)

    # Função para navegar para o Menu
    def go_to_menu(e):
        page.clean()
        dashboard_menu(page)

    # Botão de navegação para o Menu
    btn_dashboard = ft.ElevatedButton(
        "Abrir Menu",
        icon=ft.icons.MENU,
        on_click=go_to_menu,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_600,
        width=200,
        height=50,
    )

    # Layout da página inicial
    page.add(
        ft.Column(
            [
                title,
                btn_dashboard,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

# Função para o Dashboard com Menu Centralizado e AppBar no Topo
def dashboard_menu(page: ft.Page):
    page.title = "Menu - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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

    # Função para navegar para a página de Dashboard
    def go_to_dashboard(e):
        page.clean()  # Limpa a página
        dashboard_view(page)

    # Função para voltar para a Home
    def go_to_home(e):
        page.clean()
        home_view(page)

    # Função para abrir configurações
    def open_configuracoes(e):
        page.clean()
        page.add(ft.Text("Configurações", size=30, weight=ft.FontWeight.BOLD))

    # Função para sair do sistema
    def sair(e):
        page.window_close()  # Fecha a aplicação

    # Criando o AppBar no topo
    app_bar = ft.AppBar(
        title=ft.Text("Sistema Contábil",color='white'),
        center_title=True,
        bgcolor=ft.colors.BLUE_800,
        actions=[
            ft.IconButton(icon=ft.icons.HOME, on_click=go_to_home, tooltip="Voltar para Home", icon_color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.BUSINESS, on_click=go_to_cadastrar_empresa, tooltip="Cadastrar Empresa", icon_color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.PAYMENTS, on_click=go_to_contas_pagar, tooltip="Contas a Pagar", icon_color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.ATTACH_MONEY, on_click=go_to_contas_receber, tooltip="Contas a Receber", icon_color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.DASHBOARD, on_click=go_to_dashboard, tooltip="Dashboard", icon_color=ft.colors.WHITE),
            ft.PopupMenuButton(
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(text="Configurações", icon=ft.icons.SETTINGS, on_click=open_configuracoes),
                    ft.PopupMenuItem(text="Sair", icon=ft.icons.EXIT_TO_APP, on_click=sair),
                ],
                icon_color=ft.colors.WHITE,
            )
        ]
    )

    # Botões do Menu Centralizado
    menu_buttons = ft.Column(
        [
            ft.ElevatedButton(
                "Cadastrar Empresa",
                icon=ft.icons.BUSINESS,
                on_click=go_to_cadastrar_empresa,
                width=300,
                height=50,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_600,
            ),
            ft.ElevatedButton(
                "Contas a Pagar",
                icon=ft.icons.PAYMENTS,
                on_click=go_to_contas_pagar,
                width=300,
                height=50,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_600,
            ),
            ft.ElevatedButton(
                "Contas a Receber",
                icon=ft.icons.ATTACH_MONEY,
                on_click=go_to_contas_receber,
                width=300,
                height=50,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_600,
            ),
            ft.ElevatedButton(
                "Dashboard",
                icon=ft.icons.DASHBOARD,
                on_click=go_to_dashboard,
                width=300,
                height=50,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_600,
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Adiciona o AppBar e o menu centralizado à página
    page.appbar = app_bar
    page.add(menu_buttons)

# Função para o Dashboard (exemplo de outra tela)
def dashboard_view(page: ft.Page):
    page.title = "Dashboard - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Exemplo de conteúdo do Dashboard
    page.add(ft.Text("Dashboard", size=30, weight=ft.FontWeight.BOLD))

# Executa o aplicativo
if __name__ == "__main__":
    ft.app(target=home_view)