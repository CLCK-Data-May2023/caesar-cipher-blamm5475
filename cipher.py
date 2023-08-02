try:
    #input from user
    plain_text = input("Enter a plain text sentence: ")
    #shift variable that can be changed
    shift = 5

    #Create object for encrypted text
    encrypted_text = ""
    #parse throught user text 
    #find ascii value and add 5 to return encrypted value
    for char in plain_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    #print encrypted value
    print("Encrypted text:", encrypted_text)
except Exception as e:
    print("An error occurred:", e)