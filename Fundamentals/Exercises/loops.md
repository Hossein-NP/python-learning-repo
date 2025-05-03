<pre>
```
num = int(input("Please enter only one number.(e.g.,1, 3, 4, ...): "))
for i in range(1, 6):
  multipli = num * i
  print(f"{num} * {i}= ", num * i, end="\t")  #You can customize the column spacing with the end parameter.
  i += 5
  for j in range(1, 2):
    print(f"{num} * {i}= ", num * i)

```
</pre>