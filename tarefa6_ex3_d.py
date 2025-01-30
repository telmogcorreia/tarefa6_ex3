# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:38:06 2025

@author: telmo
"""

nomefich = input("Nome do ficheiro: ").lower()
nomefich = nomefich+".txt"
max = 0
nome =""
soma = 0
contar = 0

try:
    lerFicheiro = open(nomefich, "r+", encoding="utf-8")
    
except:
    print("Ficheiro não existe ou a Localização errada!!!")

else: # Garante que só executa o código se o ficheiro for aberto com sucesso.
     while True: # inicia um loop infinito para ler linha por linha.
         
         linha = lerFicheiro.readline()   # Lê uma linha do ficheiro.
         if not linha: # Se não tiver nada termina
             break
         else:
             if linha == "\n": # Se a linha for apenas uma mudança de linha ("\n"), o código não faz nada (pass).
                 pass          # Poderia usar linha.strip() para remover os espaços e evitar o (pass).
             else:
                 aluno = linha.slipt(",") # Cada linha do fich passa para uma lista nome, nota.
                 nota = int(aluno[1])
                 if nota > max:
                     max = nota
                     nome = aluno[0]
                     melhores_aluno = [aluno[0]]    # Opção para mostrar mais do que um aluno com nota maxima
                elif nota == max:
                    melhores_aluno.append(aluno[0])
                    
                soma += nota   # Acumular as notas.
                contar += 1    # Conta o numero de alunos.
                if nota >9:
                    print(f"{aluno[0]:.<25}{nota} Aprovado") # :.<25 para alinhar o texto.
                    
                else:
                    print(f"{aluno[0]:.<25}{nota} Reprovado")
                    
    print("-"*40)
    print(f"Média das notas .......{soma/contar:.2f}")
    print(f"Melhor nota: {nome:.<12} {max}")
    print("-"*40)
    lerFicheiro.close()