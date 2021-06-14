
def main():
    keys = []                                       #list to store text from gen_key.txt
    with open("gen_key.txt", 'r') as file:
        for line in file:
            for a in line.split():                  #split text by space
                keys.append(a)                      #add text to keys list
    n = int(keys[2])                                #declare n
    e = int(keys[4])                                #declare e
    encrypted_mess = open("encrypted_Text.txt", 'w')     #create encrypted_Text.txt
    with open("plain_Text.txt") as newFile:
        for word in newFile:
            for char in word:
                print(encryption(ord(char),e,n),file=encrypted_mess)    
    print(n, file=encrypted_mess)
    print(keys[4], file=encrypted_mess)

#encyrption funciton. m^e % n
def encryption(m,e,n):
    x = pow(m,e,n)
    return x

main()