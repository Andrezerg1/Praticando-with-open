#lista de exercicios with open

# Crie um programa que abra um arquivo chamado texto.txt usando with open e exiba todo o conteúdo na tela.
endereco_arquivo = 'C:\\Users\Andre\\Desktop\\Projetos python\\tratamento de arquivos\\texto.txt'

with open (endereco_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#Abra um arquivo dados.txt e imprima cada linha separadamente, removendo os espaços em branco extras no final de cada linha.
endereco_arquivo2 = 'C:\\Users\Andre\\Desktop\\Projetos python\\tratamento de arquivos\\dados.txt'

with open (endereco_arquivo2, 'r') as arquivo2:
    for linha in arquivo2:
        linha = arquivo2.read()
        print(linha)

#Usando with open, conte quantas linhas existem em um arquivo chamado relatorio.txt e exiba o total.
endereco_arquivo3 = 'C:\\Users\Andre\\Desktop\\Projetos python\\tratamento de arquivos\\relatorio.txt'
contador = 0

with open (endereco_arquivo3, 'r') as arquivo3:
    for linha in arquivo3:
        contador += 1

print(contador)

#Abra um arquivo artigo.txt e conte quantas palavras existem no texto.
endereco_arquivo4 = 'C:\\Users\Andre\\Desktop\\Projetos python\\tratamento de arquivos\\texto.txt'
contador = 0

with open (endereco_arquivo4, 'r') as arquivo4:
    for linha in arquivo4:
        palavras = linha.split()
        contador += len(palavras)

print(contador)

#Crie um programa que peça ao usuário para digitar uma frase e salve essa frase em um arquivo chamado frases.txt usando modo de escrita ("w").
with open ('frases.txt', 'w', encoding='utf8') as frases:
    conteudo = input('Insira o seu texto\r\n')
    frases.write(f'{conteudo}\n')

with open('frases.txt', 'a', encoding='utf8') as frases:
    conteudo = input('Adicione outro texto\r\n')
    frases.write(conteudo)    
