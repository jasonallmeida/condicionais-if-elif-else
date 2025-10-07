print('Bem vindo a loja do Jason Luan Frazão de Almeida!') #Tela de boas-vindas 
 
valorDoPedido = float(input('Entre com o valor do pedido: ')) #Entrada do valor do pedido 
quantidadeParcelas = int(input('Entre com a quantidade de parcelas: ')) #Entrada da quantidade de parcelas 
 
if quantidadeParcelas < 4: # Juros de 0% 
    juros = 0 / 100 
    valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas 
    valorTotalParcelado = valorDaParcela * quantidadeParcelas 
 
    print('O valor das parcelas é de:R$ %.2f' % valorDaParcela) 
    print('O valor Total Parcelado é de: R$: %.2f' % valorTotalParcelado) 
 
elif 4 <= quantidadeParcelas < 6: #Juros de 4% 
    juros = 4 / 100 
    valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas 
    valorTotalParcelado = valorDaParcela * quantidadeParcelas 
 
    print('O valor das parcelas é de:R$ %.2f' % valorDaParcela) 
    print('O valor Total Parcelado é de: R$: %.2f' % valorTotalParcelado) 
 
elif 6 <= quantidadeParcelas < 9: #Juros de 8% 
    juros = 8/ 100 
    valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas 
    valorTotalParcelado = valorDaParcela * quantidadeParcelas 
 
    print('O valor das parcelas é de:R$ %.2f' % valorDaParcela) 
    print('O valor Total Parcelado é de: R$: %.2f' % valorTotalParcelado) 
 
elif 9 <= quantidadeParcelas < 13: #Juros de 16% 
    juros = 16/ 100 
    valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas 
    valorTotalParcelado = valorDaParcela * quantidadeParcelas 
 
    print('O valor das parcelas é de:R$ %.2f' % valorDaParcela) 
    print('O valor Total Parcelado é de: R$: %.2f' % valorTotalParcelado) 
 
else: # Juros de 32% 
    juros = 32 / 100 
    valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas 
    valorTotalParcelado = valorDaParcela * quantidadeParcelas 
 
    print('O valor das parcelas é de:R$ %.2f' %valorDaParcela) 

    print('O valor Total Parcelado é de: R$: %.2f' %valorTotalParcelado) 
