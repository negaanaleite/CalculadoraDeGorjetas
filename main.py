print("------------------------------------")
print(" Bem vindo ao Simulador de Gorgeta")
print("-------------------------------------")
conta = float(input("Qual o valor da conta? R$ "))
gorjeta = int(input(" Quanto você quer dar de gorjeta? 10,12 ou 15; "))
pessoa = int(input("Com quantas pessoas para dividir a conta? "))

gorjeta_porcentagem = gorjeta/100
valor_gorjeta_Tot = conta * gorjeta_porcentagem  
valor_gorjeta = conta + valor_gorjeta_Tot
conta_pp =valor_gorjeta / pessoa
total_cada = round(conta_pp,2)

print(f"Valor para cada: R$ {total_cada}")







