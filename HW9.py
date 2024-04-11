def encode(s):
    #Takes string s
    t = ""
    for i in range(0, len(s)):
        x = int(s[i])
        x = (x + 3) % 10
        t += str(x)
    return t

def decode(s):
    # Takes string s
    t = ""
    for i in range(0, len(s)):
        x = int(s[i])
        #using -3 = 7 mod 10
        x = (x + 7) % 10
        t += str(x)
    return t

def main():
    stored = ""
    while(True):
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = str(input("Please enter an option: "))
        if(option == "1"):
            x = str(input("Please enter your password to encode: "))
            stored = encode(x)
            print("Your password has been encoded and stored!")
        elif(option == "2"):
            print(f"The encoded password is {stored}, and the original password is {decode(stored)}.")
        elif(option == "3"):
            break

main()

