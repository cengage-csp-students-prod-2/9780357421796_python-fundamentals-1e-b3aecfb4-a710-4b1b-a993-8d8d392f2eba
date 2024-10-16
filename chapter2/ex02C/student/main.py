sentence = input("Enter a sentence: ")
substring = input("Word to look for in sentence ")

sanitized_sentence = sentence.replace(" ", "").lower()  # Remove whitespace and convert to lowercase
sanitized_substring = substring.lower()  # Convert substring to lowercase

count = sanitized_sentence.count(sanitized_substring)

print(f"The word '{substring}' occurs {count} times in the sentence.")
