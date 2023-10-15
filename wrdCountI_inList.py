# Count the occurrences of each word in a list of sentences.
# Function to count word occurrences in a list of sentences
def count_word_occurrences(sentences):
    word_count = {}

    for sentence in sentences:
        # Split the sentence into words
        words = sentence.split()

        for word in words:
            # Remove punctuation and convert to lowercase for case-insensitive counting
            word = word.strip(".,!?;").lower()

            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

# Sample list of sentences
sentences = [
    "This is a sample sentence.",
    "Another sample sentence with a sample word."
]

# Count word occurrences in the list of sentences
word_occurrences = count_word_occurrences(sentences)

# Print the word occurrences
for word, count in word_occurrences.items():
    print(f"{word}: {count}")
