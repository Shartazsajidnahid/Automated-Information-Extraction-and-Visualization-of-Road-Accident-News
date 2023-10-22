def bengali_stem(word):
    # Define a list of suffixes to remove
    suffixes = ["ের", "ে"]

    # Iterate through the suffixes and remove them if they exist at the end of the word
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break

    return word

# Example words
words = ["মোটরসাইকেলের", "মোটরসাইকেলে", "ট্রাকের", "ট্রাকে", "ট্রেনের"]

# Stem the words
stems = [bengali_stem(word) for word in words]

# Print the results
for i in range(len(words)):
    print(f"Original: {words[i]}\tStemmed: {stems[i]}")
