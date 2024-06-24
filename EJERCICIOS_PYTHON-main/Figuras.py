# Cuadrado
size = 5
print("Cuadrado:")
for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)
    else:
        print('* ' + '  ' * (size - 2) + '*')

print()

# Rectángulo
width = 6
height = 3
print("Rectángulo:")
for i in range(height):
    if i == 0 or i == height - 1:
        print('* ' * width)
    else:
        print('* ' + '  ' * (width - 2) + '*')

print()

# Triángulo
size = 7
print("Triángulo:")
for i in range(size):
    if i == size - 1:
        print('* ' * (i + 1))
    else:
        print('* ' * (i + 1))

print()

# Rombo
size = 7
print("Rombo:")
for i in range(size):
    if i <= size // 2:
        print(' ' * (size - i - 1) + '* ' * (i + 1))
    else:
        print(' ' * (i) + '* ' * (size - i))
