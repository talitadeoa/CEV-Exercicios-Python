#Um programa que cria uma lista de compras com nome e preço e ao final informa o total gasto nas compras, quantos produtos custam mais de R$1000 e qual o produto mais barato

product = ''
count = cheapest = price = 0
shopping = []
prices = []
mt1000 = []

while True: 
    product = input('Qual o produto? ')
    shopping.append(product)
    price = int(input('Qual o valor do produto? R$'))
    prices.append(price)
    count+=1
    if price >= 1000:
        mt1000.append(p)
    if count == 1:
        cheapest = price
    else:
        if price < cheapest:
            cheapest = count
    stop = input('Deseja cadastrar mais um produto? [S/N] ').upper()
    while stop not in ['S','N']:
        stop = input('Deseja cadastrar mais um produto? [S/N] ').upper()
    if stop == 'S':
        count+=1
    if stop == 'N':
        break

print(f'O total das compras foi: R${sum(prices):.2f} \n{len(mt1000)} Produtos custaram mais de R$1000 \nO produto mais barato foi {shopping[cheapest]} custando {prices[count-1]}')        