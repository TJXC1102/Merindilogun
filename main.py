#Projeto Mérìndilogún
#Cálculo do odu de nascimento
import datetime
from datetime import date
import pandas as pd
import random
import numpy as np

def valida(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        print("Opção inválida")
        x = int(input(pergunta))
    return x

def dia_da_semana():

    temp = pd.Timestamp(data_ano)
    orisa = (temp.dayofweek)

    if orisa == 0:
        print("Você nasceu na segunda e os orixás regentes são: Esú, Omulu, Iansã.")
    elif orisa == 1:
        print("Você nasceu na terça e os orixás regentes são: Ogu. Oxum, Ossãe.")
    elif orisa == 2:
        print("Você nasceu na quarta e os orixás regentes são: Xangô, Obá, Oxumarê.")
    elif orisa == 3:
        print("Você nasceu na quinta e os orixás regentes são: Oxóssi, Irocô, Lodé.")
    elif orisa == 4:
        print("Você nasceu na sexta e o orixá regente é: Oxalá.")
    elif orisa == 5:
        print("Você nasceu no sábado e os orixás regentes são: Iemanjá, podendo ser qualquer uma das iáras.")
    elif orisa == 6:
        print("Você nasceu na domingo e os orixás regentes são: Nanã, ibeiji.")

def odu():
    if odu_nascimento == 1:
        print("Okaran")
    elif odu_nascimento == 2:
        print("Ejiokô")
    elif odu_nascimento == 3:
        print("Etaogundá")
    elif odu_nascimento == 4:
        print("Irosun")
    elif odu_nascimento == 5:
        print("Ôxê")
    elif odu_nascimento == 6:
        print("Obará")
    elif odu_nascimento == 7:
        print("Ôdi")
    elif odu_nascimento == 8:
        print("Êgioníle")
    elif odu_nascimento == 9:
        print("Ossá")
    elif odu_nascimento == 10:
        print("Ofún")
    elif odu_nascimento == 11:
        print("Ôwarin")
    elif odu_nascimento == 12:
        print("Êjilaxeborá")
    elif odu_nascimento == 13:
        print("Êjilobon")
    elif odu_nascimento == 14:
        print("Iká")
    elif odu_nascimento == 15:
        print("Obéogundá")
    elif odu_nascimento == 16:
        print("Aláfia")


def caida_buzio(p):
    result = np.random.binomial(1, p)
    return result

def odus_caidas():
    if np.count_nonzero(resultado == 0) == 0:
        print("jogo Fechado - jogar novamente")
    if np.count_nonzero(resultado == 0) == 1:
        print("Okaran")
    if np.count_nonzero(resultado == 0) == 2:
        print("Ejiokô")
    if np.count_nonzero(resultado == 0) == 3:
        print("Etaogundá")
    if np.count_nonzero(resultado == 0) == 4:
        print("Irosun")
    if np.count_nonzero(resultado == 0) == 5:
        print("Ôxê")
    if np.count_nonzero(resultado == 0) == 6:
        print("Obará")
    if np.count_nonzero(resultado == 0) == 7:
        print("Ôdi")
    if np.count_nonzero(resultado == 0) == 8:
        print("Êgioníle")
    if np.count_nonzero(resultado == 0) == 9:
        print("Ossá")
    if np.count_nonzero(resultado == 0) == 10:
        print("Ofún")
    if np.count_nonzero(resultado == 0) == 11:
        print("Ôwarin")
    if np.count_nonzero(resultado == 0) == 12:
        print("Êjilaxeborá")
    if np.count_nonzero(resultado == 0) == 13:
        print("Êjilobon")
    if np.count_nonzero(resultado == 0) == 14:
        print("Iká")
    if np.count_nonzero(resultado == 0) == 15:
        print("Obéogundá")
    if np.count_nonzero(resultado == 0) == 16:
        print("Aláfia")

while True:
    print("\nVocê deseja:")
    print("1 - Cálcular o odú de nascimento \n2 - Jogar búzios \n3 - Sair")
    opcao = valida("Escolha a opção desejada: ", 1, 3)
    if opcao == 1:
        nome = input("Digite seu nome: ")
        data_simples = date(year=int(input("Digite o ano de seu nascimento: ")), month=int(input("Digite o mês de seu nascimento: ")),day=int(input("Digite o dia de seu nascimento: ")))
        data_ano = data_simples.strftime("%y-%m-%d")
        print("Data de nascimento: ",data_simples.strftime("%d/%m/%y"), "\n")
        dia_da_semana()
        odu_nascimento = sum(int(i) for i in (data_simples.strftime("%d%m%y")))
        if odu_nascimento <=16:
            odu_nascimento
        else:
            odu_nascimento = sum(int(i) for i in (str(odu_nascimento)))
        print("\nO seu Odu de nascimento é: ")
        odu()

    elif opcao == 2:
        probabilidade = .5
        n = 16
        resultado = np.arange(n)
        for i in range(0, n):
            resultado[i] = caida_buzio(probabilidade)
        i += 1
        print(resultado)
        print("\nBúzios fechados: ", np.count_nonzero(resultado == 1))
        print("Búzios abertos: ", np.count_nonzero(resultado == 0),"\n")
        odus_caidas()
    elif opcao == 3:
        exit()
