def allocate_resources(total_pool,chosen_profile):
    if chosen_profile == 'Dev-Heavy':
        development = total_pool * 0.90
    elif chosen_profile == 'Balanced':
        development = total_pool * 0.50
    elif chosen_profile == 'Safety':
        development = total_pool * 0.20
    else:
        development = total_pool * 0.80
    
    development = total_pool * 0.80
    safety_allocation = total_pool - development

    return development,safety_allocation
profile = ['Dev-Heavy','Balanced','Safety']


while True:
    try:
        name = input("Enter your name: ")
        for profiles in profile:
            print(f"{profiles}")

        chosen_profile = input("Choose a profile from the list above: ")


        total_pool = float(input("Enter total resource pool (or type 'exit' to quit) ): "))
        if total_pool == "exit":
            print(f"Goodbye,{name}")
            break
        total_pool = int(total_pool)
        development, safety_allocation = allocate_resources(total_pool,chosen_profile)
    
        print(f"Allocated to Development: {development}")
        print(f"safety_allocation: {safety_allocation}")


    except ValueError:
        print("Hey! That was not a valid number. Please use  digits only")
