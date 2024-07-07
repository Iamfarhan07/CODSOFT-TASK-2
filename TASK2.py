import random
import string

def your_password(length):
    

    characters=string.ascii_letters+string.digits+string.ascii_lowercase+string.octdigits 

    pw=''.join(random.choice(characters)for i in range(length))
    return pw
length=int(input("enter lenght of password="))
if length<=7:
    print("lenght of the password must be 8")
else:
    print("generated password is:=",your_password(length))

