import flet as ft
import sqlite3
from busca_empresa import criar_busca_empresa  # Importando o componente de busca

def dashboard_view(page: ft.Page):
    page.title = "Dashboard - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Variável para armazenar a empresa selecionada
    empresa_selecionada = None

    # Função para calcular o total das contas a pagar
    def calcular_total_contas_pagar():
        conn = sqlite3.connect('sistema_contabil.db')
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(valor) FROM contas_pagar")
        total = cursor.fetchone()[0] or 0  # Se não houver registros, retorna 0
        conn.close()
        return total

    # Função para calcular o total das contas a receber
    def calcular_total_contas_receber():
        conn = sqlite3.connect('sistema_contabil.db')
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(valor) FROM contas_receber")
        total = cursor.fetchone()[0] or 0  # Se não houver registros, retorna 0
        conn.close()
        return total

    # Função chamada quando uma empresa é selecionada
    def on_select_empresa(empresa):
        nonlocal empresa_selecionada
        empresa_selecionada = empresa

        # Conectar ao banco de dados e buscar os dados da empresa
        conn = sqlite3.connect('sistema_contabil.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome, cnpj, endereco, telefone FROM empresas WHERE nome = ?", (empresa['nome'],))
        dados_empresa = cursor.fetchone()
        conn.close()

        if dados_empresa:
            # Atualizar os dados no container
            container_empresa.content.controls[0].value = dados_empresa[0]  # Nome da Empresa
            container_empresa.content.controls[2].value = f"CNPJ: {dados_empresa[1]}"  # CNPJ
            container_empresa.content.controls[3].value = f"Telefone: {dados_empresa[3]}"  # Telefone
            container_empresa.content.controls[4].value = f"Endereço: {dados_empresa[2]}"  # Endereço

            # Atualizar o valor das contas a pagar
            total_contas_pagar = calcular_total_contas_pagar()
            contas_pagar.content.controls[1].value = f"R$ {total_contas_pagar:,.2f}"

            # Atualizar o valor das contas a receber
            total_contas_receber = calcular_total_contas_receber()
            contas_receber.content.controls[1].value = f"R$ {total_contas_receber:,.2f}"

            saldo_atual.content.controls[1].value = f"R$ {total_contas_receber - total_contas_pagar:,.2f}"
            if total_contas_receber > total_contas_pagar:
                saldo_atual.content.controls[1].color = ft.colors.GREEN_700
            else:
                saldo_atual.content.controls[1].color = ft.colors.RED_700
            

            
            # Mostrar mensagem de sucesso
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Empresa selecionada: {empresa['nome']}"),
                bgcolor=ft.colors.GREEN,
            )
            page.snack_bar.open = True
            page.update()
        else:
            # Mostrar mensagem de erro se a empresa não for encontrada
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Empresa não encontrada: {empresa['nome']}"),
                bgcolor=ft.colors.RED,
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
            ft.Text("R$ 0,00", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_700)
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
            ft.Text("R$ 0,00", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.RED_700)
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
            ft.Text("R$ 0,00", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_700)
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

    # Container para os dados da empresa
    container_empresa = ft.Container(
        bgcolor=ft.colors.BLUE_100,
        padding=ft.padding.all(20),
        border_radius=15,
        height=500,
        width=300,
        content=ft.Column(
            controls=[
                ft.Text(value='Nome da Empresa', size=20, color=ft.colors.BLUE_800),
                ft.Divider(color=ft.colors.BLUE_800),
                ft.Text(value='CNPJ', size=15, color=ft.colors.BLUE_800),
                ft.Text(value='Telefone', size=15, color=ft.colors.BLUE_800),
                ft.Text(value='Endereço', size=15, color=ft.colors.BLUE_800),
            ]
        )
    )

    container_principal = ft.Container(
        width=1500,
        content=ft.Row(
            controls=[
                container_empresa,
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