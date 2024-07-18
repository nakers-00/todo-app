from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.CloseButton("Close")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [exit_button]],
                   font=('Helvetica', 14))
while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)
        case sg.WIN_CLOSED:
            break

window.close()


