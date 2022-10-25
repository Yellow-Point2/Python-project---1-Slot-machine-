import random
from array import *





print("Olá hacker, bem vindo à Slot Machine!\n")
y=0
cred = 500
my_list =[* "@"*50,* "#"*40,*"$"*30,*"%"*20,* "&"*10,* "£"*5, "€"]
# O * no início faz com q o valor apareça o no. de vezes pelo qual e multiplicado

x=600
while y != 1:
    print(" Você tem ", cred, " créditos iniciais. Quantos Créditos Quer Apostar?\n")
    x=int(input())
    while x>cred:
        if (x>cred):
            print("Você n tem esse montante de créditos. Por favor insira um montante válido")
            print(" Você tem ", cred, " créditos iniciais. Quantos Créditos Quer Apostar?\n")
            x=int(input())
        else:
            pass
    class Roleta:
        """Define os valores da Slot Machine"""
        def __init__(self, roleta1, roleta2, roleta3):
            self.roleta1 = roleta1
            self.roleta2 = roleta2
            self.roleta3 = roleta3
   
    simb1=random.choice(my_list)
    simb2=random.choice(my_list)
    simb3=random.choice(my_list)
    roleta = Roleta(simb1, simb2, simb3)
    roleta.creditos = cred
    print("Números da Slot Machine:")
    print(roleta.roleta1, roleta.roleta2, roleta.roleta3)

    if (roleta.roleta1 == roleta.roleta2 == roleta.roleta3) and simb1 == my_list [1]:
        cred = cred + x * 5
        print("Venceu! Ganhou:", x*5, "créditos\nAgora tens ",cred," créditos")
    elif (roleta.roleta1 == roleta.roleta2 == roleta.roleta3 and simb1 == my_list[50]):
        cred = cred + x*10
        print("Venceu! Ganhou:", x*10, "créditos\nAgora tens ",cred," créditos")
    elif (roleta.roleta1 == roleta.roleta2 == roleta.roleta3 and simb1 == my_list[90]):
        cred = cred + x*20
        print("Venceu! Ganhou:", x*20, "créditos\nAgora tens ",cred," créditos")
    elif (roleta.roleta1 == roleta.roleta2 == roleta.roleta3 and simb1 == my_list[120]):
        cred = cred + x*70
        print("Venceu! Ganhou:", x*70, "créditos\nAgora tens ",cred," créditos")
    elif (roleta.roleta1 == roleta.roleta2 == roleta.roleta3 and simb1 == my_list[140]):
        cred = cred + x*200
        print("Venceu! Ganhou:", x*200, "créditos\nAgora tens ",cred," créditos")
    elif (roleta.roleta1 == roleta.roleta2 == roleta.roleta3 and simb1 == my_list[150]):
        cred = cred + x*1000
        print("Venceu! Ganhou:", x*1000, "créditos\nAgora tens ",cred," créditos")
    elif (roleta.roleta1 == roleta.roleta2 == roleta.roleta3 and simb1 == my_list[155]):
        cred = cred + x*100000
        print("Venceu! Ganhou:", x*100000, "créditos\nAgora tens ",cred," créditos")
    else:
        cred = cred - x
        print("Perdeu! Perdeu: ",x, " créditos.\nAgora tens ",cred," créditos")
    print(cred)
    if (cred <=0):
        y=y+1
        print("Sem créditos para jogar!")
        print("Fim de jogo")
    else:
        y=0
        print("Quer jogar novamente? (Sim, Não)")
        z=str(input())

        if (z == "Sim"):
            y=0
        else:
            y= y+1
            print("Fim de jogo")


    


