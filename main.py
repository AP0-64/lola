# INT / INTEGER
# ex : 1, -4, 0

# FLOAT
# ex : 1.5, -0.3, 0.0, 3.0, 2.000001

# STR / STRING / CHAINE DE CARACTERES
# ex : "hello", 'world', "123", "", ' '

# BOOL / BOOLEAN
# ex : True, False

a = 10         # int
test = -3.14      # float
c = "Hello World"    # str
d = True       # bool
m = 5

print(a)
print(test)
print(c)
print(d)
print()

# + - * / // % **

print(10 == 1)  # False
print(10 == "10") # False
print(a != 10)  # False
print(a > 5) # True
print(a < 20)   # True
print(a >= 10)  # True
print(a <= 9)   # False
print()

if m > 5:
    print("m est plus grand que 5")
elif m == 5:
    print("m est egal a 5")
else:
    print("m est plus petit ou egal a 5")
print()

if 10 > 5 and 2 < 3:
    print("Les deux conditions sont vraies")
if 10 > 5 or 2 > 3:
    print("Au moins une des conditions est vraie")
print()

while m > 0:
    print("m vaut :", m)
    m = m - 1
print("Boucle terminee")
print()

for i in range(5):
    print("i vaut :", i)
print("Boucle terminee")
print()

while True:
    a = a + 1
    print(a)
    if a == 100:
        break
print()

# Exemple avec continue
for i in range(5):
    print("aaaaaaaaa")
    if i == 2:
        continue  # Passe à l'itération suivante si i vaut 2
    print("i vaut :", i)
    print()
print("Boucle avec continue terminee")

def test_function(x, y=0):
    x = x + 1
    x = x * 2
    return x

result = test_function(9, 5)
print("Le résultat de la fonction est :", result)

res = test_function(50)
