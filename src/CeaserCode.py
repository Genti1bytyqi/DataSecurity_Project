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
