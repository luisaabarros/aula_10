lst_vendas = []
resposta = 's'
venda = 1
tentativa = 1

while resposta != 'n':
    try:
        valor = float(input(f'Informe o valor da {venda}ª venda: '))
    except ValueError:
        print('Informe apenas numeros')
    except KeyboardInterrupt:
        print('\nUsuário encerrou operação.')
        break
    else:
        lst_vendas.append(valor)
        resposta = input('Deseja continuar? \n[s/n] ')[0].lower()
        venda += 1
    finally:
        print(f'Tentativa {tentativa}.')
        tentativa += 1
    
print(f'Vendas registradas {lst_vendas}.')