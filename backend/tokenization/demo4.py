word=input("Enter a word:") or "GenAi"

print("word:",word)
print("Length of the word:",len(word))
Characters=list(word)
print("Characters in the given word:",Characters)
pais=list(zip(Characters,Characters[0:]))
print("Adjacent pairs:",pais)
