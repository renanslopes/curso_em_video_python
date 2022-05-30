# BRINCANDO COM STRINGS 01
# Usando STRIP, LEN e COUNT

# strip = remove os espaços antes e depois da string
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome....')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# len = retorna a quantidade de letras
# count = quanta a quantidade de caracteres informados dentro do ()
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
