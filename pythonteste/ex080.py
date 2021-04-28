valores = []
cont = 0
'''for i, v in enumerate(valoress):
    vals.append(int(input('Digite um valor: ')))# entra valor na pos 0
    min = vals[0]# coloca valor da pos 0 na var min
    if i <= min:
        print('Adicionado ao final da lista...')
    elif i > min:
        vals.append()

    cont += 1'''
for cont in range(0, 5): #contador de 0 a 4
    n = int(input('Digite um valor')) #cada ver que o contador passa um valor é inserido na variável p/ ser analizado
    if cont == 0 or n > valores[-1]:#Na primeira vez que passar ou quando n for maior q o último valor da lista...
        valores.append(n)#...n será adicionado ao final da lista.
        print(f'O valor {n} foi colocado na última posição.')
    else:# se não for a primeira passagem ou se n for menor que o último valor
        pos = 0# posição 0
        while pos < len(valores):# vai fazer uma  uma varredura na lista
            if n <= valores[pos]:# cada vez que passar vai verificar se n é <= ao valor dentro da posição(pos)
                valores.insert(pos, n) # se n for <= ao valor da posição haverá um deslocamento do valor anterior para a próxima posiçao e o valor de n será colocado em seu lugar
                print(f'O valor {n} foi inserido na posição {pos}')
                break # para o loop while
            pos += 1# incrementa em 1 a var pos e soce pro For novamente
print('-='*30)
print(f'Os valores digitados foram: {valores}')





