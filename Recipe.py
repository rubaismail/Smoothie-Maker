# Ruba Ismail
# Mar 24 2024


# function that takes in ingredients and adds them into the list, also doubles as the update_list function.
def load_list(items):

    bananas = float(input("How many bananas do you have?\n"))
    items[0] = bananas

    strawberries = float(input("How many strawberries do you have?\n"))
    items[1] = strawberries

    blueberries = float(input("How many blueberries do you have?\n"))
    items[2] = blueberries

    spinach = float(input("How many cups of spinach do you have?\n"))
    items[3] = spinach

    avocados = float(input("How many avocadoes do you have?\n"))
    items[4] = avocados


# menu function to print out the options.
def menu():

    print("What would you like to do?")
    print("1 - View Ingredients")
    print("2 - Update Ingredients")
    print("3 - Make a smoothie")
    print("4 - Quit")
    
    option = int(input("What number do you choose?\n"))
    
    return option

# function that just prints the current values in the list to view them.
def view_ingredients(items):

    print("Bananas:",items[0])
    print("Strawberrries:",items[1])
    print("Blueberries:",items[2])
    print("Spinach:",items[3],"cups")
    print("Avocados:",items[4])
   

    
    
def make_smoothie(items):

    use_bananas = input("Will you use bananas?\n")
    use_strawberries = input("Will you use strawberries?\n")
    use_blueberries = input("Will you use blueberries?\n")
    use_spinach = input("Will you use spinach?\n")
    use_avocados = input("Will you use avocados?\n")

    # if statements to make sure we have enough of the ingredients required to make a smoothie.
    if (use_bananas == "yes"):
        if (items[0] < 1):
            print("Sorry, this recipe cannot be completed. You do not have enough bananas.")
            return

    if (use_strawberries == "yes"):
        if (items[1] < 5):
            print("Sorry, this recipe cannot be completed. You do not have enough strawberries.")
            return

    if (use_blueberries == "yes"):
        if (items[2] < 12):
            print("Sorry, this recipe cannot be completed. You do not have enough blueberries.")
            return

    if (use_spinach == "yes"):
        if (items[3] < 1):
            print("Sorry, this recipe cannot be completed. You do not have enough spinach.")
            return
        
    if (use_avocados == "yes"):
        if (items[4] < 0.5):
            print("Sorry, this recipe cannot be completed. You do not have enough avocados.")
            return

    # if statements that subtract the ingredients we use from the list.
    if (use_bananas == "yes"):

        items[0] -= 1
        
    if (use_strawberries == "yes"):

        items[1] -= 5

    if (use_blueberries == "yes"):

        items[2] -= 15

    if (use_spinach == "yes"):

        items[3] -= 1

    if (use_avocados == "yes"):

        items[4] -= 0.5


    drink_score = 0
    health_score = 0

    # drink and health scores based on the use of spinach and avocados.
    if (use_spinach=="yes" and use_avocados=="yes"):

        drink_score = 0
        health_score = 2
        

    elif (use_spinach=="yes" or use_avocados=="yes"):

        drink_score = 1
        health_score = 1

    else:

        health_score = 0
        drink_score = 1
        

    if (drink_score == 1):
        print("Your recipe scored a Drink Score of 1. It will be delicious!")
    else:
        print("Your recipe scored a Drink Score of 0. Yuck!")


    if (health_score == 2): 
        print("Your recipe scored a Health Score of 2. It will be super healthy!")
    
    elif (health_score == 1):
        print("Your recipe scored a Health Score of 1. It is good to go!")

    else:
        print("Your recipe scored a Health Score of 0. It probably tases good though.")
        
      

def main():
    
    print("Welcome to our Smoothie Recipe Analyzer!")
    
    items = [0, 0, 0, 0,  0]

    load_list(items)
    
    choice = menu()

    # calling each function based on the choice from the menu. 
    while (choice != 4):
        if (choice == 1):
            view_ingredients(items)
        elif (choice == 2):
            load_list(items)
        elif (choice == 3):
            make_smoothie(items)
            
        choice = menu()
            
main()   
    
