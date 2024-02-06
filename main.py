from system import System
def main():

    system = System()

    print("Welcome player")
    print("Type 'execute' to enter make commands.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Main> ").strip()
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'execute':
            system.enter_execute_mode()
        else:
            system.process_command(user_input)


if __name__ == "__main__":
    main()





