word = input("Enter the word to convert: ")
count = int(input("How many letters at the end of the word should be converted:"))
start = word[:-count]
end = word[-count:]
result = start + end.upper()
print("Converted word:", result)