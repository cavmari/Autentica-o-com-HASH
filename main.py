import hashlib

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)
        
    def _hash_senha(self, senha):
        return hashlib.md5(senha.encode()).hexdigest()

class SistemaAutenticacao:
    def __init__(self):
        self.usuarios = []
    
    def cadastrar_usuario(self, nome, email, senha):
        novo_usuario = Usuario(nome, email, senha)
        self.usuarios.append(novo_usuario)
        self._salvar_usuarios()

    def _salvar_usuarios(self):
        with open('usuarios.txt', 'w') as file:
            for usuario in self.usuarios:
                file.write(f"{usuario.nome},{usuario.email},{usuario.senha}\n")

    def autenticar_usuario(self, email, senha):
        senha_hash = hashlib.md5(senha.encode()).hexdigest()
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha_hash:
                return True
        return False


sistema = SistemaAutenticacao()
sistema.cadastrar_usuario("Alice", "alice@example.com", "1234")
sistema.cadastrar_usuario("Bob", "bob@example.com", "5678")

print(sistema.autenticar_usuario("alice@example.com", "1234"))  # Saída: True
print(sistema.autenticar_usuario("alice@example.com", "5678"))  # Saída: False
