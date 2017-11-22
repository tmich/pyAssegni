# views.py
from tkinter import ttk
import tkinter as tk

class MainView(ttk.Frame):
	def __init__(self, master=None):
		super().__init__(master, padding='0.5i')
		self.grid()
		self.btn1 = ttk.Button(self, text='Nuovo assegno', command=self.on_nuovo)
		self.btn1.pack()
		
	def on_nuovo(self):
		print('on_nuovo')

class NuovoAssegno(ttk.Frame):
	def __init__(self, master=None, aziende=None, fornitori=None):
		super().__init__(master, padding='0.5i')
		self.grid()
		self.grab_set()
		self.azienda=tk.StringVar()
		self.azienda.trace('w', self.on_azienda)
		self.contocorrente=tk.StringVar()
		self.contocorrente.trace('w', self.on_conto)
		self.libretto=tk.StringVar()
		self.libretto.trace('w', self.on_libretto)
		self.assegno=tk.StringVar()
		self.fornitore=tk.StringVar()
		self.importo=tk.DoubleVar()
		ttk.Label(self, text='Azienda').grid(row=0, column=0)
		self.cbazienda = ttk.Combobox(self, textvariable=self.azienda, values=aziende, postcommand=self.on_post)
		self.cbazienda.grid(row=0, column=1)
		ttk.Label(self, text='Conto').grid(row=1, column=0)
		self.cbconto = ttk.Combobox(self, textvariable=self.contocorrente, values=[])
		self.cbconto.grid(row=1, column=1)
		ttk.Label(self, text='Libretto').grid(row=2, column=0)
		self.cblibr = ttk.Combobox(self, textvariable=self.libretto, values=[])
		self.cblibr.grid(row=2, column=1)
		ttk.Label(self, text='Assegno n°').grid(row=3, column=0)
		self.cbass = ttk.Combobox(self, textvariable=self.assegno, values=[])
		self.cbass.grid(row=3, column=1)
		ttk.Label(self, text='Intestato a').grid(row=4, column=0)
		self.cbforn = ttk.Combobox(self, textvariable=self.fornitore, values=fornitori)
		self.cbforn.grid(row=4, column=1)
		ttk.Label(self, text='Importo').grid(row=5, column=0)
		self.tximpo = ttk.Entry(self, textvariable=self.importo)
		self.tximpo.grid(row=5, column=1)
	
	def set_conti(self, conti):
		self.conti=conti
		self.cbconto.configure(values=self.conti)
	
	def set_libretti(self, libretti):
		self.libretti=libretti
		self.cblibr.configure(values=self.libretti)
	
	def set_assegni(self, assegni):
		self.assegni=assegni
		self.cbass.configure(values=self.assegni)
	
	def on_conto(*args):
		print('<NuovoAssegno::on_conto>')
		
	def on_libretto(*args):
		print('<NuovoAssegno::on_libretto>')
	
	def on_azienda(*args):
		print('<NuovoAssegno::on_azienda>')
	
	def on_post(*args):
		print('<NuovoAssegno::on_post>')
