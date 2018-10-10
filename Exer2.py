nome = input("Digite o seu nome: ")
idade = input("Digite o sua idade: ")
idade = int(idade)
altura = input("Digite o sua altura: ")
altura = float(altura)
peso = input("Digite o seu peso: ")
peso = float(peso)
endereco = input("Digite o seu endereço: ")
print("Nome: %s " % nome + "\n" + "idade: %i" % idade + " anos" + "\n"
      + "Altura: %2.2f" % altura + "\n" + "Peso: %2.2f" % peso + "\n"
      + "Endereço: %s" % endereco)
