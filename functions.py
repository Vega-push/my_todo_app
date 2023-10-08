FILEPATH = "todos.txt"


def load_todos(filepath=FILEPATH):
	""" load user data from file and save it in a list todos[]"""
	with open(filepath, "r") as file:
		todos = file.readlines()
		return todos


def save_todos(todos_arg, filepath=FILEPATH):
	""" save user date to file """
	with open(filepath, "w") as file:
		file.writelines(todos_arg)
