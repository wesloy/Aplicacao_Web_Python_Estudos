from flask import request, jsonify, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from sentinella import app, lm
from sentinella.models.forms import *
from sentinella.models.tables import *
from sentinella.uteis import uteis
#criptografar senhas
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/home", methods = ['GET'])
@app.route("/", methods = ['GET']) 
def index():
    return render_template('index.html')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USUARIOS
@lm.user_loader #pegar o usuário que está logado no momento
def load_user(id):
    return Usuarios.query.filter_by(id=id).first()

@app.route("/login", methods=['GET','POST']) #Liberar os métodos necessários
def login():
    form = login_form()
    if form.validate_on_submit(): #Usando a função de validação criada no formulário para ver se foi digitado alguma coisa
        u = Usuarios.query.filter_by(idRede=form.username.data).first() # validando se as informações inseridas são validadas com o bd
        if not u:
            flash("Usuário não cadastrado no Sentinella!")
            return render_template('login.html', form=form)

        if check_password_hash(u.senha, form.password.data):
            login_user(u)
            #flash("Logado com sucesso!")
            #redirecionando para uma outra página após o login
            return redirect(url_for('index'))
        else:
            flash("Senha incorreta!")
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/config_usuario', methods=['GET','POST'])
@login_required
def config_usuario():
    form = config_usuario_form()

    if request.method == 'POST':

        #CARREGANDO VARIÁVEIS COM INFORMAÇÕES DO FORM
        id = form.lista_usuarios.data
        id_rede = form.id_rede.data
        nome = form.nome.data
        ativo = form.ativo.data
        perfil_acesso = form.perfil_acesso.data
        id_modificacao = current_user.id_Rede()

        if form.validate_on_submit(): #Usando a função de validação criada no formulário para ver se foi digitado alguma coisa

            #NOVO USUÁRIO
            if form.opcao_entrada.data == '1':
                #Evitando duplicidade de cadastro
                u = Usuarios.query.filter_by(idRede=form.id_rede.data).first()
                if u:
                    flash("Usário já está cadastrado no Sentinella!")
                    return render_template('criacao_usuario.html', form=form, id=id)
                
                user = Usuarios(
                    id_rede,            
                    nome,
                    ativo,
                    perfil_acesso,
                    id_modificacao
                )
                db.session.add(user)        
                db.session.commit()
                flash("Usuário inserido com suscesso!")
                return redirect(url_for('config_usuario'))

            #EDITANDO UM USUÁRIO
            if form.opcao_entrada.data == '2':
                u = Usuarios.query.filter_by(id=id).first()
                u.idRede = id_rede
                u.nome = nome
                u.ativo = ativo
                u.perfilAcesso = perfil_acesso
                u.idModificacao = id_modificacao
                u.dataModificacao = dt.datetime.today()
                db.session.commit()
                flash("Usuário atualizado com suscesso!")
                return redirect(url_for('config_usuario'))
        
    return render_template('config_usuario.html', form=form)


@app.route('/info_usuario/<int:id>')
@login_required
def info_usuario(id):
    u = Usuarios.query.filter_by(id=id).all()    
    array = [{'idRede':i.idRede,'nome':i.nome,'perfilAcesso':i.perfilAcesso, 'senha':i.senha, 'ativo':i.ativo} for i in u]
    return jsonify({'info':array})


@app.route('/resetar_senha', methods=['GET','POST'])
@login_required
def resetar_senha():
    form = resetar_senha_form()

    if form.validate_on_submit():
        u = Usuarios.query.filter_by(id=form.lista_usuarios.data).first()
        u.senha = generate_password_hash('123456')    
        db.session.commit()
        flash("Senha do usuário " + u.nome + " foi resetada!")
        return redirect(url_for('resetar_senha'))

    return render_template('senha_resetar.html', form=form)

@app.route('/atualizar_senha', methods=['GET','POST'])
@login_required
def atualizar_senha():
    form = atualizar_senha_form()
    
    if form.validate_on_submit():
        u = Usuarios.query.filter_by(id=int(current_user.get_id())).first()
        if not check_password_hash(u.senha, form.senha_atual.data):
            flash("Senha atual é diferente da digitada!")
            return render_template('senha_atualizar.html', form=form)
        if form.senha_nova.data != form.senha_confirmacao.data:
            flash("Nova senha e confirmação de senha são diferentes!")
            return render_template('senha_atualizar.html', form=form)
    
        u.senha = generate_password_hash(form.senha_nova.data)
        db.session.commit()
        flash("Senha atualizada com sucesso!")
        return render_template('senha_atualizar.html', form=form)

    #senha = generate_password_hash(form.senha.data,method='sha256')
    return render_template('senha_atualizar.html', form=form)
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM CONTORLE DE USUARIOS


@app.route('/testes')
@login_required
def testes():
    dados = FuncionariosHistorico.query.filter_by(nome_associado='Wesley Eloy').all()
    return render_template('teste.html',lista=dados)
    #dados = capturar_dados_sql('select * from [db_Corporate_V3].[dbo].Dados$')
    #dados = capturar_dados_sql("EXECUTE [10.200.48.167].[db_TechOnline].[dbo].sp_clsRelatorioRegistroPlanoAcao_Detalhe  '2019-10-01','2019-10-10'")
    #dados = Usuarios.query.filter_by(idRede='wesleyel').all()
    #dados = SysUsuariosPerfilDeAcesso.perfil_acesso()
    #dados = capturar_dados_sql("EXECUTE dadosCartao '5248163609'")          
    #dados = capturar_dados_sql('Select top 10  * from w_funcionarios_historico')
    #response = [{'Nome':i.nome_associado} for i in dados]    
    #return response
    #return render_template('teste.html',lista=dados)
    