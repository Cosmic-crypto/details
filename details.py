details = {}
user_inp = input("hello user would you like to add(1) find(2) any person/s' details?")

if user_inp == '1' or user_inp == 'add':
    while True:
        user_detail_name = input("please enter the person's name: ").lower()
        user_detail_contact = input("Please enter the person's email/mobile number (only 1):")
        if not user_inp == None:
            details[user_detail_name] = user_detail_contact
            with open('contacts.txt', 'a') as f_contact:
                f_contact.write(str(details) + '\n')
            print('thank you for adding to our database! we hope you have a good day')
            break
        else:
            print('Please enter something')

elif user_inp == '2' or user_inp == 'find':
    find = input("enter either the person's name, email, or /all to see every user: ")

    if find == "/all":
        confirm = input("This will show ALL contacts. Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            with open('contacts.txt', 'r') as f_contact:
                print("\nAll Contacts:")
                for line in f_contact:
                    print(line.strip())
        else:
            print("Cancelled showing all contacts.")
    else:
        with open('contact.txt', 'r') as f_contact:
            for line in f_contact:
                if find.lower() in line.lower():
                    print('Person has been found:', line.strip())

elif user_inp == '4' or user_inp == 'DELETE':
    password = input('enter password:')
    if password == 'DELETE!@#10dec13':
        question = input('Are you sure you want to delete this data base!?')
        if question == 'yes':
            with open('contacts.txt', 'w') as f_contact:
                f_contact.write('')
