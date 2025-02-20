# Makeup  calculator
# Descripiton: This program gives you a list of make products and you select the ones you need.
#              It then calculates the total amount thr porducts cost.


#the main function of the code and what begins the program
def main():
    #Encourage the user for input and convert the response to lowercase letters
    question = (input("Do you want to buy some new products? (yes/no): ")).lower()
    #Check if the user ansers no and if so, exit the function early
    if question == "no":
        print("Okay, see you next time!")
        return  # This allows the function to end early
    elif question == "yes":
        print("Let's buy some products")
    else:
        #This handles invalid input that the user types
        print("Invalid input. Please type 'yes' or 'no'.")
        return
#Two list/dictonary for makeup products and their prices
makeup = {"masacara": 22.00,
          "blush": 15.00,
          "foundation": 30.00,
          "bronzer": 28.00,
          "concealer": 25.00,
          "eyeshadow": 29.00,
          "eyeliner": 20.00,
          "eyebrow gel": 19.00}
#Defining the dictionary for skincare products and theur prices
skincare = {"Primer": 28.00,
            "moisturizer": 17.21,
            "toner": 16.00,
            "cleanser": 10.50,
            "Sunscreen": 18.00,
            "serums": 14.92}
#The function to start that shopping at a makeup store
def makeup_store(makeup):

    cart = [] #empty list to store selected products
    total = 0 #The total cost to 0

    #Print the list of the avaiable products and prices
    print("-----------------List----------------")
    for key, value in makeup.items(): #the interation 
        print(f"{key}: ${value:.2f}")
    print("-------------------------------------")
    
    while True: #a while loop that allows the user to select products until they quit
        products = input("Select the items you need (q to quit): ").lower()
        if products == "q":
            break #Exit the loop if the usqer types "q"
        #checks if the products exists in the dictionary
        elif makeup.get(products) is not None:
            cart.append(products) #Adds product to the cart
    print("--------------Your Cart--------------")
    for products in cart:
        total += makeup.get(products) #adds the price of the selected product
        print(products, end=" ") #prints the name of the product
    print() #prints a new line after the list of products in the cart
    print(f"Total is: ${total:.2f}") #total cost of the selected items

#Call the main function
main()
#call the function for both makeup and skincar lists
makeup_store(makeup)
makeup_store(skincare)