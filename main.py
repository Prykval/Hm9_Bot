def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

@input_error
def add_handler(*args, **kwargs):
    name, phone = args[0].split(' ')
    contacts[name] = phone
    return 'Contact added'

@input_error
def exit_handler():
    return "Good bye!"

@input_error
def hello_handler():
    return 'Hello, how I can help you?'

@input_error
def change_handler(*args, **kwargs):
    name, phone = args[0].split(' ')
    if name not in contacts:
        raise IndexError
    contacts[name] = phone
    return f"Phone number for {name} changed to {phone}"

@input_error
def phone_handler(name):
    if name not in contacts:
        raise IndexError
    return f"Phone number for {name}: {contacts[name]}"

@input_error
def show_all_handler():
    if not contacts:
        return "No contacts available"
    result ='\n'.join(f"{name}: {phone}" for name, phone in contacts.items())
    return result

contacts={}


def main():
    while True: 
        user_input = input("Enter command: ").lower()

        if user_input in ["good bye", "close", "exit"]:
             print(exit_handler())
             break
        
        elif user_input=='hello':
            print(hello_handler())
        
        elif user_input.startswith('add'):
            print(add_handler(user_input[4:]))
        
        
        elif user_input.startswith("change"):
            print(change_handler(user_input[7:]))
        
        elif user_input.startswith('phone'):
            print(phone_handler(user_input[6:]))
        
        elif user_input=="show all":
            print(show_all_handler())
        
        else:
            print("Unknown command. Try again.")

if __name__ == '__main__':
    main()

    
            
