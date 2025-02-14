from modules import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkGrey11")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")

input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button(size=2, key="Add", tooltip="Add todo",
                       image_source="add.png")
exit_button = sg.Button("Exit")
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=2, key="Complete", tooltip="Complete todo",
                            image_source="complete.png")

list_box = sg.Listbox(values=functions.read_file(), key="todos",
                      enable_events=True, size=(45, 10))

window = sg.Window('My To-Do App',
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 14))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(time.strftime('%m/%d/%Y %H:%M:%S'))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo.title())
            functions.write_file(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.title() + "\n"
                functions.write_file(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 10))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.read_file()

                todos.remove(todo_to_complete)
                functions.write_file(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 10))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()


