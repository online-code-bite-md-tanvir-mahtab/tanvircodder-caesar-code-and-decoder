# importing the art module
from art import logo
from word import alphabet
print(logo)


def caesar(direction, text, shift):
    arr = []
    index = 0
    string = []
    for item in text:
        arr.append(item)
    for i in arr:
        index = alphabet.index(i)
        if direction == 'encode':
            string.append(alphabet[index + shift])
            s = "".join(string)
        elif direction == 'decode':
            string.append(alphabet[index - shift])
            s = "".join(string)
    print(f"The {direction}d text is {s}")


choose = False
while not choose:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
    if shift > 26:
        shift = shift % 26
    caesar(direction, text, shift)
    typed = input("yes to restart no to exit : \n")
    if typed == 'no':
        choose = True
