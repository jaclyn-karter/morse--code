# create a morse code converter

# prompt user for their input
user_input = input("Hello there, please type a word or sentence and watch it convert into morse code :\n ").upper()
while True:
    try:
        # Assign each letter in the alphabet with their morse sequence
        letters = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
            "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
            "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--..", " ": " ",
        }
        # store user input
        input_list = list(user_input)

        # take user input and use a for loop to assign each character to its morse code sequence and print string
        for word in user_input:
            word = letters[word]
            print(word, end='')
    # catch errors
    except KeyError:
        user_input = input("Sorry only letters are accepted. Please try again. \n ").upper()

    else:
        break


















