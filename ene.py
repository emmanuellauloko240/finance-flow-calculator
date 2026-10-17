def allocate_resources(total_pool):
    development = total_pool * 0.80
    safety_allocation = total_pool - development

    return development,safety_allocation
profile = ['Dev-Heavy','Balanced','Safety']
    
while True:
    try:
        name = input("Enter your name: ")
        total_pool = float(input("Enter total resource pool (or type 'exit' to quit) ): "))
        if total_pool == "exit":
            print(f"Goodbye,{name}")
            break
        
        development, safety_allocation = allocate_resources(total_pool)
    
        print(f"Allocated to Development: {development}")
        print(f"safety_allocation: {safety_allocation}")
        print(f"Available Allocation Profile: {profile}")


    except ValueError:
        print("Hey! That was not a valid number. Please use  digits only")
