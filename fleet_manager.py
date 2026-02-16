#def initial_database():
n = ["Beverly Crusher", "Deanna Troi", "Jean-Luc Picard", "Geordi La Forge", "Data"]
r = ["Commander", "Lieutenant", "Captain", "Lieutenant", "Lieutenant"]
d = ["Sciences", "Sciences", "Command", "Operations", "Operations"]
i = ["BC87", "DT87", "JP87", "GF87", "LD87"]
print("--Booting database menu--")
print("--Syncing data--")

def main():
    opt = input("Would you like to view display menu? ").strip()
    if opt == "yes": 
        print("What is your full name? ")
        name = input("Input: ").strip()
        if name in (n):
            print("Welcome: " + name + " you are currently logged in.")
        else:
            print("Invalid name.")
            main()
    elif opt == "no":
                print("Shutting down...")
                return
    else:
        print("Invalid input")
        main()

    def display_menu():
        
            print("--Menu--")
            print("1.Add crew member: ")
            print("2.Remove crew member: ")
            print("3.Update rank: ")
            print("4.Display roster: ")
            print("5.Search crew member: ")
            print("6.Filter by division: ")
            print("7.Calculate payroll: ")
            print("8.Count officers: ")
            print("9.Shutdown: ")
                
            opt = input("Selection: ")
            if opt == "1":
                add_member()
            if opt == "2":
                remove_member()
            if opt == "3":
                update_rank()
            if opt == "4":
                display_roster()
            if opt == "5":
                search_crew_member()
            if opt == "6":
                filter_by_division()
            if opt == "7":
                calculate_payroll()
            if opt == "8":
                calculate_officers()
            if opt == "9":
                shutdown()
            else:
                print("Invalid input")
            display_menu()

    def add_member():
        print("Input to add crew member:")
        new_name = input("Name: ")
        new_rank = input("Rank: ")
        new_div = input("Division: ")
        new_id = input("Id: ")
        if new_id in (i):
            print("Invalid, ID already in use.")
            add_member()
        else:  
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)  
            i.append(new_id)
            print("Crew member added.")
            display_menu()
    def remove_member():
        
        rem = input("ID to remove: ")
        if rem not in i:
            print("ID is not in database.")
            remove_member()
        else:
            idx = i.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            i.pop(idx)
            print("Crew member removed.")
            display_menu()
             

    def update_rank():
        
        updt = input("Input crew ID to update: ")
        if updt in i:
            i.index(updt) 
            crnk = input("What is the new rank? ")
            r[i.index(updt)] = crnk
            print("Rank updated.")
            for x in range(len(n)): 
                print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x])  
                display_menu()                        #insert rank at list number i want to change
        else:
            print("Invalid ID.") 
            update_rank()                                #then remove said list number by pop but of + 1

            
    def display_roster():
        for x in range(len(n)): 
                    print(n[x] + " - " + r[x] + " - " + d[x] + " - " + i[x]) 
        display_menu()
        
    def search_crew_member():
        
        term = input("Please enter a search term: ")
        searchlist = []
        for x in n:
            if term in x:
                searchlist.append(x)
        print(searchlist)
        if x not in n:
            print("Invalid input.")
            display_menu()
        
        display_menu()

    def filter_by_division():
        if opt == "6":
         filter_by_division()
    def calculate_payroll():
        if opt == "7":
         calculate_payroll()
    def calculate_officers():
        if opt == "8":
            calculate_officers()
    def shutdown():
        print("Shutting down...")
        exit()
            
                

    display_menu()  
main()
#initial_database()
     
