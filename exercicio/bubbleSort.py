import sys
from time import time
sys.dont_write_bytecode = True  # Impede a criação do cache
import sys, tracemalloc


from vehicles10k import vehicles
vehicles = vehicles[:10000]

def bubble_sort(lista):
    global comps, trocas, passd
    comps = trocas = passd = 0  # Inicializando contadores

    n = len(lista)
    for i in range(n - 1):
        trocou = False
        passd += 1  # Conta as passadas

        for j in range(n - 1 - i):
            comps += 1  # Conta comparações
            if lista[j] > lista[j + 1]:  # Compara dois elementos vizinhos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1  # Conta trocas
                trocou = True

        if not trocou:
            break  # Se não houve trocas, a lista já está ordenada
###################################################################################
tracemalloc.start() 
hora_ini = time()
bubble_sort(vehicles)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles)
print(f"Comparações: {comps}; Trocas: {trocas}; Passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000:.2f}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")
