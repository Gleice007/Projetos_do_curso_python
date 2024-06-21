#Vamos fazer um desafio com oque foi revisado.
#nome , sobrenome , idade (em inteiro) , Escola e numero de telefone. preciso de uma condição de que se o usuário for menor de idade 
#ele print que e de menor e precisa do documento da mae ai entra mais um input para saber o nome da mae : nome e sobre nome. 
#caso não seja menor de idade ele mostre para o usuário :print(nome sobrenome escola telefone)

nome_sobrenome = input('Qual seu nome completo? ')
idade = int(input('Qual sua idade? '))
escola = input('Qual escola você estuda ou estudou? ')
numero_para_contato = input('Qual seu número para contato? ')
maior_de_idade = idade >=18
menor_de_idade = idade <=17
print('Nome e sobrenome:', nome_sobrenome,)
print('Idade:', idade) 
print('Escola:', escola) 
print('Numero para contato:', numero_para_contato)

if maior_de_idade:
    print('Você estar autorizado')
elif menor_de_idade:
    print('Você é de menor!, precisa de uma autorização da mãe') 
    input('Qual o nome da sua mãe? ')  



