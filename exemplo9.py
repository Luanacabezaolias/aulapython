nome = input("Insira seu nome: ")
carros = int (input("Digite a quantidade de carros vendidos: "))
valor = float(input("Insira o valo total de vendas: "))
comissao = 200 * carros 
porcentagem = 0.02 * valor
salariototal1 = 2500 + comissao + porcentagem 
print(f'salario do vendedor {nome} é {salariototal1}') 
