
usuarios = []  

def criar_usuario(nome, email, senha, cpf):


    if not all([nome, email, senha, cpf]):
        raise ValueError("Todos os campos são obrigatórios")
    
    
    if any(u['cpf'] == cpf for u in usuarios):
        raise ValueError("CPF já cadastrado")
    
    novo_usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'cpf': cpf
    }
    usuarios.append(novo_usuario)
    return novo_usuario

def listar_usuarios():
    return usuarios.copy()

def buscar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario.copy()
    return None

def deletar_usuario(cpf):
    global usuarios
    usuarios = [u for u in usuarios if u['cpf'] != cpf]
    return len(usuarios)  