def horner_rule(koef, x):
    hasil = koef[0]
    for i in range(1, len(koef)):
        hasil = hasil * x + koef[i]
    return hasil
# Evaluasi polinomial x^3 + 2x^2 + 3x + 4 pada x = 2
koef = [1, 2, 3, 4]
x = 2
result = horner_rule(koef, x)
print(result)