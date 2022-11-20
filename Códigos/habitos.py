# Dividir trabalho em partes
# Criar banco de dados
# Criar lista que receba nome, idade e sexo- ok
# criar lista que seja possível digitar itens de uma sexta de produtos
# criar lista de itens complementares
# Criar realatório por itens consumidos por cleinte
nome=[]
idad=[]
sexo=[]
homens=mulheres20=pessoas18=0
while True:
    print('Olá seja bem vindo(a) a seguir vamos solicitar algumas informações para cadastro')
    n= str(input('Digite seu nome: '))
    nome.append(n)
    idade=int(input('Qual a sua idade? '))
    idad.append(idade)
    s=' '
    while s not in 'MF':
        s= str(input('Qual seu sexo? (Masculino ou feminino) ')).strip().upper()[0]
        sexo.append(s)
    continuar=' '
    while continuar not in 'SN':
        continuar= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar=='N':
        print('Obrigado pelo cadastro, volte sempre!')
        break
