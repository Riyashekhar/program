import re
phone_regex="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
phone_num=input("enter your contact number\n")
valid=re.search(phone_regex,phone_num)
if valid:
    print("the given contact number is valid")
else:
    print("the given contact number is not valid")
