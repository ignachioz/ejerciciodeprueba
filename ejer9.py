import string
frase=input("Ingrese una palabra o frase a analizar si es heterograma: ").lower()
heterograma=True
for caracter in frase:
    if(caracter in string.ascii_lowercase):
        if(frase.count(caracter)>1):
            heterograma=False
            print("No es un heterograma")
            break
if(heterograma):
    print(f"Es un heterograma la palabra/frase: {frase} ")
