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
                print("1.Add crew member: ")
                print("2.Remove crew member: ")
                print("3.Update rank: ")
                print("4.Display roster: ")
                print("5.Search crew member: ")
                print("6.Filter by division: ")
                print("7.Calculate payroll: ")
                print("8.Count officers: ")
                
                
            else:
                print("Invalid name.")
                display_menu()


        elif opt == "no":
            print("Shutting down...")
            
        else:
                print("Invalid input")
                display_menu()
        add_member()
        remove_member()

    def add_member():
        opt = input("Select option:")
        if opt == "1":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            new_id = input("Id: ")
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)  
            i.append(new_id)
            if id in (i):
                print("Invalid, ID already in use.")
                display_menu()
            else:    
                print("Crew member added.")
         
    def remove_member():
        opt = input("Select option:")
        if opt == "2":
            rem = input("ID to remove: ")
            if rem not in i:
                print("ID is not in database.")
            else:
             idx = i.index(rem)
             n.pop(idx)
             r.pop(idx)
             d.pop(idx)
             i.pop(idx)
             print("Crew member removed.")
        
            remove_member()  

    def update_rank():
        opt = input("Select option:")
        if opt == "3":
         
         
         update_rank()
    def display_roster():
        if opt == "4":
         display_roster()
    def search_crew_member():
        if opt == "5":
         search_crew_member()
    def filter_by_division():
        if opt == "6":
         filter_by_division()
    def calculate_payroll():
        if opt == "7":
         calculate_payroll()
    def calculate_officers():
        if opt == "8":
            calculate_officers()    

    display_menu()  
main()
#initial_database()
     
