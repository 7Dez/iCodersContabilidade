import flet as ft
from datetime import datetime
from busca_empresa import criar_busca_empresa  # Importando o componente de busca

# Função para a tela de Contas a Pagar
def contas_pagar_view(page: ft.Page):
    page.title = "Contas a Pagar - Sistema Contábil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Variável para armazenar a empresa selecionada
    empresa_selecionada = None

    # Função chamada quando uma empresa é selecionada
    def on_select_empresa(empresa):
        nonlocal empresa_selecionada
        empresa_selecionada = empresa
        page.snack_bar = ft.SnackBar(ft.Text(f"Empresa selecionada: {empresa['nome']}"))
        page.snack_bar.open = True
        page.update()

    # Componente de busca de empresa
    busca_empresa = criar_busca_empresa(on_select_empresa)

    # Função para adicionar uma nova conta
    def adicionar_conta(e):
        if not empresa_selecionada:
            page.snack_bar = ft.SnackBar(ft.Text("Selecione uma empresa antes de adicionar uma conta!"))
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
        page.snack_bar = ft.SnackBar(ft.Text("Conta adicionada com sucesso!"))
        page.snack_bar.open = True
        page.update()

    # Campos do formulário
    descricao = ft.TextField(label="Descrição", width=300)
    valor = ft.TextField(label="Valor", width=300)
    data_vencimento = ft.TextField(label="Data de Vencimento (AAAA-MM-DD)", width=300)
    categoria = ft.Dropdown(
        label="Categoria",
        width=300,
        options=[
            ft.dropdown.Option("Aluguel"),
            ft.dropdown.Option("Energia"),
            ft.dropdown.Option("Fornecedores"),
            ft.dropdown.Option("Outros"),
        ],
    )

    # Botão para adicionar conta
    btn_adicionar = ft.ElevatedButton("Adicionar Conta", on_click=adicionar_conta)

    # Layout da página
    page.add(
        ft.Column(
            [
                ft.Text("Contas a Pagar", size=30, weight=ft.FontWeight.BOLD),
                busca_empresa,  # Componente de busca de empresa
                descricao,
                valor,
                data_vencimento,
                categoria,
                btn_adicionar,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executa o aplicativo
if __name__ == "__main__":
    ft.app(target=contas_pagar_view)