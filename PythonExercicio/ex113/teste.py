# Reescreva a função leiaInt do desafio 104, incluindo agora a possibilidade da digitação d eum número tipo inválido.
# Aproveite e crie também uma função leiaFloat com a mesma funcionalidade

from PythonExercicio.ex113.ex113 import leiaInt
from PythonExercicio.ex113.ex113 import leiaFloat

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')
