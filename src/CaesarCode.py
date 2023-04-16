#Ceaser Encryption algorithm
def Encryption(plaintext,key_val):
    ciphertext = ''                 # empty string to store the encrypted message
    for i in range(len(plaintext)):
       character = plaintext[i]       # assigns each character to variable special
       if not character.isalpha():    # isalpha() ->Funksioni i gatshem nese te gjitha karakteret jan a-z kthen true 
            ciphertext += character
            continue 
       new_character = character.lower()
       ciphertext += chr((ord(new_character) + key_val - 97) % 26 +97).upper() if character.isupper() else chr((ord(new_character) + key_val - 97) % 26 + 97)
                                        # P = ( P + K ) % 26  
    return ciphertext


#Decryption of a ciphertext
def Decryption(ciphertext, key_val):
    plaintext = '' 
    for i in range(len(ciphertext)): #iterates through each character in the ciphertext string
        character = ciphertext[i]
        if not character.isalpha(): #checks if special is not an alphabet character
            plaintext += character 
            continue
        new_character = character.lower() #converts special to lowercase 
        plaintext += chr((ord(new_character) - key_val - 97) % 26 + 97).upper() if character.isupper() else chr((ord(new_character) - key_val - 97) % 26 + 97) 
        #Calculates the new character's ASCII value using formula C = (C - K) % 26
        #If original character was uppercase the decrypted character is converted to uppercase

    return plaintext

while True:  #starts the infinite loop that continues until the user chooses to exit the program
    print(
        'Welcome \n [] Press 0 for Encryption \n [] Press 1 for Decryption \n [*] Press 2 to exit.. ') 
    print('Encryption/Decryption with shift value of your choice ! ')                              
    choice = input('Insert Here : ')                                                   
    if choice.isdigit():                                                               
        if choice == '0':
            plainTxt = input('Insert the plaintext : ')                                 
            key = int(input('Insert shift value(Only integer values) : '))         
                                                                                   #The input is converted to an integer and stored in the key variable.
            print(50 * '-')                                                        
            print(f'Your ciphertext ---> {Encryption(plainTxt, key)}') #calls the Encryption function with the sen plaintext and key shift value,and prints the resulting ciphertext.
            print(50 * '-')                                       
            con = input('Continue ? [Any Key/no]')                
            if con == 'no':
                print('Exiting..')                                
                break 
            else:
                pass
        elif choice == '1': 
            cipherTxt = input('Insert the ciphertext : ') 
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your plaintext ---> {Decryption(cipherTxt, key)}') #Calling the function for decryption
            print(50 * '-')
            con = input('Would you like to continue ? [Any Key/no]') #Continue or exit 
            if con == 'no':
                print('Exiting..')
                break
            else:
                pass
        elif choice == '2':  #Exiting without encrypting or decrypting
            print('Exiting..')
            break
        else:
            print('Exception error .. \n'
                  'Please insert 0, 1 or 2') #A nonvalid choice
          
