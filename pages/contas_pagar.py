import flet as ft
from datetime import datetime
from busca_empresa import criar_busca_empresa  # Importando o componente de busca

# Função para a tela de Contas a Pagar
def contas_pagar_view(page: ft.Page):
    page.title = "Contas a Pagar - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT  # Modo claro

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

    # Função para adicionar uma nova conta
    def adicionar_conta(e):
        if not empresa_selecionada:
            page.snack_bar = ft.SnackBar(
                ft.Text("Selecione uma empresa antes de adicionar uma conta!"),
                bgcolor=ft.colors.RED,
            )
            page.snack_bar.open = True
            page.update()
            return

        nova_conta = {
            "id_empresa": empresa_selecionada["id"],
            "descricao": descricao.value,
            "valor": float(valor.value),
            "data_vencimento": datetime.strptime(data_vencimento.value, "%Y-%m-%d"),
            "categoria": categoria.value,
            "status": "Pendente",
        }
        # Aqui você pode salvar a conta no banco de dados
        print("Nova conta:", nova_conta)
        page.snack_bar = ft.SnackBar(
            ft.Text("Conta adicionada com sucesso!"),
            bgcolor=ft.colors.GREEN,
        )
        page.snack_bar.open = True
        page.update()

    # Campos do formulário
    descricao = ft.TextField(
        label="Descrição",
        width=400,
        border_radius=10,
        filled=True,
    )
    valor = ft.TextField(
        label="Valor",
        width=400,
        border_radius=10,
        filled=True,
    )
    data_vencimento = ft.TextField(
        label="Data de Vencimento (AAAA-MM-DD)",
        width=400,
        border_radius=10,
        filled=True,
    )
    categoria = ft.Dropdown(
        label="Categoria",
        width=400,
        border_radius=10,
        filled=True,
        options=[
            ft.dropdown.Option("Aluguel"),
            ft.dropdown.Option("Energia"),
            ft.dropdown.Option("Fornecedores"),
            ft.dropdown.Option("Outros"),
        ],
    )

    # Botão para adicionar conta
    btn_adicionar = ft.ElevatedButton(
        "Adicionar Conta",
        on_click=adicionar_conta,
        icon=ft.icons.ADD,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        width=400,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    # Layout da página
    page.add(
       
        ft.Column(
            [
                ft.Text("Contas a Pagar", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE),
                # Componente de busca de empresa destacado, separado do container
                ft.Card(
                    content=ft.Container(
                        content=busca_empresa,  # Componente de busca de empresa
                        padding=20,
                    ),
                    elevation=5,
                    width=600,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                               
                                descricao,
                                valor,
                                data_vencimento,
                                categoria,
                                btn_adicionar,
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                    ),
                    elevation=5,
                    width=600,
                ),
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executa o aplicativo
if __name__ == "__main__":
    ft.app(target=contas_pagar_view)