print("This is the Address Creator. Enter in your information to get you address formatted correctly.")
print()
name = input("Name: ")
add1 = input("Address Line 1: ")
add2 = input("Address Line 2: ")
city = input("City: ")
state = input("State: ")
zip = input("Zip Code: ")
print()

def checkadd(add1, add2):
    if len(add1) > 50:
        print("Address Line 1 Too Long")
    else:
        print(add1)
    if add2 != "":
        print(add2)

def checkcity(city):
    if len(city) > 50:
        return print("City Too Long")
    else:
        return city

def checkstate(state):
    if len(state) > 12:
        return print("State too Long")
    else:
        return state

def checkzip(zip):
    if len(zip) > 5:
        return str("Invalid Zip Code")
    else:
        return zip

def creator(name, add1, add2, city, state, zip):
    print(name)
    checkadd(add1, add2) 
    print("{}, {} {}".format(checkcity(city), checkstate(state), checkzip(zip)))

creator(name, add1, add2, city, state, zip)
