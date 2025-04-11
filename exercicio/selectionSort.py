import sys
from time import time
sys.dont_write_bytecode = True
import sys, tracemalloc

from vehicles10k import vehicles
vehicles = vehicles[:10000]

comps = trocas = passd = 0

def selection_sort(lista):
    global comps, trocas, passd
    comps = trocas = passd = 0
    for pos_sel in range(len(lista) - 1):
        passd += 1
        pos_menor = pos_sel + 1
        for pos in range(pos_menor + 1, len(lista)):
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

########################################################################### 
tracemalloc.start() 
hora_ini = time()
selection_sort(vehicles)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles)
print(f"Comparações: {comps}; Trocas: {trocas}; Passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000:.2f}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")