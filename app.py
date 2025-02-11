import flet as ft

def dashboard_view(page: ft.Page):
    page.title = "Dashboard - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Títulos
    title = ft.Text("Dashboard", size=30, weight=ft.FontWeight.BOLD)

    # Informações do Dashboard
    saldo_atual = ft.Card(
        content=ft.Column([
            ft.Text("Saldo Atual", size=20, weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 5.000,00", size=25, weight=ft.FontWeight.BOLD, color="green")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=300,
        height=150,
        color=ft.colors.CYAN_50
    )

    contas_pagar = ft.Card(
        content=ft.Column([
            ft.Text("Contas a Pagar", size=20, weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 1.200,00", size=25, weight=ft.FontWeight.BOLD, color="red")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=300,
        height=150,
        color=ft.colors.RED_50
    )

    contas_receber = ft.Card(
        content=ft.Column([
            ft.Text("Contas a Receber", size=20, weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 2.500,00", size=25, weight=ft.FontWeight.BOLD, color="green")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=300,
        height=150,
        color=ft.colors.GREEN_50
    )

    fluxo_caixa = ft.Card(
        content=ft.Column([
            ft.Text("Fluxo de Caixa", size=20, weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 3.000,00", size=25, weight=ft.FontWeight.BOLD, color="blue")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=300,
        height=150,
        color=ft.colors.BLUE_50
    )

    # Adicionando os Cards na tela
    page.add(
        title,
        ft.Row(
            [
                saldo_atual,
                contas_pagar,
                contas_receber,
                fluxo_caixa
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    ft.app(target=dashboard_view)  # Chama diretamente a função dashboard_view
