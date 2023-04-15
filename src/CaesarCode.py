#Krijimi i enkriptimit per Cesar algoritem
def Encryption(plaintext,key_val):
    ciphertext = '' # empty string to store the encrypted message
    for i in range(len(plaintext)):
       special = plaintext[i]  # assigns each character to variable special
       if not special.isalpha():  # isalpha() ->Funksioni i gatshem nese te gjitha karakteret jan a-z kthen true 
            ciphertext += special
            continue 
       new_special = special.lower()
       ciphertext += chr((ord(new_special) + key_val - 97) % 26 +97).upper() if special.isupper() else chr((ord(new_special) + key_val - 97) % 26 + 97)
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

 while True:  #starts the infinite loop that continues until the user chooses to exit the program
    print(
        'Welcome \n [] Press 0 for Encryption \n [] Press 1 for Decryption \n [*] Press 2 to exit.. ') #displays a welcome message and the menu with three options
    print('Encryption/Decryption with shift value of your choice ! ')                               #displays a message to guide the user on how to use the program.
    choice = input('Insert Here : ')                                                   #prompts the user to enter their choice and stores it in the choice variable.
    if choice.isdigit():                                                               #checks if the user input is a digit.
        if choice == '0':
            sen = input('Insert the plaintext : ')                                 #prompts the user to enter the plaintext that they want to encrypt.
            key = int(input('Insert shift value(Only integer values) : '))         #prompts the user to enter the shift value they want to use for the encryption.
                                                                                   #The input is converted to an integer and stored in the key variable.
            print(50 * '-')                                                        #prints a line of 50 dashes(-) to separate the output for better readability.
            print(f'Your ciphertext ---> {Encryption(sen, key)}') #calls the Encryption function with the sen plaintext and key shift value,and prints the resulting ciphertext.
            print(50 * '-')                                       #prints another line of 50 dashes to separate the output.
            con = input('Continue ? [Any Key/no]')                #prompts the user to continue or exit the program.
            if con == 'no':
                print('Exiting..')                                #prints a message to indicate that the program is exiting.
                break #breaks out of the infinite loop and ends the program. If the user chose to continue, the loop continues to display the menu and prompt the user for their choice.
            else:
                pass
        elif choice == '1': 
            csen = input('Insert the ciphertext : ') 
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your plaintext ---> {Decryption(csen, key)}') #Calling the function for decryption
            print(50 * '-')
            con = input('Shall we continue ? [Any Key/no]') #Continue or exit 
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
                  'Please insert 2 to exit ') #A nonvalid choice
          
