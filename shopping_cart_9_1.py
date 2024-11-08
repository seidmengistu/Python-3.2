#Based on collections building shopping cart

foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food to buy (q for quit): ")
    if food.lower()=='q':
        break
    
    else:
        price=float(input(f"Enter a price of a{food}:$"))
        foods.append(food)
        prices.append(price)

print ("-------YOUR CART IS-----")

for food in foods:
    print(food,end=" ")

for prices in prices:
    total=total+prices

print(f"\nTotal Price: ${total}")