import bcrypt
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario

def criar_usuario(nome, email, senha):
    session = SessionLocal()  # Criando a sessão com o banco
    
    # Verifica se o e-mail já existe
    if session.query(Usuario).filter(Usuario.email == email).first():
        print("E-mail já cadastrado!")
        session.close()
        return
    
    # Gera um hash seguro para a senha
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash)
    
    try:
        session.add(novo_usuario)
        session.commit()  # Salva no banco
        print("Usuário cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        session.rollback()
    finally:
        session.close()

def autenticar_usuario(email, senha):
    session = SessionLocal()
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    session.close()

    if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario.senha.encode('utf-8')):
        return True  # Usuário autenticado
    return False  # Senha errada

