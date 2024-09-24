def add_contact(contact_list,contact_name,contact_phone, contact_email):
    contact_dict = {"contact_name": contact_name,"contact_phone": contact_phone, "contact_email": contact_email, "favorite":False}
    contact_list.append(contact_dict)
    print(f"\n{contact_name} was successfully added to you contact list")
    return

def view_contact(contact_list):
    for index, contact_dict in enumerate(contact_list,start=1):
        status = "✓" if contact_dict["favorite"] else "No"
        contact_name = contact_dict["contact_name"]
        contact_phone = contact_dict["contact_phone"]
        contact_email = contact_dict["contact_email"]
        print(f"\n{index} - {contact_name} - {contact_phone} - {contact_email} - Favorite: {status}")

    return

def edit_contact(index, contact_list, new_name, new_phone, new_email):
    corrected_index = int(index) - 1
    if corrected_index>=0 and corrected_index<len(contact_list):
        contact_list[corrected_index]["contact_name"] = new_name
        contact_list[corrected_index]["contact_phone"] = new_phone
        contact_list[corrected_index]["contact_email"] = new_email
        print(f"Contact successfully updated")
    else:
        print("Invalid index")

    return

def add_favorite(index, contact_list):
    corrected_index = int(index) - 1
    if corrected_index>=0 and corrected_index<len(contact_list):
        contact_list[corrected_index]["favorite"] = True
        print(f"Contact successfully marked as favorite")
    else:
        print("Invalid index")
    return

def delete_contact(index, contact_list):
    corrected_index = int(index) - 1
    if corrected_index>=0 and corrected_index<len(contact_list):
        del contact_list[corrected_index]
        print("Contact deleted")
    else:
        print("Invalid index")

    return

contact_list = []
while True:
    print("\nAgenda's Menu")
    print("1. Add a Contact")
    print("2. View Contacts")
    print("3. Edit a Contact")
    print("4. Add as a Favorite")
    print("5. Delete a Contact")
    print("6. Exit")

    choice = int(input("Type your option: "))
    
    if choice == 1:
        contact_name = input("Enter contact's name: ")
        contact_phone = input("Enter contact's phone: ")
        contact_email = input("Enter contact's e-mail: ")
        add_contact(contact_list,contact_name,contact_phone, contact_email)
    elif choice == 2:
        view_contact(contact_list)
    elif choice == 3:
        view_contact(contact_list)
        index = input("Type the contact's index that you want to update: ")
        new_name = input("Type the new name: ")
        new_phone = input("Type the new phone number: ")
        new_email = input("Type the new e-mail: ")
        edit_contact(index, contact_list, new_name, new_phone, new_email)
    elif choice == 4:
        view_contact(contact_list)
        index = input("Type the contact's index that you want to mark as favorite: ")
        add_favorite(index, contact_list)
    elif choice == 5:
        view_contact(contact_list)
        index = input("Type the contact's index that you want to delete: ")
        delete_contact(index, contact_list)
    elif choice == 6:
        break
    else:
        print("Invalid Option, please try again.")

print("Program Finished")