vNome = str(input('Digite um nome: '))
if vNome == 'Ulisses':
    print('Qua lindo nome!!!')
elif vNome == 'Nayara' or vNome == 'Arthur':
    print('Meu Amor')
elif vNome in 'Gonçalves, Figueiredo':
    print('Prepara todas as panelas...')
else:
    print('Legal pacas!!!')
print('Tenha um Bom Dia, {}!'.format(vNome))



