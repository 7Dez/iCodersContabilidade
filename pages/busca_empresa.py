import flet as ft
import sqlite3  # Substitua pelo seu banco de dados, se necessário

# Conectar ao banco de dados (exemplo usando SQLite)
def conectar_banco():
    return sqlite3.connect("sistema_contabil.db")

# Buscar empresa pelo ID
def buscar_empresa_por_id(id_empresa):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM empresas WHERE id = ?", (id_empresa,))
    empresa = cursor.fetchone()
    conn.close()
    return {"id": empresa[0], "nome": empresa[1]} if empresa else None

# Buscar todas as empresas do banco de dados
def carregar_empresas():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM empresas")
    empresas = cursor.fetchall()
    conn.close()
    return [{"id": emp[0], "nome": emp[1]} for emp in empresas]

# Função para criar o componente de busca de empresa
def criar_busca_empresa(on_select_empresa):
    dropdown_empresa = ft.Dropdown(
        label="Selecione uma empresa",
        width=300,
        options=[ft.dropdown.Option(key=str(empresa["id"]), text=empresa["nome"]) for empresa in carregar_empresas()],
        on_change=lambda e: on_select_empresa(buscar_empresa_por_id(int(e.control.value))),
    )
    return dropdown_empresa