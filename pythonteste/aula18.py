'''teste = []
teste.append('Thiago')
teste.append(34)
galera = []
galera.append(teste[:])
teste [0] = 'Maria'
teste [1] = 70
galera.append(teste[:])
print(galera)
print(teste)'''
#galera = [['Thiago', 34], ['Maria', 70], ['Naeme', 22], ['Josete', 52]]
#print(galera[3][1], galera[2][1])

'''frutas = []# cria uma lista
frutas.append('banana')#adiciona um item na lista
frutas.append(2.50)#adiciona o próximo item a lista
itens = []# cria outra lista item
itens.append(frutas[:])#cópia: não muda se com os dois comandos abaixo, eles serão adicionados como uma nova sublista em itens
frutas [0] = 'Maçã'#ao invés de substituir 'banana' ela vai criar um novo item(em modo associado(substituível)) na lista itens
frutas [1] = 3.50
itens.append(frutas)#associação: muda com os dois comandos abaixo
frutas[0] = 'Pêra'#substitui o item anterior ('Maçã')
frutas[1] = 4.20# subistitui o valor anterior (3.50)

print(frutas)
print(itens)'''

'''produtos = list()
produtos.append('Notebook')
produtos.append(2500)
listaProd = list()
#listaProd.append(produtos[:])
produtos[0] = 'Caderno'
produtos[1] = 25
listaProd.append(produtos[:])
print(produtos)
print(listaProd)'''

'''turma = [['Joao', 48], ['Francisco', 35], ['Frederico', 60], ['Mácio', 55]]
for p in turma:
    print(f'{p[0]}, tem {p[1]} anos.')'''

clientes = list()
dados = list()
for c in range(0, 5):
    dados.append(str(input('Nome do cliente: ')))
    dados.append(int(input('Idade do cliente: ')))
    clientes.append(dados[:])#faz uma cópia de dados para dentro de clientes
    dados.clear()#apaga conteudo de dados pra poder gerar novos dados no proximo loop pra adicionar a clientes

print(dados)
print(clientes)
print(clientes[0])
print('-=' * 30)
for p in clientes:
    if p[1] < 25:
        print(f'')
