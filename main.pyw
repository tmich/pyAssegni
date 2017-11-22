from tkinter import ttk
import tkinter as tk
from views import MainView, NuovoAssegno
import models
from models import session, User, Assegno, Azienda, ContoCorrente, Libretto, Fornitore

root=tk.Tk()

def on_azienda(view, *tail):
	azienda=view.azienda.get()
	conti=[]
	for c in session.query(ContoCorrente).filter(ContoCorrente.azienda.has(Azienda.ragione_sociale==azienda)).all():
		conti.append(c.numero)
	view.set_conti(conti)
	view.contocorrente.set("")
	view.libretto.set("")
	view.assegno.set("")
	
def on_conto(view, *tail):
	contocorrente=view.contocorrente.get()
	libretti=[]
	for l in session.query(Libretto).filter(Libretto.conto.has(ContoCorrente.numero==contocorrente)).all():
		libretti.append(l.numero)
	view.set_libretti(libretti)
	view.libretto.set("")
	view.assegno.set("")

def on_libretto(view, *tail):
	libretto=view.libretto.get()
	assegni=[]
	for a in session.query(Assegno).filter(Assegno.libretto.has(Libretto.numero==libretto)).all():
		assegni.append(a.numero)
	view.set_assegni(assegni)
	view.assegno.set("")
	if len(assegni) > 0:
		view.assegno.set(assegni[0])
	
def nuovo_assegno(view):
	aziende=[]
	fornitori=[]
	for az in session.query(Azienda).all():
		aziende.append(az.ragione_sociale)
	for f in session.query(Fornitore).all():
		fornitori.append(f.denominazione)
	w=tk.Toplevel(root)
	w.title('Nuovo assegno')
	NuovoAssegno.on_azienda = on_azienda
	NuovoAssegno.on_conto = on_conto
	NuovoAssegno.on_libretto = on_libretto
	n=NuovoAssegno(master=w, aziende=aziende, fornitori=fornitori)

def main():
	MainView.on_nuovo=nuovo_assegno
	MainView(root)
	root.title('Assegni')
	root.mainloop()

if __name__ == '__main__':
	main()