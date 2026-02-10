firstname = input("What's your first name? : " )
lastname = input("What's your last name? : " )

print(f"Well, pleased to meet you, {firstname.strip("ra").replace(" ", "")} {lastname.strip().replace(" ", "")}")