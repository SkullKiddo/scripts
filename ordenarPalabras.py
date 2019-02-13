from collections import Counter

file = open("wordlist.txt","r")
palabras = file.read().split("\n")
entrada = []
for i in range(10):
    entrada.append(input())
    input()
resultados = []
for garbage in entrada:
    for palabra in palabras:
        if Counter(palabra) == Counter(garbage):
            resultados.append(palabra)
            break
print(",".join(resultados))