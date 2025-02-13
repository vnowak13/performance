# Makeup  calculator
# Author: Victoria Nowak
# Date: 02/07/2025
# Descripiton: This program gives you a list of make products and you select the ones you need.
#              It then calculates the total amount thr porducts cost.

def main():
    question = (input("Do you want to buy some new products? (yes/no): ")).lower()

    if question == "no":
        print("Okay, see you next time!")
        return  # Exit the function early, since break is not valid here
    elif question == "yes":
        print("Let's buy some products")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        return

makeup = {"masacara": 22.00,
          "blush": 15.00,
          "foundation": 30.00,
          "bronzer": 28.00,
          "concealer": 25.00,
          "eyeshadow": 29.00,
          "eyeliner": 20.00,
          "eyebrow gel": 19.00}

skincare = {"Primer": 28.00,
            "moisturizer": 17.21,
            "toner": 16.00,
            "cleannser": 10.50,
            "Sunscreen": 18.00,
            "serums": 14.92}

def makeup_store(makeup):

    cart = []
    total = 0
    while True:
        print("-----------------List----------------")
        for key, value in makeup.items():
            print(f"{key}: ${value:.2f}")
        print("-------------------------------------")

        products = input("Select the items you need (q to quit): ").lower()
        if products == "q":
            break
        elif makeup.get(products) is not None:
            cart.append(products)
    print("--------------Your Cart--------------")
    for products in cart:
        total += makeup.get(products)
        print(products, end=" ")
    print()
    print(f"Total is: ${total:.2f}")

#Call the main function
main()
#Get totals for makeup and skincare
makeup_total = makeup_store(makeup)
skincare_total = makeup_store(skincare)
#Add the totals together
total_amount = makeup_total + skincare_total
print(f"Total for all products: ${total_amount:.2f}")