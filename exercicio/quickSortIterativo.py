import sys
from time import time
sys.dont_write_bytecode
import sys, tracemalloc

from vehicles80k import vehicles
vehicles = vehicles[:80000]

def quick_sort_iterativo(lista):
    global passd, comps, trocas
    passd = comps = trocas = 0
    
    pilha = [(0, len(lista) - 1)]

    while pilha:
        ini, fim = pilha.pop()
        passd += 1

        if ini >= fim:
            continue

        # Particionamento
        pivot = fim
        div = ini - 1
        for pos in range(ini, fim):
            comps += 1
            if lista[pos] < lista[pivot]:
                div += 1
                if pos != div:
                    lista[pos], lista[div] = lista[div], lista[pos]
                    trocas += 1

        div += 1
        comps += 1
        if lista[pivot] < lista[div]:
            lista[div], lista[pivot] = lista[pivot], lista[div]
            trocas += 1

        # Adiciona as subfaixas à pilha
        pilha.append((ini, div - 1))
        pilha.append((div + 1, fim))
###################################################################################
tracemalloc.start()   
hora_ini = time()
quick_sort_iterativo(vehicles)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles)  # Imprime a lista ordenada
print(f"Comparações: {comps}; Trocas: {trocas}; Passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000:.2f}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")