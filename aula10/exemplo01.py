def calcula_meta(v, m):
    r = v / m
    return r * 100


for num in range(1, 4):
    try:
        venda = float(input('Informe o valor da venda: '))
        meta = float(input('Informe a meta: '))
        resultado = calcula_meta(venda, meta)

    except ValueError:
        print('Erro! Apenas números.')
    except ZeroDivisionError:
        print('Erro! Meta não pode ser 0.')
    except KeyboardInterrupt:
        print('\nOperação encerrada pelo usuário.')
    else:
        print(f'Resultado: {resultado}%')
    finally:
        print('Operação finalizada.')
