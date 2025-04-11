import sys
from time import time
sys.dont_write_bytecode
import sys, tracemalloc

from vehicles80k import vehicles
vehicles = vehicles[:80000]
passd = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    global passd, comps, trocas
    passd += 1

    if fim is None: fim = len(lista) - 1
    if fim <= ini: return
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
    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

###################################################################################
tracemalloc.start()   
hora_ini = time()
quick_sort(vehicles)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles)  # Imprime a lista ordenada
print(f"Comparações: {comps}; Trocas: {trocas}; Passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000:.2f}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")