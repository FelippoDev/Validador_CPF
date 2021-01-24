print('<<<< VALIDADOR DE CPF >>>>')
cont = 0
cpf = str(input('Informe o CPF: '))
fixa = [10, 9, 8, 7, 6, 5, 4, 3, 2]
n_cpf = []
for x in cpf:
    if x.isnumeric():
        if cont < 9:
            cont += 1
            n_cpf.append(int(x))

validador_n1 = list(zip(n_cpf, fixa))
validador_n1 = [a * b for (a, b) in validador_n1]
validador_n1 = (sum(validador_n1) * 10) % 11
if validador_n1 == 10:
    validador_n1 = 0

if str(validador_n1) != cpf[-2]:
    print('CPF inválido!')
else:
    fixa = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    n_cpf.append(validador_n1)
    validador_n2 = list(zip(n_cpf, fixa))
    validador_n2 = [a * b for (a, b) in validador_n2]
    validador_n2 = (sum(validador_n2) * 10) % 11
    if validador_n2 == 10:
        validador_n2 = 0
    if str(validador_n1) == cpf[0] or str(validador_n1) == cpf[1] or str(validador_n1) == cpf[2]:
        print('CPF inválido!')
    else:
        if str(validador_n1) + str(validador_n2) == cpf[-2:]:
            print('CPF válido!')
        else:
            print('CPF inválido!')