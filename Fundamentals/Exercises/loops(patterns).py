# LOOPS >> PATTERNS
# PATTERN 1:
print("(*,*)" *5, "Loops >> PATTERNS: PATTERN 1: Simple right triangle:", "(*,*)" *5)

for i in range(1, 7):
  for j in range(1, i + 1):
    print("*", end="")
  print()

print(end="\n\n")

print("(*,*)" *5, "Loops >> PATTERNS: PATTERN 2: Simple right triangle reverse:", "(*,*)" *5)

q = 8
for i in range(1, 7):
  for j in range(1, q - i):
    print("*", end="")
  print()


print(end="\n\n")

print("(*,*)" *5, "Loops >> PATTERNS: PATTERN 3: Right triangle (with distance):", "(*,*)" *5)

q = 8
for i in range(1, 7):
  print(" " * (q - i), end="")
  for j in range(1, i + 1):
    print("*", end="")
  print()

print(end="\n\n")

print("(*,*)" *5, "Loops >> PATTERNS: PATTERN 4: Complete pyramid:", "(*,*)" *5)

k = 8
step = 1
for i in range(1, 7):
  print(" " * (k - i), end="")
  for j in range(1, i + step):
    print("*", end="")
  if i % 2 == 0:
    step += 1
  elif i % 2 == 1:
    step += 1
  print()

print(end="\n\n")

print("(*,*)" *5, "Loops >> PATTERNS: PATTERN 5: Inverted right triangle:", "(*,*)" *5)

p = 8
step_2 = 7
for i in range(1, 7):
  print(" " * (p - step_2), end="")
  for j in range(1, p - i):
    print("*", end="")
  print()
  step_2 -= 1
  