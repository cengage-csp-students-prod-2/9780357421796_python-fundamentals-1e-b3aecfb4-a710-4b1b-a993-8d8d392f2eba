calc = 0 
for even in range (6, 16,2):
    for odd in range (5, 16, 2):
        calc = even + odd
        print(f"{even} + {odd} = {calc}")