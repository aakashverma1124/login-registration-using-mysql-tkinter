from tkinter import *
import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="root",
  database = "stud1"
)

class Login():
	def __init__(self):
		self.root = Tk()
		self.root.geometry("400x300")
		self.root.title("Login Window")
		self.create_elements()
		self.root.mainloop()
		
	def create_elements(self):
		
		self.username = Label(self.root, text="Username:", font=('Verdana', 14, 'bold'))
		self.username.place(x=50, y=50)

		self.entry_username = Entry(self.root, font=('Verdana', 14))
		self.entry_username.place(x=160, y=50)

		self.password = Label(self.root, text="Password:", font=('Verdana', 14, 'bold'))
		self.password.place(x=50, y=90)

		self.entry_password = Entry(self.root, font=('Verdana', 14))
		self.entry_password.place(x=160, y=90)

		self.login_button = Button(self.root, text="Login", height=2, width=10)
		self.login_button.place(x=50, y=160)

		self.new_user = Label(self.root, text="New User?", font=('Verdana', 10, 'bold'))
		self.new_user.place(x=150, y=140)

		self.register_button = Button(self.root, text="Sign Up", height=2, width=10, command=self.destroy_login)
		self.register_button.place(x=150, y=160)


	def destroy_login(self):
		self.root.destroy()
		register = Register()


class Register():
	def __init__(self):
		self.root = Tk()
		self.root.geometry("500x300")
		self.root.title("Register Window")
		self.create_elements()
		self.root.mainloop()

	def create_elements(self):

		self.username = Label(self.root, text="Username:", font=('Verdana', 14, 'bold'))
		self.username.place(x=50, y=50)

		self.entry_username = Entry(self.root, font=('Verdana', 14))
		self.entry_username.place(x=160, y=50)

		self.password = Label(self.root, text="Password:", font=('Verdana', 14, 'bold'))
		self.password.place(x=50, y=90)

		self.entry_password = Entry(self.root, font=('Verdana', 14))
		self.entry_password.place(x=160, y=90)

		self.name = Label(self.root, text="Name:", font=('Verdana', 14, 'bold'))
		self.name.place(x=50, y=130)

		self.entry_name = Entry(self.root, font=('Verdana', 14))
		self.entry_name.place(x=160, y=130)

		self.register_button = Button(self.root, text="Sign Up", height=2, width=10)
		self.register_button.place(x=50, y=180)

		self.existing_user = Label(self.root, text="Existing User?", font=('Verdana', 10, 'bold'))
		self.existing_user.place(x=150, y=160)

		self.login_button = Button(self.root, text="Login", height=2, width=10, command=self.destroy_register)
		self.login_button.place(x=150, y=180)

	def destroy_register(self):
		self.root.destroy()
		login = Login()


if __name__ == '__main__':
	login = Login()