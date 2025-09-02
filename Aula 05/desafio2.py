lado = int(input("digite o tamanho do lado: "))
lado2 = int(input("digite o tamanho do lado: "))
lado3 = int(input("digite o tamanho do lado: "))

if lado == lado2 == lado3:
    print("Você tem um triangulo equilatero")
elif lado == lado2 != lado3:
    print("Você tem um triangulo Isosceles")
else:
    print("Você tem um triangulo Escaleno")
    