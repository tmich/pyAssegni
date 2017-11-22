import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime, Float

# https://stackoverflow.com/questions/1972259/cannot-open-include-file-config-win-h-no-such-file-or-directory-while-inst
# easy_install mysql-connector-python
engine = sqlalchemy.create_engine("mysql+mysqlconnector://scott:tiger@192.168.56.2/palmi", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Assegno(Base):
	__tablename__ = 'assegno'
	
	id = Column(Integer, primary_key=True)
	id_libretto = Column(Integer)
	numero = Column(String(50))
	data_emissione = Column(DateTime)
	data_scadenza = Column(DateTime)
	beneficiario = Column(String(50))
	importo = Column(Float)
	data_incasso = Column(DateTime)
	note = Column(String(50))
	
	def __repr__(self):
		return "<Assegno(id={0}, beneficiario={1})".format(self.id, self.beneficiario)
	

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