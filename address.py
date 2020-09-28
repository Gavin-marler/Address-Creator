print("This is the Address Creator. Enter in your information to get you address formatted correctly.")
print()
name = input("Name: ")
add1 = input("Address Line 1: ")
add2 = input("Address Line 2: ")
city = input("City: ")
state = input("State: ")
zip = input("Zip Code: ")
print()
def creator(name, add1, add2, city, state, zip):
    print(name) 
    print(add1)
    if add2 != "":
        print(add2)
    print("{}, {} {}".format(city, state, zip))

creator(name, add1, add2, city, state, zip)
