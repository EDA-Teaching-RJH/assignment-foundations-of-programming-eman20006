#def initial_database():
n = ["Beverly Crusher", "Deanna Troi", "Jean-Luc Picard", "Geordi La Forge", "Data"]
r = ["Commander", "Lieutenant", "Captain", "Lieutenant", "Lieutenant"]
d = ["Sciences", "Sciences", "Command", "Operations", "Operations"]
i = ["BC87", "DT87", "JP87", "GF87", "LD87"]
print("--Booting database menu--")
print("--Syncing data--")

def main():

    def display_menu():
        opt = input("Would you like to view display menu? ")
        if opt == "yes": 
            print("What is your full name? ")
            name = input("Input: ")
            if name in (n):
                print("Welcome: " + name + "you are currently logged in.")
                print("What would you like to do: ")
                1 = input("Add crew member: ")
                2 = input("Remove crew member: ")
                3 = input("Update rank: ")
                4 = input("Display roster: ")
                5 = input("Search crew member: ")
                6 = input("Filter by division: ")
                7 = input("Calculate payroll: ")
                8 = input("Count officers: ")
            
            else:
                print("Invalid name.")
                display_menu()


        elif opt == "no":
            print("Shutting down...")
            
        else:
                print("Invalid input")
                display_menu()
    display_menu()

    def add_member():
        new_name = input("Name: ")
        new_rank = input("Rank: ")
        new_div = input("Division: ")
        new_id = input("Id: ")
        n.append(new_name)
        r.append(new_rank)
        d.append(new_div)  
        i.append(new_id)
        if id in (i):
             print("Invalid, Id already in use.")
             display_menu()
             
        print("Crew member added.")
         
    def remove_member():
         
    def update_rank():
         
    def display_roster():
         
    def search_crew_member():
         
    def filter_by_division():
         
    def calculate_payroll():
         
    def calculate_officers():
         
        

main()
#initial_database()
     
