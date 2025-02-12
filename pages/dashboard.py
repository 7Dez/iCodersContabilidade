import flet as ft

def dashboard_view(page: ft.Page):
    page.title = "Dashboard - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Títulos
    title = ft.Text("Painel de controle", size=30, weight=ft.FontWeight.BOLD)
    
    # Informações do Dashboard
    saldo_atual = ft.Container(
        padding=10,
        bgcolor=ft.colors.RED_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Saldo Atual", weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 5.000,00", size=20, weight=ft.FontWeight.BOLD, color="lightgreen")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=200,
        height=100,
        
    )

    contas_pagar = ft.Container(
        padding=10,
        bgcolor=ft.colors.RED_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Contas a Pagar", weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 1.200,00", size=20, weight=ft.FontWeight.BOLD, color="red")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=200,
        height=100,
        
    )

    contas_receber = ft.Container(
         padding=10,
        bgcolor=ft.colors.RED_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Contas a Receber", weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 1.200,00", size=20, weight=ft.FontWeight.BOLD, color="green")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=200,
        height=100,
        
    )
    fluxo_caixa = ft.Container(
        padding=10,
        bgcolor=ft.colors.RED_50,
        border_radius=15,
        content=ft.Column([
            ft.Text("Fluxo de Caixa", weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("R$ 2.500,00", size=20, weight=ft.FontWeight.BOLD, color="lightblue")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=200,
        height=100,
        
    )
    container_busca = ft.Container(
        height=70,
        width=1500,
        bgcolor=ft.colors.GREEN_300,
        padding=ft.padding.symmetric(horizontal=20),
        content=ft.Row(
            controls=[
                ft.IconButton(ft.icons.ARROW_BACK),
                ft.Text(value='Consulta Empresa',size=25,color='white',weight=ft.FontWeight.BOLD),
                ft.TextField(hint_text='Buscar Empresa',icon=ft.icons.SEARCH,filled=True,bgcolor='white',border_color='transparent')
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    
    container_principal = ft.Container(
        width=1500,
        # padding=ft.padding.symmetric(horizontal=20),
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.colors.GREEN_300,
                    padding=ft.padding.all(15),
                    border_radius=15,
                    height=500,
                    width=300,
                    content=ft.Column(
                        controls=[
                            ft.Text(value='Nome da Empresa',size=20,color='white'),
                            ft.Divider(color='white'),
                            ft.Text(value='Dados Cadastrais',size=15,color='white'),
                            ft.Text(value='Cnpj',size=15,color='white'),
                            ft.Text(value='Telefone',size=15,color='white'),
                            ft.Text(value='Email',size=15,color='white'),
                        ]
                    )
                ),
                ft.Container(
                    bgcolor=ft.colors.GREEN_300,
                    padding=ft.padding.all(15),
                    border_radius=15,
                    height=500,
                    expand=True,
                    content=ft.Column(
                        controls =[
                                ft.Row(
                                    controls=[
                                        saldo_atual,contas_pagar,contas_receber,fluxo_caixa
                                ],alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        )
                        ]
                        
                    )
                )
            ],
        )
    )
    

    # Adicionando os Cards na tela
    page.add(
        container_busca,
        title,
        container_principal,
        
    )

if __name__ == "__main__":
    ft.app(target=dashboard_view)  # Chama diretamente a função dashboard_view
