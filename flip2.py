import random
random.seed(0)

N = 1000    # Number of passes through loop
H = 0       # Number of heads
T = 0       # Number of tails

for _ in range(N):
    flip = random.choice(['H', 'T'])
    if flip == 'H':
        H += 1
    else:
        T += 1
        
print(f"After {N} attempts, there were {H} heads and {T} tails.")  
