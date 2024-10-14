#Alan Armstrong
#Prog 108
#Programming Project 1: Chatbot
#4/21/23

#requirements

#     Use the print() function to output a variety of data
#     Use the input() function to ask for multiple data types
#     Use an if statement for handling program decisions
#     Use basic arithmetic operations in a program
#     Use string methods and operations 
#     Debug, test, and use best practices

# Scenario

# create customer service AI chatbot

import sys 
from termcolor import colored, cprint

print("Greetings valued customer, I am Cathy, your friendly chatbot.\n\n")

ipsum = colored("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n", "blue")
print(ipsum)

#global lists

tax = .1
total = 0
newTotal = 0
cart = []
productList = ['Sprocket', 'Cog', 'Widget'] 
priceList = [5, 10, 15]

#create a user account

class newCustomer:

  def __init__(self, firstName, lastName, email, phone):
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.phone = phone

  @classmethod
  def from_input(cls):
    return cls(
      input("Firstname: "),
      input("Lastname: "),
      input("email: "),
      int(input("Phone: ")),
    )

# def customerMenu(): --------------- abandoned this idea -----------------
#   print("Customer Input")
#   print("Show - show items in cart")
#   print("Add - add item to cart")
#   print("Rem - remove item from cart")
#   print("Quit - quit the chat session")
#   print()
# shopping cart
# def cart(customerCart):
#   if len(customerCart) == 0:
#     print("you have no items in your cart.\n")
#   else:
#     for i, item in enumerate(customerCart, start=1):
#       print(f"{i}. {productList[0]} ({priceList[0]})")
#     print()


# Customer service chatbot program. Introduce products and prices to customer
  
askHelp = input("Would you like some help? ")
if askHelp.lower() == "yes" or askHelp.lower() == "y":
  print("Which product interests you?\n ")
  for item, price in zip(productList, priceList):
    print(f"{item} ${price} each")
    print()
else: 
    print("Have a nice day.  Goodbye.")
    exit()

customerShopping = False

#asks customer if they want to start an order, and if so creates a profile for the customer and a shopping cart.

askOrder = input("Would you like to place an order? ")
if askOrder.lower() == "yes" or askOrder.lower() == "y":
  print("Great, let's get started. First I will need your name and contact info")
  newCustomer = newCustomer.from_input()
  print(f"Let me make sure I have that right. It's {newCustomer.firstName} {newCustomer.lastName} and your email is {newCustomer.email}, and phone is {newCustomer.phone}")
  customerShopping = True
  while customerShopping == True:
    print(f"what would you like to add? {productList}")
    item = input()
    if item == "Sprocket": #increment prices in customer order
      total += 5
    if item == "Cog":
      total += 10
    if item == "Widget":
      total += 15
    if item in productList: #product verification
      cart.append(item)
      print(cart)
      doneShopping = input("are you done shopping?")
      if doneShopping.lower() == "yes" or doneShopping.lower() == "y":
        print(cart)
        customerShopping = False
        newTotal = total * tax + total
    else:
      print("sorry, we don't carry that.")
      print(cart)
  else:
    print(f"you have ordered these items: {cart}")
    print(f"Your total is: ${newTotal}. We will send your receipt to {newCustomer.email}. Thank you for your business. Have a good day.")
    exit()
else:
  print("I'm sorry I couldn't help you today, Goodbye")


