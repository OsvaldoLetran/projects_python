# function to find the truht by shifting the letter by a specified amount.
def lasso_letter(letter, shift_amount):
    # ord function to translate the letter to its ASCII code.
    letter_code = ord(letter.lower())
    # the ASCII number representation of lowercase letter 'a'
    a_ascii = ord('a')
    alphabet_size = 26
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)
    # convert the ASCII number to character o letter with chr
    decoded_letter = chr(true_letter_code)
    
    return decoded_letter


# definde a function to find the truth in a secret message
def lasso_word(word, shift_amount):
    decoded_word = ""

    # this for loop iterates trough each letter in the word parameter.
    for letter in word:
        # the lasso_letter function is invoked with each letter and shift amount.
        decoded_letter = lasso_letter(letter, shift_amount)
        # decoded_letter value is added to the end of the decoded_word value.
        decoded_word += decoded_letter

    return decoded_word


if __name__ == '__main__':
    word = input('word: ')
    amount = int(input('shift amount: '))
    result = lasso_word(word, amount)
    print(result)