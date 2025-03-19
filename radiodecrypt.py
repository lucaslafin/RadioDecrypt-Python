#Exercicio 4, lista 2

import os
import re

palavras = []

def limpar_terminal():
    '''Função para limpar o terminal de acordo com o S.O'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
        
def programa():
    '''Função da funcionalidade do programa'''
    print('Escreva sua mensagem abaixo (máximo 250 caracteres):')
    texto = input('').strip()
    if len(texto) > 250:
        print("A cadeia de caracteres deve ter no máximo 250 caracteres.Aperte enter para voltar")
        voltar_um = input('')
        if voltar_um == '':
            limpar_terminal()
            programa()
    else:        
        numeros = re.findall(r'\d+', texto)
        for numero_str in numeros:
            numero = int(numero_str)  
            if numero > 100:
                posicao = texto.index(numero_str) + len(numero_str) 
                parte_seguinte = texto[posicao:]  
                palavra = re.search(r'\D+', parte_seguinte)  
                if palavra:
                    palavra_limpa = re.sub(r'[^a-zA-Z]', '', palavra.group())  
                    palavras.append(palavra_limpa)  
                    
        mensagem_final = ''.join(palavras)          
        print(f'\n\nPalavras encontradas: {mensagem_final}\n\nDeseja continuar?\n[1]Transcrever nova mensagem\n[2]Sair')
        voltar = input('')
        if voltar == '1':
            limpar_terminal()
            palavras.clear()
            programa()
        elif voltar == '2':
            limpar_terminal()

def main():
    limpar_terminal()  
    programa()

if __name__ == '__main__':
    main()