lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(lanche)

'''for comida in lanche: #cada vez que passar vai imprimir um item da Tupla
    print(f'Eu ou comer {comida}')'''

#print(len(lanche))

'''for cont in range(0, len(lanche)):
    print(lanche)'''

#for comida in lanche: #se não precisar mostrar o índice da tupa
    #print(f'Eu comi {comida}')

#for cont in range(0, len(lanche)): #se precisar mostrar o indice (maneira 1)
    #print(f'Eu vou come {lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(lanche): #se precisar mostrar o indice (maneira 2)
    #print(f'Eu vou comer {comida} na posição {pos}')

#print(sorted(lanche))#ordenado (não altera a ordem, só exibe ela ordenada)
#print(lanche)#desordenado

a = (2, 4, 5, 3)
b = (3, 5, 9)
c = a + b# a ordem importa
d = b + a# a ordem importa
#print(c)
#print(d)
#print(c.count(3))
#print(c.index(5))
#print(c.index(5, 3)
pessoa = ('Thiago', 34, 'M', 1.74)
#del(pessoa)#apaga variavel completa
print(pessoa)