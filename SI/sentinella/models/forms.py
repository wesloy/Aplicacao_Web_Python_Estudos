
#Biblioteca de geração do form, lembro que é necessário instalar com pip antes (pip install flask-wtf)
from flask_wtf import FlaskForm
#importando os tipos de campos que serão usados nos formulários
from wtforms import StringField, PasswordField, BooleanField, SelectField, Label, RadioField
#importando validação de campos
from wtforms.validators import DataRequired
#importando bilbioteca de consulta intrelaça sqlalchemy e o wtforms os campos necessários para consultas
from wtforms_sqlalchemy.fields import QuerySelectField
#Tabelas
from sentinella.models.tables import *

#criação parecida com a criação de tabelas
#declarar os campos que serão chamados na view ou templates
#necessário dizer o tipo do campo, o que eles vão receber e é passado como parametro e por fim a validação do campo
class login_form(FlaskForm): 
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])


class config_usuario_form(FlaskForm):    
    opcao_entrada = SelectField("opcao_entrada", validators=[DataRequired()],choices=[('0','SELECIONE UMA ENTRADA'),('1','NOVO'),('2','EDITAR')])
    lista_usuarios = SelectField("lista_usuario", validators=[DataRequired()],choices=Usuarios.campoSelecaoIdRede())
    id_rede = StringField('id_rede',validators=[DataRequired()])    
    nome = StringField("nome", validators=[DataRequired()])
    perfil_acesso = SelectField("perfil_acesso", validators=[DataRequired()],choices=SysUsuariosPerfilDeAcesso.campoSelecao())    
    ativo = BooleanField("ativo")
    
class atualizar_senha_form(FlaskForm):
    senha_atual = PasswordField("senha_atual", validators=[DataRequired()])
    senha_nova = PasswordField("senha_atual", validators=[DataRequired()])
    senha_confirmacao = PasswordField("senha_atual", validators=[DataRequired()])

class resetar_senha_form(FlaskForm):
    lista_usuarios = SelectField("lista_usuario", validators=[DataRequired()],choices=Usuarios.campoSelecaoIdRede())
    nome = StringField("nome", validators=[DataRequired()])