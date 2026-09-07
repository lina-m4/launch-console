print("Welcome to the Launch Console!")

name = input("What's your name? ")
print(f'Hi, {name}!')

menu = ["1) About me", "2) My goals", "3) Favorite product", "4) Exit"]

def about_me(name, grade, state):
    return f"My name is {name}, I'm a {grade}, and I live in {state}!"

def favorite_product(product):
    return f"I'm interested in building {product} this term!"

running = True
while running:
    print(menu)
    choice = input("Pick 1, 2, 3, or 4: ")
    
    if choice == "1":
        print(about_me(name, 'junior', 'Virgina'))
    elif choice == "2":
        print("My goals are to do well during Elite 101, \nmake the varsity basketball team, \nand to finish the semester with all A's!")
    elif choice == "3":
        print(favorite_product('BudgetBuddy'))
    elif choice == "4":
        running = False
        print("Goodbye!")





