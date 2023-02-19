

#24. Elabore um programa que leia a velocidade de um carro e a velocidade permitida pelo radar.
#Caso a leitura do carro ser maior que 10% da permitida, informar uma mensagem “reduza a
#velocidade da próxima vez, porque desta vez terá que pagar uma multa.

print(f"\nVelocidade da Via 100Km\n")

Velicidade = int(input("Qual a sua Velocidade? : "))

if (Velicidade <= 110):
    print(f"\nSua velocidade é {Velicidade}, Esta deboa!\n")
else:
    print(f"\nSua velocidade é {Velicidade}, Levou Multa!\n")