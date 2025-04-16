import unittest
from src.app import usuarios, criar_usuario, buscar_usuario_por_cpf, deletar_usuario

class TestUsuarioCRUD(unittest.TestCase):
    def setUp(self):
        usuarios.clear()
    
    def test_criar_usuario(self):
        usuario = criar_usuario("João", "joao@email.com", "senha123", "12345678900")
        self.assertEqual(usuario['nome'], "João")
          
    
    def test_buscar_usuario(self):
        criar_usuario("Maria", "maria@email.com", "senha456", "98765432100")
        usuario = buscar_usuario_por_cpf("98765432100")
        self.assertEqual(usuario['nome'], "Maria")
    
    def test_buscar_usuario_inexistente(self):
        usuario = buscar_usuario_por_cpf("00000000000")
        self.assertIsNone(usuario)
    
    def test_deletar_usuario(self):
        criar_usuario("Pedro", "pedro@email.com", "senha789", "11122233344")
        criar_usuario("Ana", "ana@email.com", "senha000", "22233344455")
        novo_tamanho = deletar_usuario("11122233344")
        self.assertEqual(novo_tamanho, 1)
        

if __name__ == '__main__':
    unittest.main()