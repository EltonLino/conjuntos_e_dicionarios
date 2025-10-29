estoque = { 
    "Caderno universitário": 50, 
    "Caneta azul": 120, 
    "Borracha branca": 30 
} 

print(estoque)

produto = input('Nome do produto que deseja atualizar: ')
nova_quantidade = int(input('Nova quantidade: '))

estoque.update({produto:nova_quantidade})

print(estoque)