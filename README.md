# Validador_CPF
Validador de CPF em python

Para validar um CPF, nós usamos os 9 primeiros dígitos para encontrar quais são os 2 digítos verificadores corretos, e verificamos se esses dois digítos encontrados, através da aplicação de uma fórmula, são iguais aos 2 últimos dígitos do CPF que temos em mãos


Validador está contido na função `val_cpf`, toda funcionalidade de validação e entrada de dados é feito através da chamada desta função


## Função val_cpf
Nesta função temos todo o codigo que será feito para realizar o validador.



Neste início temos a entrada de dados e os números que irão ser utilizados para o cálculo dos 9 primeiros digítos, estes números sendo guardados em uma lista na varíavel `fixa`.
```python
def val_cpf():
    cont = 0
    cpf = str(input('Informe o CPF: '))
    fixa = [10, 9, 8, 7, 6, 5, 4, 3, 2]
```


No trecho a seguir temos a presença de um for loop para realizar o tratamento do dado informado pelo user, iterando sobre cada dígito contido na varíavel, vale ressaltar que se o input recebido não for do tipo `str` não será possível realizar a iteração. Realizado a iteração, será feito uma checagem se o dado contido em `x` é numérico, se for numérico irá ser adicionado a lista `n_cpf`. 

```python
    for x in cpf:
        if x.isnumeric():
            if cont < 9:
                cont += 1
                n_cpf.append(int(x))
```

Adiante nós temos o início do cálculo para a validação do CPF informado pelo user. Juntando a lista `n_cpf` com a lista `fixa` multiplicando então cada dupla de número feito através do comando `zip()` e esse resultado sendo inserido dentro da varíavel `validador_n1`, substituindo então o dado que estava dentro desta lista, depois sendo realizado a soma de todos os valores contidos na lista e o resultado destes valores sendo multiplicados por 10 e por último... pegando o resto da divisão do resultado deste cálculo por 11. 
Ao final temos a verificação do primeiro digíto descoberto, se o dígito revelado for igual ao primeiro dígito(sem contar os 9 primeiros dígitos do CPF) o processo de validação continuará se não, teremos o CPF como inválido.
```python
    validador_n1 = list(zip(n_cpf, fixa))
    validador_n1 = [a * b for (a, b) in validador_n1]
    validador_n1 = (sum(validador_n1) * 10) % 11
    if validador_n1 == 10:
        validador_n1 = 0
    if str(validador_n1) != cpf[-2]:
        print('CPF inválido!')
```

Temos agora a validação do segundo dígito, com a diferença de que irá ser adicionado o dígito, confirmado na validação, na lista `n_cpf` e sendo também adicionado mais um número da lista `fixa` para então realizar a validação do segundo dígito. 
Se o segundo dígito for igual ao produto achado na equação então o CPF é valido.
```python 
        fixa = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        n_cpf.append(validador_n1)
        validador_n2 = list(zip(n_cpf, fixa))
        validador_n2 = [a * b for (a, b) in validador_n2]
        validador_n2 = (sum(validador_n2) * 10) % 11
        if validador_n2 == 10:
            validador_n2 = 0
        if n_cpf[0] == sum(n_cpf) / len(n_cpf):
            print('CPF inválido!')
        else:
            if str(validador_n1) + str(validador_n2) == cpf[-2:]:
                print('CPF válido!')
            else:
                print('CPF inválido!')
```

Se o user informar que o número CPF é uma sequência de números repetidos haverá uma falha que poderia acabar por invalidar a autênticidade do codigo. Para então, impedir que está falha ocorrá foi criado este algoritmo. Se o primeiro número informado pelo user for igual a soma de todos esses números informados pelo user dividos pela quantidade de digitos informados então o CPF será dado como Invalido, impedindo então que está falha no algoritmo ocorrá.  

```python
    if n_cpf[0] == sum(n_cpf) / len(n_cpf):
        print('CPF inválido!')
```



##Contribuidores
@[FelippoDev](https://github.com/FelippoDev)



