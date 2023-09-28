alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# NOTE - I used an if statement below to sort of "shift back to the beginning" if we reached the end of the
#  list.  The instructor did it much simpler - she simply had the list repeat itself, that way any index could
#  be shift by a reasonable amount.  See ex4...
#  Either way, this isn't about building the perfect cypher, it's about functions and list indexes.
def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if (position + shift_amount) > 25:
            letter = alphabet[position - 26 + shift_amount]
        else:
            letter = alphabet[position + shift_amount]
        cypher_text += letter
    print(f"The encoded text is {cypher_text}")


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)