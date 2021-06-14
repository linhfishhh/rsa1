from __future__ import print_function

def main():

    keys = []  # list to store text from gen_key.txt
    with open("gen_key.txt", 'r') as file:
        for line in file:
            for a in line.split():  # split text by space
                keys.append(a)  # add text to keys list
    keysLength = len(keys)
    d = keys[10]

    nums = []
    with open("encrypted_Text.txt", 'r') as file:
        for line in file:
            nums.append(int(line))
    l = len(nums)
    n = nums[l-2]
    e = nums[l-1]

    i = 0
    decrypted_Mess = open("decrypt_Text.txt", 'w')
    while i < l -2:
        x = decrypt(nums[i], int(d), int(n))
        y = chr(x)
        print(y, end="", file=decrypted_Mess)
        i+=1


def decrypt(c,d,n):
    x = pow(c,d,n)
    return x


main()