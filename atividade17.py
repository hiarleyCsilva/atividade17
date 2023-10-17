# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.from datetime import date

# Solicita o ano de nascimento do jovem
from datetime import date 
ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento


if idade < 18:
    anos_restantes = 18 - idade
    print(f"Você ainda vai se alistar ao serviço militar. Faltam {anos_restantes} anos.")
elif idade == 18:
    print("É a hora exata de se alistar ao serviço militar.")
else:
    anos_passados = idade - 18
    print(f"Já passou o tempo do alistamento. Passaram-se {anos_passados} anos.")
