r1 = float(input("Informe o valor do primeiro segmento: "))
r2 = float(input("Informe o valor do segundo segmento: "))
r3 = float(input("Informe o valor do terceiro segmento: "))

if r1 + r2 > r3 and r3 + r2 > r1 and r1 + r3 > r2:
    if r1 == r2 == r3:
        print("Essas retas podem formar um triângulo.")
        print("Esse triângulo será do tipo EQUILÁTERO")
    else:
        if r3 != r1 == r2 or r2 != r1 == r3 or r1 != r2 == r3:
            print("Essas retas podem formar um triângulo.")
            print("Esse triângulo será do tipo ISÓSCELES")
        else:
            print("Essas retas podem formar um triângulo.")
            print("Esse triângulo será do tipo ESCALENO")
else:
    print("Não é possível formar um triângulo")