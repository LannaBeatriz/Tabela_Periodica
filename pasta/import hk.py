import time
lista = list(range(1000000))
start_time = time.time()
lista = [x for x in lista if x %2 == 0]
end_time = time.time()
print(f"Tempo de execução: {end_time - start_time} segundos.")