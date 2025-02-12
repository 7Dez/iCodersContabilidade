import flet as ft
import sqlite3
import bcrypt

# Configuração do banco de dados
def criar_tabelas():
    conn = sqlite3.connect("sistema_contabil.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT UNIQUE NOT NULL,
            endereco TEXT,
            telefone TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa_id INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            FOREIGN KEY (empresa_id) REFERENCES empresas(id)
        )
    """)
    conn.commit()
    conn.close()

# Função para cadastrar empresa e usuário
def cadastrar_empresa(nome, cnpj, endereco, telefone, email, senha):
    conn = sqlite3.connect("sistema_contabil.db")
    cursor = conn.cursor()

    try:
        # Insere a empresa
        cursor.execute("""
            INSERT INTO empresas (nome, cnpj, endereco, telefone)
            VALUES (?, ?, ?, ?)
        """, (nome, cnpj, endereco, telefone))
        empresa_id = cursor.lastrowid  # Obtém o ID da empresa recém-cadastrada

        # Criptografa a senha do usuário
        senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

        # Insere o usuário associado à empresa
        cursor.execute("""
            INSERT INTO usuarios (empresa_id, email, senha)
            VALUES (?, ?, ?)
        """, (empresa_id, email, senha_hash))

        conn.commit()  # Confirma as alterações no banco de dados
        print("Empresa e usuário cadastrados com sucesso!")  # Log de depuração
        return True
    except sqlite3.IntegrityError as e:
        # Caso haja erro de integridade (ex.: CNPJ ou email já cadastrados)
        conn.rollback()  # Desfaz as alterações
        print(f"Erro de integridade: {e}")  # Log de depuração
        return False
    finally:
        conn.close()  # Fecha a conexão com o banco de dados

# Interface gráfica
def main(page: ft.Page):
    # Configurações da página
    page.title = "Sistema Contábil"
    page.theme_mode = ft.ThemeMode.LIGHT  # Tema claro
    page.padding = 50
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#F5F5F5"  # Cor de fundo suave

    # Cabeçalho
    header = ft.Text(
        "Cadastro de Empresa",
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#333333",
    )

    # Campos do formulário
    nome = ft.TextField(
        label="Nome da Empresa",
        width=400,
        border_color="#4CAF50",  # Verde
        focused_border_color="#4CAF50",
    )
    cnpj = ft.TextField(
        label="CNPJ",
        width=400,
        border_color="#4CAF50",
        focused_border_color="#4CAF50",
    )
    endereco = ft.TextField(
        label="Endereço",
        width=400,
        border_color="#4CAF50",
        focused_border_color="#4CAF50",
    )
    telefone = ft.TextField(
        label="Telefone",
        width=400,
        border_color="#4CAF50",
        focused_border_color="#4CAF50",
    )
    email = ft.TextField(
        label="Email do Administrador",
        width=400,
        border_color="#4CAF50",
        focused_border_color="#4CAF50",
    )
    senha = ft.TextField(
        label="Senha",
        password=True,
        width=400,
        border_color="#4CAF50",
        focused_border_color="#4CAF50",
    )

    # Função para limpar os campos do formulário
    def limpar_campos():
        nome.value = ""
        cnpj.value = ""
        endereco.value = ""
        telefone.value = ""
        email.value = ""
        senha.value = ""
        page.update()

    # Função para exibir AlertDialog de sucesso
    def mostrar_dialogo_sucesso():
        dialogo = ft.AlertDialog(
            title=ft.Text("Sucesso!"),
            content=ft.Text("Empresa cadastrada com sucesso!"),
            on_dismiss=lambda e: print("Dialogo fechado"),
        )
        page.open(dialogo)  # Abre o diálogo usando page.open()
        print("Dialogo de sucesso exibido!")  # Log de depuração

    # Função para exibir AlertDialog de erro
    def mostrar_dialogo_erro():
        dialogo = ft.AlertDialog(
            title=ft.Text("Erro"),
            content=ft.Text("CNPJ ou email já cadastrado."),
            on_dismiss=lambda e: print("Dialogo fechado"),
        )
        page.open(dialogo)  # Abre o diálogo usando page.open()
        print("Dialogo de erro exibido!")  # Log de depuração

    # Função de cadastro
    def on_cadastrar(e):
        print("Botão de cadastro clicado!")  # Log de depuração
        if cadastrar_empresa(
            nome.value,
            cnpj.value,
            endereco.value,
            telefone.value,
            email.value,
            senha.value
        ):
            # Limpa os campos do formulário
            limpar_campos()

            # Exibe mensagem de sucesso
            mostrar_dialogo_sucesso()
        else:
            # Exibe mensagem de erro
            mostrar_dialogo_erro()

    # Botão de cadastro
    botao_cadastrar = ft.ElevatedButton(
        content=ft.Text("Cadastrar", color="white"),
        width=400,
        height=50,
        bgcolor="#4CAF50",  # Verde
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        on_click=on_cadastrar,
    )

    # Layout principal
    form = ft.Container(
        content=ft.Column(
            [
                header,
                nome,
                cnpj,
                endereco,
                telefone,
                email,
                senha,
                botao_cadastrar,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=40,
        bgcolor="white",
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.GREY_300,
            offset=ft.Offset(0, 0),
        ),
    )

    # Adiciona o formulário à página
    page.add(form)

# Cria as tabelas no banco de dados (se não existirem)
criar_tabelas()

# Inicia o aplicativo
ft.app(target=main)