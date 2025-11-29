historico = []
salarioINI = 1000


def verSaldo(dinero = salarioINI):
  print(f"O seu saldo é de R${dinero}")
  menu()


def addHist(action,listaHistorico = historico):
  return listaHistorico.append(action)

def verHist(listaHist = historico):
  for i in range(0,len(listaHist)):
    print(listaHist[i])
  menu()

def deposito():
    print(f'Saldo atual = {salarioINI}')
    qntd = float(input('Qual o valor que deseja depositar ?\n> '))
    if qntd < 0:
        print('Valor invalido')
    else:
        qntd += salarioINI
        print(f'Valor atual na conta: {qntd} com sucesso!')
        addHist(f"Depósito de {qntd}")
    menu()



def sacar():
    print(f'Saldo atual = {salarioINI}')
    qntd = float(input('Qual o valor que deseja depositar ?\n> '))
    if qntd < 0:
        print('Valor invalido')
    else:
        if salarioINI < qntd:
            qntd -= salarioINI
            print(f'Valor atual na conta: {qntd} com sucesso!')
            addHist(f"Saque de {qntd}")
    menu()


def menu():
    print('== MENU DO CAIXA ELETRONICO ==')
    escolha = int(input('1 - Depositar\n2 - Sacar\n3 - ver saldo\n4 - ver historico de transações\n5 - Sair\n> '))
    if escolha == 1:
        deposito()
    elif escolha == 2:
        sacar()
    elif escolha == 3:
      verSaldo()
    elif escolha == 4:
      verHist()
    elif escolha == 5:
      print("Finalizando o sistema")
      return


menu()