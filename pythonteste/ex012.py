precoini = float(input('Qual o preço do produto? R$'))
desc = int(input('De quantos porcento é o desconto?'))
valdesc = (precoini * desc) / 100
valfinal = precoini - valdesc
print('O valor final com desconto de {}% é R${}'.format(desc, valfinal))