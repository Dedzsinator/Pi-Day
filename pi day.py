from math import pi
precision = 31141592
num = 0
for i in range(precision):
    num += (-1)**i/(2*i+1)
val = 4*num
print(f"a Pi kiszamitott erteke\n" + val)