def count_characters(word):
    return len(word)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    found_vowels = [char for char in word if char in vowels]
    return len(found_vowels), found_vowels

word = input("Enter a word: ")
print("Number of characters:", count_characters(word))
vowel_count, vowel_list = count_vowels(word)
print("Number of vowels:", vowel_count)
print("Vowels found:", vowel_list)
