def mutate(word):  #AI生成的例子
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mutations = set()

    # Insertion
    for i in range(len(word) + 1):
        for letter in alphabet:
            mutations.add(word[:i] + letter + word[i:])

    # Deletion
    for i in range(len(word)):
        mutations.add(word[:i] + word[i + 1 :])

    # Replacement
    for i in range(len(word)):
        for letter in alphabet:
            if letter != word[i]:
                mutations.add(word[:i] + letter + word[i + 1 :])

    # Swap
    for i in range(len(word) - 1):
        mutations.add(word[:i] + word[i + 1] + word[i] + word[i + 2 :])

    return mutations


# Testing the function
words = mutate("hello")
print("helol" in words)  # True
print("helko" in words)  # True
print(
    "helol1" in words
)  # This won't be true because we're only considering letters from a to z.
print("hell" in words)