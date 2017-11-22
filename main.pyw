from tkinter import ttk
import tkinter as tk
from views import MainView
import models
from models import session, User, Assegno

def crea_utente(view):
	# user = User(name=view.nome.get(), fullname=view.nome.get(), password=view.pwd.get())
	# session.add(user)
	# session.commit()
	# print(user)
	for ass in session.query(Assegno):
		print(ass)

def main():
	root=tk.Tk()
	MainView.on_crea=crea_utente
	frm=MainView(root)
	root.title('MainView')
	root.mainloop()

if __name__ == '__main__':
	main()