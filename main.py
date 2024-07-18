# from functions import read_file, write_file
from modules import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(f"It is {now}")
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # the open function creates a file object like how other
        # functions create a string object
        # 'w' means 'write', 'r' means 'read'
        todo = user_action[4:] + "\n"

        todos = functions.read_file()

        todos.append(todo)

        functions.write_file(todos)

    elif user_action.startswith("show"):
        # enumerate basically makes a list of tuples that
        # store the index and item of each item in the list

        todos = functions.read_file()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item.title()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.read_file()

            if number > len(todos):
                print("There is no todo with that number")
                continue

            change = input("Enter edited todo: ")
            todos[number] = change + '\n'

            functions.write_file(todos)
        except ValueError:
            print("Invalid Command!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.read_file()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_file(todos)

            message = f"Todo '{todo_to_remove.title()}' completed!"

            print(message)
        except IndexError:
            print("There is no todo with that number")
            continue
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid.")

print("Bye!")
