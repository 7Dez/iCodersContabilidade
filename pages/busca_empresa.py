import flet as ft
import sqlite3  

# Conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect("sistema_contabil.db")

# Buscar empresas pelo nome que começa com a letra digitada
def buscar_empresas_por_nome(prefixo):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM empresas WHERE nome LIKE ?", (prefixo + "%",))
    empresas = cursor.fetchall()
    conn.close()
    return [{"id": emp[0], "nome": emp[1]} for emp in empresas]

# Criar a interface de busca dentro do diálogo
def criar_dialogo_busca(on_empresa_selecionada):
    lista_empresas = ft.Column(scroll="adaptive")  # Lista para exibir as empresas filtradas
    input_busca = ft.TextField(label="Digite para buscar", on_change=None)

    def atualizar_lista(e):
        prefixo = input_busca.value.strip()
        lista_empresas.controls.clear()
        if prefixo:
            empresas_filtradas = buscar_empresas_por_nome(prefixo)
            for emp in empresas_filtradas:
                botao_empresa = ft.TextButton(emp["nome"], on_click=lambda e, emp=emp: selecionar_empresa(emp))
                lista_empresas.controls.append(botao_empresa)
        lista_empresas.update()

    def selecionar_empresa(empresa):
        on_empresa_selecionada(empresa)
        dialog.open = False
        dialog.update()

    input_busca.on_change = atualizar_lista

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Buscar Empresa"),
        content=ft.Column([input_busca, lista_empresas]),
        actions=[ft.TextButton("Fechar", on_click=lambda e: fechar_dialogo())],
    )

    def abrir_dialogo(e):
        dialog.open = True
        input_busca.value = ""
        lista_empresas.controls.clear()
        dialog.update()

    def fechar_dialogo():
        dialog.open = False
        dialog.update()

    return abrir_dialogo, dialog

def criar_busca_empresa(on_select_empresa):
    empresa_selecionada_text = ft.Text("")  # Texto onde será exibida a empresa escolhida

    def on_empresa_selecionada(empresa):
        empresa_selecionada_text.value = f"Empresa selecionada: {empresa['nome']}"
        empresa_selecionada_text.update()
        # Chama a função passada como argumento com a empresa selecionada
        on_select_empresa(empresa)

    abrir_dialogo, dialogo_busca = criar_dialogo_busca(on_empresa_selecionada)

    return ft.Column([
        ft.ElevatedButton("Adicionar Empresa", on_click=abrir_dialogo),
        empresa_selecionada_text,  # Exibe a empresa abaixo do botão
        dialogo_busca
    ])
