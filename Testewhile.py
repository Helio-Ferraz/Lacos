
# FOR exemple

numero = 5

for i in range(1, 11):
    print(f" {i} x {numero} = {i * numero}")


# WHILE exemple

numero = 5
i = 1

while i <= 10:
    print(f" {i} x {numero} = {i * numero}")
    i += 1


# Exemplo HELIO-FOR

Numero = int(input("Qual numero você vai começar?"))
multiplicador = int(input("Por qual numero você vai multiplicar?"))
final = int(input("Até qual numero você vai multiplicar?"))

for Numero in range(Numero, final + 1):
    print(f"{Numero} x {multiplicador} = {multiplicador * Numero}")




# Exemplo HELIO-WHILE

Numero = int(input("Qual numero você vai começar?"))
multiplicador = int(input("Por qual numero você vai multiplicar?"))
final = int(input("Até qual numero você vai multiplicar?"))
print("\n--------------------------------------------")

while Numero <= final:
    print(f" {Numero} x {multiplicador} = {multiplicador * Numero}")
    Numero += 1
