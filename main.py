"""
xi = 300 / 5
t1 = 15
t2 = 7
x2 = (xi * t2) / t1
print(xi)
print(t1)
print(t2)
print(x2)
resultado = x2 * 8
print(resultado)

"""
pedras1 = int(input("Quantas pedras? "))
bateria1 = int(input("Quantas bateriais? "))
bateria2 = int(input("Quantas bateriais? "))
tempo1 = int(input("Quantos minutos? "))
tempo2 = int(input("Quantos minutos? "))
pedras2 = int(((pedras1 / bateria1) * tempo2) / tempo1)
print(pedras2)

pedras_minuto = 4
pedras_minuto2 =


print(str("Se uma catapulta lança {} por minuto em {} bateria de {} minuts, quantas pedras ela vai lançar em "))

print(str("Uma catapulta lança {} pedras em {} baterias de {} minutos cada. Quantas pedras ela laçaria em {} baterias de {} minutos? Ela lançaria {} pedras. ").format(pedras_minuto, bateria1, tempo1,bateria2, tempo2, pedras2))


