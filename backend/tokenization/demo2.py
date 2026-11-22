text=input("Enter a Sentence:") or "I LOVE LEARNING PYTHON"

print("Length=",len(text))
print("Characters in the given text:")
for ch in text:
    print(ch,end=",")