
n = ["Beverly Crusher", "Deanna Troi", "Jean-Luc Picard", "Geordi La Forge", "Data"]
r = ["Commander", "Lieutenant", "Captain", "Lieutenant", "Lieutenant"]
d = ["Sciences", "Sciences", "Command", "Operations", "Operations"]
i = ["BC87", "DT87", "JP87", "GF87", "LD87"]

def fleet_manager():
    print("--Booting database menu--")
    def initial_database():
        opt = input("Would you like to view current database? ")
        if opt == "yes":
            for x in range(len(n)):
                print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x]) 
        elif opt == "no":
            print("...")
        else:
            print("Invalid input")
            initial_database()

    initial_database()

    def display_menu():
        opt = input("Would you like to view display menu? ")
        if opt == "yes": 
            print("What is your full name? ")
            print("Here are the current options: ")
            print(n)  
            name = input("Input selection: ")

        elif opt == "no":
            print("...")
        else:
                print("Invalid input")
                display_menu()
        
    display_menu()

        
fleet_manager()
     
