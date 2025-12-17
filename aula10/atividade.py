# ATIVIDADE 01
#VSCode - GitHub
def soma_valores(v1, v2):
    t = v1 + v2
    return t

for n in range(3):
    try:
        valor1 = int(input('Informe o 1º valor: '))
        valor2 = int(input('Informe o 2º valor: '))
        total = soma_valores(valor1, valor2)
    except ValueError:
        print('Erro! Apenas numeros.')
    except KeyboardInterrupt:
        print('\nOperação encerrada pelo usuário.')
    else:
        print(f'O resultado da soma dos números é {total}!')
    finally:
        print('Operação finalizada.')
    
