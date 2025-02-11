import flet as ft
from auth_service import autenticar_usuario

def login_view(page: ft.Page):
    email = ft.TextField(label="E-mail")
    senha = ft.TextField(label="Senha", password=True)

    def login(event):
        if autenticar_usuario(email.value, senha.value):
            page.clean()
            page.add(ft.Text("Login bem-sucedido!"))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha inválidos"), open=True)
            page.update()

    btn_login = ft.ElevatedButton("Entrar", on_click=login)

    return ft.Column([email, senha, btn_login], alignment=ft.MainAxisAlignment.CENTER)
