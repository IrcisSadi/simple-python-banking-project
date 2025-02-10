from script1 import *

def favorite_drink(drink):
    print(f"your favorite drink is {drink}")

def main():

    print("this is script 2")
    favorite_food("sushi")
    favorite_drink("coffe")
    print("goodbye")

if __name__ == '__main__':
    main()
