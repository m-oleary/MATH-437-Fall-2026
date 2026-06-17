import random
random.seed(0)

N = 100000    # Number of passes through loop
count = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

while sum(count.values())<N:
    x1 = random.choice([1,2,3,4,5,6])
    x2 = random.choice([1,2,3,4,5,6])
    count[x1+x2] += 1

print (f"The die is thrown {N} times")
for key in sorted(count.keys()):
    subtotal = count[key]
    fraction = subtotal/N
    print(f"Number of {key:2}s is {subtotal:5}, "
           f"which is approximately {fraction:6.2%}")
