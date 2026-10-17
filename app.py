while True:

    try:
        name = input("Enter your name: ")
        total_pool = input("Enter total resource pool (or type 'exit' to quit) ): ")
        if total_pool == "exit":
            print(f"Goodbye,{name}")
            break
        total_pool = int(input("Enter a number: "))

        development = total_pool * 0.80
        safety_allocation = total_pool - development

        print(f"Allocated to Development: {development}")
        print(f"safety_allocation: {safety_allocation}")
    except ValueError:
        print("Hey! That was not a valid number. Please use  digits only")
        break