
import sys
from time import time
sys.dont_write_bytecode = True  # Impede a criação do cache

import sys, tracemalloc
from vehicles80k import vehicles
vehicles = vehicles[:80000]

# Variáveis de estatística
divs = juncs = comps = 0

def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT
    No processo de ordenação, este algoritmo "desmonta" a lista
    original, contendo N elementos, até obter N listas com apenas
    um elemento cada uma. Em seguida, usando a técnica de mesclagem
    (merging), "monta" uma nova lista, com os elementos ordenados.
    """
    global divs, juncs, comps

    # PARTE 1: DIVISÃO DA LISTA ORIGINAL EM (SUB)LISTAS MENORES

    # Para que possa haver divisão da lista, esta deve ter mais de
    # um elemento. Caso contrário, sai da função retornando a própria
    # lista
    if len(lista) <= 1: return lista

    # Calcula a posição do meio da lista, para fazer a divisão em
    # duas metades
    meio = len(lista) // 2

    # Tira uma cópia (usando fatiamento) da primeira metade da lista
    sublista_esq = lista[:meio]
    # Tira uma cópia (usando fatiamento) da segunda metade da lista
    sublista_dir = lista[meio:]
    divs += 1

    # print("ESQ:", sublista_esq, "; DIR:", sublista_dir)

    # Chamamos recursivamente a própria função para que ela continue
    # repartindo cada sublista em duas partes menores
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # PARTE 2: REMONTAGEM DE LISTA, DE FORMA ORDENADA
    
    pos_esq = pos_dir = 0

    # Inicializando duas listas vazias na mesma linha
    ordenada, sobra = [], []

    # Percorremos as sublistas esquerda e direita, comparando seus elementos
    # e os inserindo em ordem na lista ordenada
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        comps += 1
        # O menor elemento está na sublista esquerda
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1
        # O menor elemento está na sublista direita
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI

    # Verifica se há sobras na sublista da esquerda
    if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:]
    # A sobra pode estar também na sublista da direita
    else: sobra = sublista_dir[pos_dir:]

    # O resultado final é a junção (concatenação) da lista ordenada
    # com a sobra
    juncs += 1
    return ordenada + sobra

########################################################################
tracemalloc.start() 
hora_ini = time()
merge_sort(vehicles)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles)  # Imprime a lista ordenada
print(f"Divisões: {divs}; junções: {juncs}; comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000:.2f}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")

