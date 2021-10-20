from morse_code import morse_code_dictionary


def get_translation(input_string):
    """This function takes any string input and converts it into Morse Code"""
    translated_word_list = []

    # Split string into individual words
    word_list = input_string.split()

    # Iterate through words in string
    for word in word_list:
        # Split word into letters
        letters_in_word = list(word)

        translated_letters = []

        # Iterate through letters in word
        for char in letters_in_word:
            if char in morse_code_dictionary:
                translated_letters.append(morse_code_dictionary[char])

        # Combine translated letters into translated word
        translated_word = " ".join(translated_letters)

        translated_word_list.append(translated_word)

    # Combine translated words into full text
    translation = "/".join(translated_word_list)

    return translation


print("Welcome to the text to morse code converter.")
text_to_convert = input("Enter the text you would ike to translate into Morse Code: ").upper()
translated_text = get_translation(text_to_convert)
print(f"The Morse Code translation is:\n{translated_text}")
