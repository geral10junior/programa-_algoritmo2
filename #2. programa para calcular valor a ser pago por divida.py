#2. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

def valor_pagar(dias, multa):
    multa_diaria = dias * multa
    return multa_diaria

valor_divida = float(input("informe o valor da divida: "))
dias_total = int(input("informe a quantidade de dias em atraso: "))
valor_multa = float(input('informe o valor da multa diaria por atraso: '))
multa_diaria = dias_total * valor_multa
divida_total = multa_diaria + valor_divida
print(divida_total)