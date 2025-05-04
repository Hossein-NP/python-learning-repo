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