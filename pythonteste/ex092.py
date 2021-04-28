from datetime import datetime
funcionário = {}
funcionário['nome']= str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
funcionário['idade'] = datetime.now().year - nasc
funcionário['ctps']= int(input('Número da CTPS (digite 0 se não  tiver): '))
if funcionário['ctps'] != 0:
    funcionário['contratação'] = int(input('Qual o ano de contratação? '))
    funcionário['salário'] = float(input('Qual seu salário?'))
    funcionário['aposentadoria'] = (35 - (datetime.now().year - funcionário['contratação'])) + funcionário['idade']
print('-='*30)
for k, v in funcionário.items():
    print(f'{k} tem o valor {v}')






