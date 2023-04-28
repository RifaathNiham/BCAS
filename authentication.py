def signin(username,password):
    myfile = open("key.txt", "r")
    name = myfile.readline().strip()
    pswd = myfile.readline().strip()
    myfile.close()

    if(username == name and password == pswd):
        return True
    else:
        return False

name = input("ENTER YOUR USERNAME:-")
pswd = input("ENTER YOUR PASSWORD:-")

if (signin(name,pswd) == True):
    print
else:
    if not (signin(name, pswd) == True):
        print("INCORRECT YOUR USERNAME/PASSWORD!")
        exit()



