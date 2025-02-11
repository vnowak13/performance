# Makeup  calculator
# Author: Victoria Nowak
# Date: 02/07/2025
# Descripiton: This program gives you a list of make products and you select the ones you need.
#              It then calculates the total amount thr porducts cost.


print("Welcome to you makeup cart!!")
print("Let's buy some makeup/skincare!!!")

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

    print("-----------------List----------------")
    for key, value in makeup.items():
        print(f"{key}: ${value:.2f}")
    print("-------------------------------------")

    while True:
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

makeup_store(makeup)
makeup_store(skincare)