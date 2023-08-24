palabras = input("Escriba una frase para contar cuantas vocales tiene: ")
vocales = ['a','e','i','o','u']
palabras = palabras.lower()

for vocal in vocales:
    print(vocal, palabras.count(vocal))