# PORCENTAGEM (DESCONTO)

valor = float(input('Informe um valor a ser descontado: '))
valor_porcentagem = float(input('Informe a porcentagem a ser descontada: '))
calculo_porcentagem = valor * (valor_porcentagem/100)
desconto_porcentagem = valor - calculo_porcentagem
print('O valor com desconto informado fica em: R$ {}'.format(desconto_porcentagem))
