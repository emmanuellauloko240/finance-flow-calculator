def allocate_resources(total_pool):
    development = total_pool * 0.80
    safety_allocation = total_pool - development

    return development,safety_allocation

    

while True:
    try:
        name = input("Enter your name: ")
        total_pool = input("Enter total resource pool (or type 'exit' to quit) ): ")
        if total_pool == "exit":
            print(f"Goodbye,{name}")
            break
        
        development, safety_allocation = (total_pool )
    
        print(f"Allocated to Development: {development}")
        print(f"safety_allocation: {safety_allocation}")
        again = input("Do you want to continue? (yes/no) ")
        if again != "yes" or "y":
            break

    except ValueError:
        print("Hey! That was not a valid number. Please use  digits only")
