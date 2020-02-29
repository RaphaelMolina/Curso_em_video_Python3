print('============= Desafio 04 ==============')

a = input('Digite algo: ')
b = type(a)
print('O valor digitado é do tipo: {}'. format(b))
print('O valor digitado é um espaço: {}'. format(a.isspace())) # Retorna true se string contiver apenas caracteres de espaço ou em branco e false caso contrário.
print('O valor digitado pode ser exibido em tela: {}'. format(a.isprintable())) # Retorna True se todos os caracteres da string forem imprimíveis ou se a string estiver vazia. Caso contrário, retorna False.
print('O valor digitado esta todo em minúsculo: {}'. format(a.islower())) # Retorna true se string tiver pelo menos todos os caracteres em minúsculo e falsos caso contrário.
print('O valor digitado esta todo em maiúsculo: {}'. format(a.isupper())) # Retorna true se string tiver pelo todos os caracteres em maiúsculas e falsos caso contrário.
print('O valor digitado é Alfanumerico: {}'. format(a.isalnum())) # Retorna True se todos os caracteres da string forem alfanuméricos (alfabetos ou números). Caso contrário, retorna False.
print('O valor digitado é um número: {}'. format(a.isnumeric())) # Retorna true se uma string unicode contiver apenas caracteres numéricos e false caso contrário.
print('O valor digitado é um Título: {}'. format(a.istitle())) # Verifica se o valor recebido tem o primeiro caracter de cada palavra maiúsculo e o restante minúsculo. Retorna true se a string estiver corretamente "titlecased" e falsa caso contrário.
print('O valor digitado é um dígito: {}'. format(a.isdigit())) # Verifica se o valor recebido contém apenas dígitos. Retorna true se string contiver apenas dígitos e false caso contrário.
print('O valor digitado é um identificador: {}'. format(a.isidentifier())) # Retorna True se a string for um identificador válido no Python. Caso contrário, retorna False.
print('O valor digitado é Alfabético: {}'. format(a.isalpha())) # Retorna true se string tiver pelo menos 1 caracter ou todos os caracteres forem alfabéticos e falsos caso contrário.
print('O valor digitado é decimal: {}'. format(a.isdecimal())) # Retorna true se uma string unicode contiver apenas caracteres decimais e false caso contrário.
print('True = Sim / False = Não')

