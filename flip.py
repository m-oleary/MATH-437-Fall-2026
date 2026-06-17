import random
random.seed(0)

N = 2000    # Number of passes through loop
H = 0       # Number of heads
T = 0       # Number of tails
while H+T<N:
    x = random.uniform(0.0,1.0)
    if x<0.5:
        H += 1
    else:
        T += 1
print(f"After {N} attempts, there were {H} heads and {T} tails.")
