import flet as ft
from datetime import datetime
import sqlite3
from busca_empresa import criar_busca_empresa  # Importando o componente de busca

# Função para criar a tabela contas_receber (caso não exista)
def criar_tabela_contas_receber():
    conn = sqlite3.connect('sistema_contabil.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas_receber (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_empresa INTEGER NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data_vencimento DATE NOT NULL,
            categoria TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente',
            FOREIGN KEY (id_empresa) REFERENCES empresas(id)
        )
    ''')
    conn.commit()
    conn.close()
criar_tabela_contas_receber()

# Função para a tela de Contas a Receber
def contas_receber_view(page: ft.Page):
    page.title = "Contas a Receber - Sistema Contábil"
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
    # Diálogo de sucesso
    dialog_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!"),
        content=ft.Text("Conta adicionada com sucesso."),
        on_dismiss=lambda e: print("Diálogo fechado"),
    )
   

    def abrir_dialog_sucesso():
        print("Tentando abrir o diálogo de sucesso...")  # Debug
        page.open(dialog_sucesso)  # Abre o diálogo corretamente

    # Função para adicionar uma nova conta a receber
    def adicionar_conta(e):
        if not empresa_selecionada:
            page.snack_bar = ft.SnackBar(
                ft.Text("Selecione uma empresa antes de adicionar uma conta!"),
                bgcolor=ft.colors.RED,
            )
            page.snack_bar.open = True
            page.update()
            return

        # Validar campos
        if not descricao.value or not valor.value or not data_vencimento.value or not categoria.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Preencha todos os campos!"),
                bgcolor=ft.colors.RED,
            )
            page.snack_bar.open = True
            page.update()
            return

        try:
            # Converter valores
            valor_float = float(valor.value)
            data_vencimento_date = datetime.strptime(data_vencimento.value, "%Y-%m-%d").date()
        except ValueError:
            page.snack_bar = ft.SnackBar(
                ft.Text("Valor ou data inválidos!"),
                bgcolor=ft.colors.RED,
            )
            page.snack_bar.open = True
            page.update()
            return

        # Salvar no banco de dados
        conn = sqlite3.connect('sistema_contabil.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contas_receber (id_empresa, descricao, valor, data_vencimento, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            empresa_selecionada["id"],
            descricao.value,
            valor_float,
            data_vencimento_date,
            categoria.value,
        ))
        conn.commit()
        conn.close()
        abrir_dialog_sucesso()

        # Limpar campos após salvar
        descricao.value = ""
        valor.value = ""
        data_vencimento.value = ""
        categoria.value = ""

        # Mostrar mensagem de sucesso
        page.snack_bar = ft.SnackBar(
            ft.Text("Conta a receber adicionada com sucesso!"),
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
            ft.dropdown.Option("Vendas"),
            ft.dropdown.Option("Serviços"),
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
                ft.Text("Contas a Receber", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE),
                
                # Componente de busca de empresa destacado, separado do container
                ft.Card(
                    content=ft.Container(
                        content=busca_empresa,  # Componente de busca de empresa
                        padding=20,
                    ),
                    elevation=5,
                    width=600,
                ),
                
                # Formulário dentro do container
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
    criar_tabela_contas_receber()  # Cria a tabela se não existir
    ft.app(target=contas_receber_view)