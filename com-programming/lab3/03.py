import math
num = math.log10(float(input()))
print(f"{(num):.1f}") if num.is_integer() else print(f"{(num):.5f}")



import math
num = math.log10(float(input()))
print(num.round(0, 6))