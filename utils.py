from models import Pessoas, Usuarios

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Andre Luis', idade=18)
    print(pessoa)
    pessoa.save()
# Consulta dados na tabela
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Felipe').first()
   # print(pessoa.idade)
# Altera dados na tabela
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.nome = 'Felipe'
    pessoa.save()
# Exclui dados na tabela
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Andre Luis').first()
    pessoa.delete()
    #pessoa.save()

def insere_usuario(Login, senha):
    usuario = Usuarios(Login=Login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios=Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('Jose Carlos', '1234')
    insere_usuario('Marco Antonio', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
