import streamlit as st
import functions


def add_todo():
	"""read user input from inputbox and append and save it to todos.txt"""
	new_todo = st.session_state["new_todo"]
	todos.append(new_todo + "\n")
	functions.save_todos(todos)


# anytime you refresh the page python runs the script
todos = functions.load_todos()

# create GUI (order sensitive)
st.title("My Todo App")
st.subheader("Tammi ist doof!!!")
st.write("This app blablabla")

# create checkboxes with todos
for index, todo in enumerate(todos):
	checkbox = st.checkbox(todo, key=todo)
	if checkbox:
		todos.pop(index)
		functions.save_todos(todos)
		del st.session_state[todo]
		st.rerun()  # necessary for checkboxes

st.text_input(label="Enter a todo:", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

st.session_state  # this renders session_state on the webpage
