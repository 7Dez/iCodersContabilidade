import flet as ft
from busca_empresa import criar_busca_empresa  # Importando o componente de busca

def dashboard_view(page: ft.Page):
    page.title = "Dashboard - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Variável para armazenar a empresa selecionada
    empresa_selecionada = None

    # Função chamada quando uma empresa é selecionada
    def on_select_empresa(empresa):
        nonlocal empresa_selecionada
        empresa_selecionada = empresa
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Empresa selecionada: {empresa['nome']}"),
            bgcolor=ft.colors.GREEN,
        )
        page.snack_bar.open = True
        page.update()

    # Componente de busca de empresa
    busca_empresa = criar_busca_empresa(on_select_empresa)

    # Títulos
    title = ft.Text("Painel de Controle", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800)

    # Informações do Dashboard
    saldo_atual = ft.Container(
        padding=10,
        bgcolor=ft.colors.BLUE_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Saldo Atual", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            ft.Text("R$ 5.000,00", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_700)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=200,
        height=100,
    )

    contas_pagar = ft.Container(
        padding=10,
        bgcolor=ft.colors.BLUE_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Contas a Pagar", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            ft.Text("R$ 1.200,00", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.RED_700)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=200,
        height=100,
    )

    contas_receber = ft.Container(
        padding=10,
        bgcolor=ft.colors.BLUE_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Contas a Receber", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            ft.Text("R$ 1.200,00", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_700)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=200,
        height=100,
    )

    fluxo_caixa = ft.Container(
        padding=10,
        bgcolor=ft.colors.BLUE_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Fluxo de Caixa", weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            ft.Text("R$ 2.500,00", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=200,
        height=100,
    )

    container_principal = ft.Container(
        width=1500,
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.colors.BLUE_100,
                    padding=ft.padding.all(20),
                    border_radius=15,
                    height=500,
                    width=300,
                    content=ft.Column(
                        controls=[
                            ft.Text(value='Nome da Empresa', size=20, color=ft.colors.BLUE_800),
                            ft.Divider(color=ft.colors.BLUE_800),
                            ft.Text(value='Dados Cadastrais', size=15, color=ft.colors.BLUE_800),
                            ft.Text(value='CNPJ', size=15, color=ft.colors.BLUE_800),
                            ft.Text(value='Telefone', size=15, color=ft.colors.BLUE_800),
                            ft.Text(value='Email', size=15, color=ft.colors.BLUE_800),
                        ]
                    )
                ),
                ft.Container(
                    bgcolor=ft.colors.BLUE_100,
                    padding=ft.padding.all(20),
                    border_radius=15,
                    height=500,
                    expand=True,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    saldo_atual, contas_pagar, contas_receber, fluxo_caixa
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            )
                        ]
                    )
                )
            ],
        )
    )

    # Adicionando os Cards na tela
    page.add(
        title,
        ft.Card(
            content=ft.Container(
                content=busca_empresa,  # Componente de busca de empresa
                padding=20,
            ),
            elevation=5,
            width=600,
        ),
        container_principal,
    )

if __name__ == "__main__":
    ft.app(target=dashboard_view)  # Chama diretamente a função dashboard_view