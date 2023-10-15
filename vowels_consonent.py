# Count the number of vowels and consonants in a string
# Sample string
my_string = "Hello, World!"

# Initialize counters for vowels and consonants
vowel_count = 0
consonant_count = 0

# Define a set of vowels (both uppercase and lowercase)
vowels = "aeiouAEIOU"

# Iterate through the characters in the string
for char in my_string:
    # Check if the character is an alphabet letter
    if char.isalpha():
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the counts
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
