import datetime
from datetime import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]

cart = []

while True:
    itemnumber = input("Please enter an item number, or 'DONE' if complete:")
    if itemnumber == "DONE":
        print("Thanks!  You are learning... sort of.")
        break
    elif (int(itemnumber) <= 20) & (int(itemnumber) >= 1):
        cart.append(int(itemnumber))
        print("the itemnumber is: " + str(itemnumber))
    else:
        print("Please verify item")

# CHECKPOINT II WORK

charges = []
print("-----------------------------")
print("BIG TOP GROCERY")

print("-----------------------------")
print("www.bigtopgrocery.com")
print("phone: 555-212-3434")

today = datetime.now()
currentdate = str(today.year) +"-"+ str(today.month) +"-"+ str(today.day)
currenthour  = today.hour
currentminute = today.minute
currentsecond = today.second

print("CHECKOUT TIME:", str(currentdate), str(currenthour) + ":" + str(currentminute)
+ ":" + str(currentsecond))

print("-----------------------------")
print("SHOPPING CART ITEMS:")
for item in products:
    for purchase in cart:
        if item["id"] == purchase:
            charges.append(item["price"])
            print (" + ",item["name"], '(${0:.2f})'.format(item["price"]))

print("-----------------------------")
salestax = 0.08875
subtotal = sum(charges)
taxcharge = (salestax * subtotal)
total = (subtotal + taxcharge)
print("Subtotal:"'${0:.2f}'.format(sum(charges)))
print("Plus NYC Sales Tax (8.875%):", '(${0:.2f})'.format(taxcharge))
print("Total:", '(${0:.2f})'.format(total))

print("-----------------------------")
print("Thank you for your business!  See you again soon.")
