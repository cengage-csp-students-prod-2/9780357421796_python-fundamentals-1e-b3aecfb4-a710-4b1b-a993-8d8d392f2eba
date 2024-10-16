print("Enter a number you'd like to generate a multiplication table for.") 
whole_num = int(input("Enter a whole number"))
print("-" * 10)
print("Number:", whole_num)
for i in range(2, 11):
    print(f"{i}: {whole_num * i}")
print("-" * 10)