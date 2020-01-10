import os.path 
import urllib
# import sqlalchemy as sa


DEBUG = True
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)) # Caminho absoluto do diretório da aplicação
SECRET_KEY = '23-5-19-12-5-25_5-12-15-25' # Chave de criptografia de informações transacionadas entre os formulários
SESSION_PROTECTION = 'strong'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_files')
SQLALCHEMY_TRACK_MODIFICATIONS = False
WSGI_HANDLER = "sentinella.wsgi.application"

#CONEXÃO SQL SERVER:
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=UDPCRPDB03;DATABASE=db_Sentinella;UID=usr_sentinella;PWD=#sdMr4@D3sk#")
#SQLALCHEMY_DATABASE_URI = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect={}".format(params)

