entrada = input('digite algo')

print(f'Tipo primário: {type(entrada)}')
print(f'É numérico: {entrada.isnumeric()}')
print(f'É alfanumérico: {entrada.isalpha()}')
print(f'Esta tudo em maiúsculo: {entrada.isupper()}')
print(f'Esta tudo em minúsculo: {entrada.islower()}')
print(f'É um decimal: {entrada.isdecimal()}')
