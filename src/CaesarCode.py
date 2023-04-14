#Krijimi i enkriptimit per Cesar algoritem
def Encryption(plaintext,key_val):

    ciphertext = ''
    
    for i in range(len(plaintext)):
       special = plaintext[i]  #special -> karakteret speciale
       new_special = special.lower() #new_special -> shkronjat evogla
        
       if new_special == " ":
            ciphertext += ' '
    # isalpha() ->Funksioni i gatshem nese te gjitha karakteret jan a-z kthen true 
       elif special.isalpha():  
            ciphertext += chr((ord(new_special) + key_val-97)%26 +97)
                                        #(P+K)%26  
    return ciphertext


#Decrypting Ciphertext
def Decryption(ciphertext, key_val):
    plaintext = '' #initializes an empty string which will hold the decrypted message
    for i in range(len(ciphertext)): #iterates through each character in the ciphertext string
        special = ciphertext[i]
        if not special.isalpha(): #checks if special is not an alphabet character
            plaintext += special 
            continue
        new_special = special.lower() #converts special to lowercase 
        plaintext += chr((ord(new_special) - key_val - 97) % 26 + 97).upper() if special.isupper() else chr((ord(new_special) - key_val - 97) % 26 + 97) 
        #calculates the new character's ASCII value 

    return plaintext
