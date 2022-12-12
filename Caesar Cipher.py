

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Encrypt(message,index):
    encrypted_message = ""
    shifted = GetShiftedAlphabet(index)
    print(shifted)
    for c in message:
        if c.isalpha():
            if c.isupper():
                ind = alphabet.index(c)
                char = shifted[ind]
            else:
                ind = alphabet.index(c.upper())
                char = shifted[ind].lower()
            encrypted_message += char
        else:
            encrypted_message += c
    return encrypted_message

def GetShiftedAlphabet(index):
    shifted_alphabet = alphabet[index:] + alphabet[:index]
    return shifted_alphabet

def Decrypt(message,index):
    decrypted_message = ""
    shifted = GetShiftedAlphabet(index)
    for c in message:
        if c.isalpha():
            if c.isupper():
                ind = shifted.index(c)
                char = alphabet[ind]
            else:
                ind = shifted.index(c.upper())
                char = alphabet[ind].lower()
            decrypted_message += char
        else:
            decrypted_message += c
    return decrypted_message

key = 2
em = Encrypt("This is a really long, complicated message. \n I wonder if this will work.",key)
print(em)

dm = Decrypt(em,key)
print(dm)
