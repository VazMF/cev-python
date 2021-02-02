try: # nessa área ficam os comandos que o computador irá TENTAR executar
    a = int(input('Numerador: '))
    b = int(input("Denominador: "))
    r = a /b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário não informou os dados.')
except Exception as erro:
    print(f'O erro encontrado foi: {erro}')
    print(f'A causa desse erro foi: {erro.__cause__}')
else: # aqui é onde fica a instrução caso tudo ocorra bem e o try funcione (OPCIONAL)
    print(f'O resultado da operação é {r:.2f}')
finally: # serve tanto para quando o try da certo quanto caso ele falhe (OPCIONAL)
    print('Volte sempre! Muito obrigado :)')
