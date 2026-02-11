n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        loading = loading + 1    #added this line of code so code would load
        print("Loading module " + str(loading))
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #added second equals to make it compare
            print("Current Crew List:")
            
            for i in range(len(n)): #sets range as length of list, add more to list and it should make new length
                print(n[i] + " - " + r[i]) 

                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank) #added this so both name and rank would be added to their respective lists
            d.append(new_div) #for my 9th bug I realised I was missing this append
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
            if rem not in n:
                print("Provided name is not in database")
            else:
                if n.count(rem) > 1:
                    remr = input("Rank of person to remove: ")
                    for x in range(len(n)):     #all this allows for removing a person with the same name 
                        if n[x] == rem:         #as someone but differentiates by rank
                            Current_rank = r[x]
                            if Current_rank == remr:
                                n.pop(x)
                                r.pop(x)
                                d.pop(x)
                                print("Removed.")
                                break

                else:
                    idxn = n.index(rem)
                    n.pop(idxn)        # this focuses on removing an individual if their name isn't a duplicate
                    r.pop(idxn)
                    d.pop(idxn)       
                    print("Removed.")
                    
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain": 
                    count = count + 1
                if rank ==  "Commander": #made this if statement to seperately count for both captain and commander as high ranking
                    count = count + 1    #this is because it was shwoing every crew member as high ranking
                   
            print("High ranking officers: " + str(count)) #added this in and forgot to commit it, commit 6
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith() #fixed syntax error
