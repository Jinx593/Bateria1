# 1.
# def masimo (a, b): 
#     if a > b: return a
#     elif b > a: return b 
# val1 = masimo(11, 133)
# print(val1)

# 2. 
# def fmax3 (a,b,c):
#     if a > b and a > c: return a
#     elif b > a and b > c: return b
#     elif c > a and c > b: return c
#     else: return "Valores no válidos"
# valmax3 = fmax3(77,77,77)
# print(valmax3)

# 3. 
def longstring(texto):
    contador_ciclos = 0
    for _ in texto:
        contador_ciclos +=1
    print(contador_ciclos)

longstring("jfvvsfbjfgsjgjaGL")
