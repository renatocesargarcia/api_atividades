from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Gustavo', idade=38)
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
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

if __name__ == '__main__':
   #insere_pessoas()
   # altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()
