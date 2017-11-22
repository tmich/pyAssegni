# views.py
from tkinter import ttk
import tkinter as tk

class MainView(ttk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.nome=tk.StringVar()
		self.pwd=tk.StringVar()
		self.grid()
		self.txnome = ttk.Entry(self, textvariable=self.nome)
		self.txnome.pack()
		self.txpwd = ttk.Entry(self, textvariable=self.pwd)
		self.txpwd.pack()
		self.btn1 = ttk.Button(self, text='Crea utente', command=self.on_crea)
		self.btn1.pack()
		
	def on_crea(self):
		print('on_crea')
		pass
