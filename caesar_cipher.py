import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

exit_program=True

print(art.logo)

def encrypt(word,shift_num):
    i=0
    for char in word:
        text_char.append(char)
    for char in text_char:
        alphabet_index=alphabet.index(char)
        encrypted_shift_num=alphabet_index+shift_num 
    
        if encrypted_shift_num>=len(alphabet):
            text_char[i]=alphabet[encrypted_shift_num-len(alphabet)]
        else:
            text_char[i]=alphabet[encrypted_shift_num]
        i+=1    
        
        
    encrypted_text=''.join(text_char)    
    print(f"The encrypted text is {encrypted_text}")
    

def decrypt(word,shift_num):
    i=0
    for char in word:
        text_char.append(char)
    for char in text_char:
        alphabet_index=alphabet.index(char)
        encrypted_shift_num=alphabet_index-shift_num 
    
        if encrypted_shift_num<0:
            text_char[i]=alphabet[encrypted_shift_num+len(alphabet)]
        else:
            text_char[i]=alphabet[encrypted_shift_num]
        i+=1
        
    decrypted_text=''.join(text_char)    
    print(f"The decrypted text is {decrypted_text}")
  
    
while exit_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    text_char=[]
    
    if direction=='encode':
        encrypt(text,shift)
    elif direction=='decode':
        decrypt(text,shift)
    else:
        print("Please type either 'encode' or 'decode'")
    again=input("Type 'yes' to encrypt/decrypt again or 'no' to exit\n").lower()
    
    if again=='no':
        exit_program=False
    elif again=='yes':
        exit_program=True
    else:
        exit_program=False