nums=0
nums2=0
cont = 0

while nums != 999:
    nums = int(input('Digite um número (digite 999 para sair): '))
    if nums != 999:#999 é o flag(parada)
        cont +=1 #aqui o a contagem de entradas é feita somente se passar pela condição
        nums2 = nums2 + nums #aqui se somam os números digitados, que vem pela variavel de entrada e se soma a outra variavel que tem valor 0


print('A quantidade de números digitados foi: {}'.format(cont))
print('O a soma dos números digitados é: {}'.format(nums2))
