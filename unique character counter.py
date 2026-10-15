sentence = input("Enter a long sentence:")
unique_characters = set(sentence.replace("", ""))

print("Unique characters:",unique_characters)
print("Total unique characters:",len(unique_characters))