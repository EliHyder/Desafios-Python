class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros_cadastro = []

    def cadastrar_livro(self, livro):
        self.livros_cadastro.append(livro)

    def emprestar_livro(self, livro, usuario):
        if livro in self.livros_cadastro and livro.disponivel:
            livro.disponivel = False
            usuario.livros_emprestados.append(livro)
            return f"{usuario.nome} emprestou '{livro.titulo}'"
        else:
            return f"'{livro.titulo}' não está disponível para empréstimo"
        
    def devolver_livro(self, livro, usuario):
        if livro in usuario.livros_emprestados:
            livro.disponivel = True
            usuario.livros_emprestados.remove(livro)
            return f"{usuario.nome} devolveu '{livro.titulo}'"
        else:
            return f"{usuario.nome} não tem '{livro.titulo}' emprestado"
        
if __name__ == "__main__":
    biblioteca = Biblioteca()
    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
    biblioteca.cadastrar_livro(livro1)
    biblioteca.cadastrar_livro(livro2)
    
    usuario = Usuario("Alice")
    print(biblioteca.emprestar_livro(livro1, usuario))  # Saída: Alice emprestou '1984'
    print(biblioteca.emprestar_livro(livro1, usuario))  # Saída: '1984' não está disponível para empréstimo
    print(biblioteca.devolver_livro(livro1, usuario))   # Saída: Alice devolveu '1984'
    print(biblioteca.emprestar_livro(livro1, usuario))  # Saída: Alice emprestou '1984'