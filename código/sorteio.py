# Código utiliza os conhecimentos de estruturas de repetição e listas.
# Nome dos participantes: André Gustavo Xavier dos Santos, Lucas Gabriel Pereira Pestana, Marcus Fernando Santos Cuba, Samuel Victor Avelino Araújo, Miguel Farias Ramos Araújo, Christhian Gabriel Carvalho Gonçalves e Pedro Lucas Pires Lopes

print('~' * 30)
print(' UNDB - SORTEIO DE LIVROS   ')
print('~' * 30)

import random

# Lista de nomes dos livros
livros = ['O Senhor dos Anéis', 'Harry Potter e a Pedra Filosofal', 'A Guerra dos Tronos', '1984', 'Dom Casmurro', 'Cem Anos de Solidão']

# Lista de participantes
participantes = []

# (repetição) Laço para cadastro dos participantes 
print('=== CADASTRO DE PARTICIPANTES ===')
while True:
    nome = input('Digite o nome do participante (ou "sortear" para encerrar): ').lower()
    if nome == 'sortear':
        break
    participantes.append(nome)

# Sorteio dos vencedores (vão ser apenas 3 ganhadores)
vencedores = random.sample(participantes, 3) 

# Resultado mostrando quem são os 3 vencedores e os livros sorteados
print('\n=== SORTEIO DOS VENCEDORES ===')
print('Os 3 vencedores são:')
for i, vencedor in enumerate(vencedores):
    print(f'{i+1}º lugar: {vencedor}')
    livro = random.choice(livros)
    livros.remove(livro)
    print(f'Livro sorteado: {livro}')

print('~' * 20)
print(' FIM DO SORTEIO   ')
print('~' * 20)
