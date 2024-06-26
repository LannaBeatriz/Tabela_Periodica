import time
lista = list(range(1000000))
start_time = time.time()
i = 0
while i < len(lista):
    if lista [i] % 2 != 0:
            lista.pop(i)
    else:
          i += 1
end_time = time.time()
print(f"Tempo de execução: {end_time - start_time} segundos.")