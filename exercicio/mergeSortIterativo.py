import sys
from time import time
sys.dont_write_bytecode = True
import sys, tracemalloc

from vehicles80k import vehicles
vehicles = vehicles[:80000]
passd = comps = trocas = 0

def merge_sort(lista):
    global passd, comps, trocas

    tam_part = 1
    n = len(lista)

    while tam_part < n:
        esq = 0
        while esq < n:
            dir = min(esq + (tam_part * 2 - 1), n - 1)
            meio = (esq + dir) // 2
            if tam_part > n // 2:
                meio = dir - (n % tam_part)

            tam_esq = meio - esq + 1
            tam_dir = dir - meio
            lista_esq = [0] * tam_esq
            lista_dir = [0] * tam_dir

            for pos_esq in range(tam_esq):
                lista_esq[pos_esq] = lista[esq + pos_esq]
            for pos_dir in range(tam_dir):
                lista_dir[pos_dir] = lista[meio + pos_dir + 1]

            pos_esq, pos_dir, i = 0, 0, esq
            while pos_esq < tam_esq and pos_dir < tam_dir:
                comps += 1
                if lista_esq[pos_esq] > lista_dir[pos_dir]:
                    lista[i] = lista_dir[pos_dir]
                    pos_dir += 1
                    trocas += 1
                else:
                    lista[i] = lista_esq[pos_esq]
                    pos_esq += 1
                    trocas += 1
                i += 1

            while pos_esq < tam_esq:
                lista[i] = lista_esq[pos_esq]
                pos_esq += 1
                i += 1
                trocas += 1

            while pos_dir < tam_dir:
                lista[i] = lista_dir[pos_dir]
                pos_dir += 1
                i += 1
                trocas += 1

            esq += tam_part * 2
            passd += 1  # Cada fusão de sublistas é uma passada

        tam_part *= 2
    return lista

############################################################
tracemalloc.start()   
hora_ini = time()
merge_sort(vehicles)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print(vehicles)
print(f"Comparações: {comps}; Trocas: {trocas}; Passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000:.2f}ms.\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024} MB")