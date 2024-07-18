FILEPATH = 'files/todos.txt'

def read_file(filepath=FILEPATH):
    """ Read a text file abd retyrb the list of
    to-do itmes.
    """

    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_file(todos_arg, filepath=FILEPATH):
    """ Write  the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")