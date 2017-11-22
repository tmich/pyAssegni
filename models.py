import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import DateTime, Float
from cfg import *

# https://stackoverflow.com/questions/1972259/cannot-open-include-file-config-win-h-no-such-file-or-directory-while-inst
# easy_install mysql-connector-python
engine = sqlalchemy.create_engine("mysql+mysqlconnector://{0}:{1}@{2}/{3}".format(DB_USER, DB_PASS, DB_HOST, DB_NAME), echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Assegno(Base):
	__tablename__ = 'assegno'
	
	id = Column(Integer, primary_key=True)
	id_libretto = Column(Integer, ForeignKey('libretto_assegni.id'))
	numero = Column(String(50))
	data_emissione = Column(DateTime)
	data_scadenza = Column(DateTime)
	beneficiario = Column(String(50))
	importo = Column(Float)
	data_incasso = Column(DateTime)
	note = Column(String(50))
	
	libretto = relationship("Libretto", back_populates="assegni")
	
	def __repr__(self):
		return "<Assegno(id={0}, beneficiario={1})>".format(self.id, self.beneficiario)
	
class Azienda(Base):
	__tablename__ = 'azienda'
	
	id = Column(Integer, primary_key=True)
	ragione_sociale = Column(String(100))
	indirizzo = Column(String(100))
	partita_iva = Column(String(20))
	
	conti = relationship("ContoCorrente", back_populates="azienda")
	
	def __repr__(self):
		return "<Azienda {0}>".format(self.ragione_sociale)

class ContoCorrente(Base):
	__tablename__ = 'conto_corrente'
	
	id = Column(Integer, primary_key=True)
	id_azienda = Column(Integer, ForeignKey("azienda.id"))
	numero = Column(String(50))
	banca = Column(String(100))
	sede = Column(String(50))
	agenzia = Column(String(50))
	note = Column(String(200))
	
	azienda = relationship("Azienda", back_populates="conti")

class Fornitore(Base):
	__tablename__ = 'fornitori'
	
	id = Column(Integer, primary_key=True)
	denominazione = Column(String(100))
	indirizzo = Column(String(100))
	telefono = Column(String(100))
	partita_iva = Column(String(100))


class Libretto(Base):
	__tablename__ = 'libretto_assegni'
	
	id = Column(Integer, primary_key=True)
	id_conto_corrente = Column(Integer, ForeignKey("conto_corrente.id"))
	numero = Column(String(50))
	codice = Column(String(100))
	qta = Column(Integer)
	
	conto = relationship("ContoCorrente")
	assegni = relationship("Assegno", back_populates="libretto")
	
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (
                        self.name, self.fullname, self.password)

#Base.metadata.create_all(engine)