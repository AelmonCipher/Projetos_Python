print('===== DESAFIO 04 =====')
qlqr = input('Digite algo: ')
print('O tipo é: ',type(qlqr))
print(qlqr,'só tem espaços?',qlqr.isspace())
print(qlqr,'é um numero?',qlqr.isnumeric())
print(qlqr,'é alfabético? ',qlqr.isalpha())
print(qlqr,'é um alfanúmerico?',qlqr.isalnum())
print(qlqr,'está em letras minúsculas?',qlqr.islower())
print(qlqr,'está em letras maiúsculas?',qlqr.isupper())
print(qlqr,'está capitalizado?',qlqr.istitle())
print(qlqr,'é um decimal',qlqr.isdecimal())
print(qlqr, 'é um digito?', qlqr.isdigit())
print(qlqr,'é um indentificador?',qlqr.isidentifier())
print(qlqr,'é printável?',qlqr.isprintable())
print(qlqr,' é essa coisa que eu não sei o nome?',qlqr.__init_subclass__())

