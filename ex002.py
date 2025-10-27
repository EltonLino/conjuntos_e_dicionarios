texto1 = set(input('Digite o primeiro texto: ').split())
texto2 = set(input('Digite o segundo texto: ').split())

palavras_em_comum = texto1 & texto2

print(f'Palavras em comum: {', '.join(palavras_em_comum)}')