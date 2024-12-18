nome = input('Qual é o seu nome? ')
n1 = float(input('Qual foi a sua primeira nota {} ? '.format(nome) ))
n2 = float(input('Qual foi a sua segunda nota {} ? '.format(nome) ))
media = (n1 + n2) /2
print(' A primeira nota foi {:.2f}\n A segunda nota foi {}\n A média é {} ' .format(n1, n2, media))