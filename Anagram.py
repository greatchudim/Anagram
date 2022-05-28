def find_anagram(word, anagram):
    if (sorted(word)== sorted (anagram)):
        return True
    else:
        return False

word = input("What is the First Word? \n ")
anagram = input("What is the Second Word? \n")

print(find_anagram(word, anagram))
