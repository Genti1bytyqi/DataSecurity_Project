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


#Decryption of a ciphertext
def Decryption(ciphertext, key_val):
    plaintext = '' #initializes an empty string which will hold the decrypted message
    for i in range(len(ciphertext)): #iterates through each character in the ciphertext string
        special = ciphertext[i]
        if not special.isalpha(): #checks if special is not an alphabet character
            plaintext += special 
            continue
        new_special = special.lower() #converts special to lowercase 
        plaintext += chr((ord(new_special) - key_val - 97) % 26 + 97).upper() if special.isupper() else chr((ord(new_special) - key_val - 97) % 26 + 97) 
        #Calculates the new character's ASCII value using formula C = (P + K) % 26
        #If original character was uppercase the decrypted character is converted to uppercase

    return plaintext

 while True:
    print(
        'Welcome \n [] Press 0 for Encryption \n [] Press 1 for Decryption \n [*] Press 2 to exit.. ')
    print('Encryption/Decryption with shift value of your choice ! ')
    choice = input('Insert Here : ')
    if choice.isdigit():
        if choice == '0':
            sen = input('Insert the plaintext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your ciphertext ---> {Encryption(sen, key)}')
            print(50 * '-')
            con = input('Continue ? [Any Key/no]')
            if con == 'no':
                print('Exiting..')
                break
            else:
                pass
