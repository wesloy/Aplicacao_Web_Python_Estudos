import pyodbc
from sentinella import db
import datetime as dt

def conectar():
    con = pyodbc.connect(
        "DRIVER={SQL Server};"
        "server=UDPCRPDB03;"
        "database=db_Sentinella;"
        "uid=usr_sentinella;"
        "pwd=#sdMr4@D3sk#" #CRIPITOGRAFAR A SENHA
    )
    return con

def capturar_dados_sql(sql):
    con = conectar()
    cursor = con.cursor()
    dados = cursor.execute(sql)
    return dados

def executar_sql(sql):
    con = conectar()
    cursor = con.cursor()

    if cursor.execute(sql):        
        con.commit()
        con.close()
        return True
    else:        
        con.close()
        return False


class Usuarios(db.Model):
    __tablename__= "w_sysUsuarios"
    #declaração da tabela
    id = db.Column(db.Integer, primary_key=True)
    idRede = db.Column(db.String(20), nullable=True, default='SEN INFO')
    ativo = db.Column(db.Boolean, nullable=False, default=False)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(1000), nullable=False, default='123456')
    perfilAcesso = db.Column(db.Integer, nullable=False, default=0)
    online = db.Column(db.Boolean, nullable=False, default=0)
    ultimoAcesso = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    dataModificacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idModificacao = db.Column(db.String(20), nullable=False)

    #construtor
    def __init__(self, idRede, nome, ativo, perfilAcesso, idModificacao):
        self.idRede = idRede
        self.nome = nome
        self.ativo = ativo
        self.perfilAcesso = perfilAcesso
        self.idModificacao = idModificacao

    #qdo se recebe uma lista de usuário, especifica a forma de apresentação    
    def __repr__(self):        
        return "<Id: {}; idRede: {}; ativo: {}; nome: {}; senha: {}; perfilAcesso: {}; online: {}; ultimoAcesso: {}; dataModificacao: {}; idModificacao:{}>" .format(self.id, self.idRede, self.ativo, self.nome, self.senha, self.perfilAcesso, self.online, self.ultimoAcesso, self.dataModificacao, self.idModificacao)

    def campoSelecaoIdRede():
        lista = []
        dados = Usuarios.query
        lista = [('', 'SELECIONE UM ID DE REDE')] + [(str(x.id), x.idRede) for x in dados]
        return lista

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    
    def get_id(self):
        return str(self.id)

    
    def id_Rede(self):
        return str(self.idRede)

    @property
    def name(self):
        return str(self.nome)

class AnalistasPotenciaisRiscos(db.Model):
    __tablename__ = 'w_analistasPotenciaisRiscos'
    #declaração da tabela
    id = db.Column(db.Integer, primary_key=True)
    idServiceView = db.Column(db.String(20), nullable=True)
    ativo = db.Column(db.Boolean, nullable=False, default=0)
    nome = db.Column(db.String(100), nullable=True, unique=True)
    dataModificacao = db.Column(db.DateTime, nullable=True, default='1900-01-01')
    idModificacao = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, nome, ativo):
        self.id = id
        self.nome = nome
        self.ativo = ativo

    def __repr__(self):
        return "<Id: %r, Usuario: %r; Ativo: %r>" % self.id, self.nome, self.ativo

class Autorizacoes(db.Model):
    __tablename__ = 'w_autorizacoes'
    #declaração da tabela
    id = db.Column(db.Integer, primary_key=True)
    cartao = db.Column(db.String(20), nullable=True)
    bin = db.Column(db.String(6), nullable=True)
    cpf = db.Column(db.String(20), nullable=True)
    dataCorte = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    dataVencimento = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    dataTransacao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    dataInclusaoFatura = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    codReferencia = db.Column(db.String(50), nullable=True)
    codAutorizacao = db.Column(db.String(50), nullable=True)
    estabelecimento = db.Column(db.String(50), nullable=True)
    valorTransacao = db.Column(db.Float, nullable=True)
    pos = db.Column(db.String(50), nullable=True)
    ecMaquineta = db.Column(db.String(50), nullable=True)
    ecNome = db.Column(db.String(50), nullable=True)
    ecCidade = db.Column(db.String(50), nullable=True)
    ecCodPais = db.Column(db.String(50), nullable=True)
    codMoeda = db.Column(db.String(50), nullable=True)
    codRamoAtividade = db.Column(db.String(50), nullable=True)
    dataAtualizacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, cartao, cpf):
        self.id = id
        self.cartao = cartao
        self.cpf = cpf

    def __repr__(self):
        return "<Id: %r; Cartão: %r; Cpf: %r>" % self.id, self.cartao, self.cpf

class BaseDados(db.Model):
    __tablename__ = 'w_base'
    id = db.Column(db.Integer, primary_key=True)    
    bin = db.Column(db.String(6), nullable=True)
    cpf = db.Column(db.String(20), nullable=True)
    data_Registro = db.Column(db.DateTime, nullable=False, default='1900-01-01 00:00:00')
    fila_id = db.Column(db.Integer, nullable=False, default=0)
    status_id = db.Column(db.Integer, nullable=False, default=0)
    idCat = db.Column(db.String(20), nullable=True)
    finalizacao_id = db.Column(db.Integer, nullable=False, default=0)
    subFinalizacao_id = db.Column(db.Integer, nullable=False, default=0)
    observacao = db.Column(db.String(500), nullable=False, default='Sem Informação')
    data_Trabalho = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    hora_Inicial = db.Column(db.DateTime, nullable=False, default='1900-01-01 00:00:00')
    hora_Final = db.Column(db.DateTime, nullable=False, default='1900-01-01 00:00:00')
    tempo_Trabalho_Segundos = db.Column(db.Float, nullable=False, default=0)
    valor_Envolvido = db.Column(db.Float, nullable=False, default=0)
    sla_cumprido = db.Column(db.Boolean, nullable=False, default=0)
    gerado_fup = db.Column(db.Boolean, nullable=False, default=0)
    id_Historico = db.Column(db.Integer, nullable=False, default=0)
    data_Abertura = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    id_Abertura = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, bin, cpf):
        self.id = id
        self.bin = bin
        self.cpf = cpf

    def __repr__(self):
        return "<Id: %r; Bin: %r; Cpf: %r>" % self.id, self.bin, self.cpf

class BaseRetornoOuvidoria(db.Model):
    __tablename__ = 'w_baseRetornoOuvidoria'
    id = db.Column(db.Integer, primary_key=True)
    id_base_principal = db.Column(db.Integer, nullable=False, default=0)
    bin = db.Column(db.String(6), nullable=True)
    cpf = db.Column(db.String(15), nullable=True)
    data_Registro = db.Column(db.DateTime, nullable=False, default='1900-01-01 00:00:00')
    fila_id = db.Column(db.Integer, nullable=False, default=0)
    status_id = db.Column(db.Integer, nullable=False, default=0)
    idCat = db.Column(db.String(20), nullable=True)
    finalizacao_id = db.Column(db.Integer, nullable=False, default=0)
    subFinalizacao_id = db.Column(db.Integer, nullable=False, default=0)
    observacao = db.Column(db.String(500), nullable=False, default='Sem Informação')
    data_Trabalho = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    hora_Inicial = db.Column(db.DateTime, nullable=False, default='1900-01-01 00:00:00')
    hora_Final = db.Column(db.DateTime, nullable=False, default='1900-01-01 00:00:00')
    tempo_Trabalho_Segundos = db.Column(db.Float, nullable=False, default=0)
    valor_Envolvido = db.Column(db.Float, nullable=False, default=0)
    sla_cumprido = db.Column(db.Boolean, nullable=False, default=0)
    gerado_fup = db.Column(db.Boolean, nullable=False, default=0)
    id_Historico = db.Column(db.Integer, nullable=False, default=0)
    data_Abertura = db.Column(db.DateTime, nullable=True, default=dt.datetime.today())
    id_Abertura = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, bin, cpf):
        self.id = id
        self.bin = bin
        self.cpf = cpf

    def __repr__(self):
        return "<Id: %r; Bin: %r; Cpf: %r>" % self.id, self.bin, self.cpf

class Cartoes(db.Model):
    __tablename__ = 'w_cartoes'
    id = db.Column(db.Integer, primary_key=True)        
    cpf = db.Column(db.String(20), nullable=False)
    cartao = db.Column(db.String(20), nullable=True)
    bin = db.Column(db.String(6), nullable=True)
    produto = db.Column(db.String(30), nullable=True)
    tipoCartao = db.Column(db.String(20), nullable=True)
    nome = db.Column(db.String(100), nullable=True)
    endereco = db.Column(db.String(100), nullable=True)
    numResidencial = db.Column(db.String(10), nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    estado = db.Column(db.String(100), nullable=True)
    cep = db.Column(db.String(20), nullable=True)
    bloqueio = db.Column(db.String(20), nullable=True)
    ativo = db.Column(db.Boolean, nullable=False, default=0)
    limite_Credito = db.Column(db.Float, nullable=True, default=0)
    limite_Credito_Anterior = db.Column(db.Float, nullable=True, default=0)
    limite_Credito_Disponivel = db.Column(db.Float, nullable=True, default=0)
    limite_Saque = db.Column(db.Float, nullable=True, default=0)
    limite_Saque_Disponivel = db.Column(db.Float, nullable=True, default=0)
    limite_Data_Alteracao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    limite_Fonte_Alteracao = db.Column(db.String(50), nullable=True)
    data_Emissao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    data_Desbloqueio = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    data_Abertura_Conta = db.Column(db.DateTime, nullable=False, default='1900-01-01') 
    dataAtualizacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(15), nullable=True)

    #construtor
    def __init__(self, id, cartao, cpf, nome):
        self.id = id
        self.cartao = cartao
        self.cpf = cpf
        self.nome = nome

    def __repr__(self):
        return "<Id: %r; Cartao: %r; Cpf: %r; Nome: %r>" % self.id, self.cartao, self.cpf, self.nome

class DadosCadastrais(db.Model):
    __tablename__ = 'w_dadosCadastrais'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(20), nullable=False)
    cartao = db.Column(db.String(20), nullable=True)
    bin = db.Column(db.String(6), nullable=True)
    produto = db.Column(db.String(30), nullable=True)
    data_alteracao_End = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    data_alteracao_telefones = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    nome = db.Column(db.String(100), nullable=True)
    data_Nascimento = db.Column(db.DateTime, nullable=True)
    sexo = db.Column(db.String(2), nullable=True)
    nome_2 = db.Column(db.String(100), nullable=True)
    nome_3 = db.Column(db.String(100), nullable=True)
    nome_4 = db.Column(db.String(100), nullable=True)
    tel_residencial = db.Column(db.String(100), nullable=True)
    tel_empresa = db.Column(db.String(100), nullable=True)
    tel_celular = db.Column(db.String(100), nullable=True)
    end_cobranca = db.Column(db.String(250), nullable=True)
    cidade_cobranca = db.Column(db.String(100), nullable=True)
    estado_cobranca = db.Column(db.String(5), nullable=True)
    cep_cobranca = db.Column(db.String(20), nullable=True)
    end_anterior = db.Column(db.String(250), nullable=True)
    cidade_anterior = db.Column(db.String(100), nullable=True)
    estado_anterior = db.Column(db.String(5), nullable=True)
    cep_anterior = db.Column(db.String(20), nullable=True)
    end_correspondencia = db.Column(db.String(250), nullable=True)
    cidade_correspondencia = db.Column(db.String(100), nullable=True)
    estado_correspondencia = db.Column(db.String(5), nullable=True)
    cep_correspondencia = db.Column(db.String(20), nullable=True)
    dataAtualizacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(15), nullable=True)

    #construtor
    def __init__(self, id, cartao, cpf, nome):
        self.id = id
        self.cartao = cartao
        self.cpf = cpf
        self.nome = nome

    def __repr__(self):
        return "<Id: %r; Cartao: %r; Cpf: %r; Nome: %r>" % self.id, self.cartao, self.cpf, self.nome

class ExecucaoRobo(db.Model):
    __tablename__ = 'w_execucao'
    id = db.Column(db.Integer, primary_key=True)
    mainFrame = db.Column(db.String(20), nullable=False)
    macroExecutadaNome = db.Column(db.String(255), nullable=True)
    usuarioMainFrame = db.Column(db.String(20), nullable=False)
    apenasCartoesAtivos = db.Column(db.Boolean, nullable=False, default=0)
    macroExecutadaOK = db.Column(db.Boolean, nullable=False, default=0)
    logErro = db.Column(db.String(255), nullable=True)
    dataPesquisa = db.Column(db.DateTime, nullable=True, default=dt.datetime.today())
    idRedePesquisa = db.Column(db.String(20), nullable=True)
    dataInicio = db.Column(db.DateTime, nullable=True)
    dataConclusao = db.Column(db.DateTime, nullable=True)

    #construtor
    def __init__(self, id, macroExecutadaNome, apenasCartoesAtivos, macroExecutadaOK):
        self.id = id
        self.macroExecutadaNome = macroExecutadaNome
        self.apenasCartoesAtivos = apenasCartoesAtivos
        self.macroExecutadaOK = macroExecutadaOK
    
    def __repr__(self):
        return "<Id: %r; Macro Executada: %r; Cartões Ativos: %r; Execução: %r>" % self.id, self.macroExecutadaNome, self.apenasCartoesAtivos, self.macroExecutadaOK

class Faturas(db.Model):
    __tablename__ = 'w_faturas'
    id = db.Column(db.Integer, primary_key=True)
    cartao = db.Column(db.String(20), nullable=True)
    bin = db.Column(db.String(6), nullable=True)
    cpf = db.Column(db.String(20), nullable=True)    
    dataCorte = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    dataVencimento = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    dataPagamento = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    valorFatura = db.Column(db.Float, nullable=True)
    valorPagamento = db.Column(db.Float, nullable=True)
    dataAtualizacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(15), nullable=True)

    #construtor
    def __init__(self, id, cartao, dataCorte, valorFatura):
        self.id = id
        self.cartao = cartao
        self.dataCorte = dataCorte
        self.valorFatura = valorFatura
    
    def __repr__(self):
        return "<Id: %r; Cartão: %r; Data Corte: %r; Valor Fatura: %r>" % self.id, self.cartao, self.dataCorte, self.valorFatura

class Funcionarios(db.Model):
    __tablename__ = 'w_funcionarios'
    id = db.Column(db.Integer, primary_key=True)
    nome_empresa = db.Column(db.String(255), nullable=True)
    matricula = db.Column(db.String(20), nullable=True)
    ub = db.Column(db.String(20), nullable=True)
    nome_associado = db.Column(db.String(255), nullable=True)
    data_de_admissao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    data_demissao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    codcentro_de_custo = db.Column(db.String(255), nullable=True)
    descrcentro_de_custo = db.Column(db.String(255), nullable=True)
    cargo_do_associado = db.Column(db.String(255), nullable=True)
    sexo = db.Column(db.String(255), nullable=True)
    rua = db.Column(db.String(255), nullable=True)
    numero = db.Column(db.String(255), nullable=True)
    complemento = db.Column(db.String(255), nullable=True)
    bairro = db.Column(db.String(255), nullable=True)
    cidade = db.Column(db.String(255), nullable=True)
    estado = db.Column(db.String(255), nullable=True)
    cep = db.Column(db.String(255), nullable=True)
    pais = db.Column(db.String(255), nullable=True)
    cpf = db.Column(db.String(255), nullable=True)
    data_de_nascimento = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    num_filhos = db.Column(db.Integer, nullable=True)
    nome_do_pai = db.Column(db.String(255), nullable=True)
    nome_da_mae = db.Column(db.String(255), nullable=True)
    nome_do_conjuge = db.Column(db.String(255), nullable=True)
    nome_dependente_01 = db.Column(db.String(255), nullable=True)
    cpf_dependente_01 = db.Column(db.String(255), nullable=True)
    relacao_dependente_01 = db.Column(db.String(255), nullable=True)
    nome_dependente_02 = db.Column(db.String(255), nullable=True)
    cpf_dependente_02 = db.Column(db.String(255), nullable=True)
    relacao_dependente_02 = db.Column(db.String(255), nullable=True)
    nome_dependente_03 = db.Column(db.String(255), nullable=True)
    cpf_dependente_03 = db.Column(db.String(255), nullable=True)
    relacao_dependente_03 = db.Column(db.String(255), nullable=True)
    nome_dependente_04 = db.Column(db.String(255), nullable=True)
    cpf_dependente_04 = db.Column(db.String(255), nullable=True)
    relacao_dependente_04 = db.Column(db.String(255), nullable=True)
    nome_dependente_05 = db.Column(db.String(255), nullable=True)
    cpf_dependente_05 = db.Column(db.String(255), nullable=True)
    relacao_dependente_05 = db.Column(db.String(255), nullable=True)
    nome_dependente_06 = db.Column(db.String(255), nullable=True)
    cpf_dependente_06 = db.Column(db.String(255), nullable=True)
    relacao_dependente_06 = db.Column(db.String(255), nullable=True)
    nome_dependente_07 = db.Column(db.String(255), nullable=True)
    cpf_dependente_07 = db.Column(db.String(255), nullable=True)
    relacao_dependente_07 = db.Column(db.String(255), nullable=True)
    nome_dependente_08 = db.Column(db.String(255), nullable=True)
    cpf_dependente_08 = db.Column(db.String(255), nullable=True)
    relacao_dependente_08 = db.Column(db.String(255), nullable=True)
    nome_dependente_09 = db.Column(db.String(255), nullable=True)
    cpf_dependente_09 = db.Column(db.String(255), nullable=True)
    relacao_dependente_09 = db.Column(db.String(255), nullable=True)
    nome_dependente_10 = db.Column(db.String(255), nullable=True)
    cpf_dependente_10 = db.Column(db.String(255), nullable=True)
    relacao_dependente_10 = db.Column(db.String(255), nullable=True)
    ddd = db.Column(db.String(255), nullable=True)
    telefone = db.Column(db.String(255), nullable=True)
    celular = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    responsavel_gh = db.Column(db.String(255), nullable=True)
    dataAtualizacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(15), nullable=True)

    #construtor
    def __init__(self, id, nome_empresa, matricula, nome_associado):
        self.id = id
        self.nome_empresa = nome_empresa
        self.matricula = matricula
        self.nome_associado = nome_associado
    
    def __repr__(self):
        return "<Id: %r; Nome Empresa: %r; Matrícula: %r; Nome Associado: %r>" % self.id, self.nome_empresa, self.matricula, self.nome_associado

class FuncionariosHistorico(db.Model):
    __tablename__ = 'w_funcionarios_historico'
    id = db.Column(db.Integer, primary_key=True)
    nome_empresa = db.Column(db.String(255), nullable=True)
    cpf = db.Column(db.String(255), nullable=True)
    matricula = db.Column(db.String(20), nullable=True)
    ub = db.Column(db.String(20), nullable=True)
    nome_associado = db.Column(db.String(255), nullable=True)
    data_de_admissao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    data_demissao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    codcentro_de_custo = db.Column(db.String(255), nullable=True)
    descrcentro_de_custo = db.Column(db.String(255), nullable=True)
    cargo_do_associado = db.Column(db.String(255), nullable=True)
    sexo = db.Column(db.String(255), nullable=True)
    rua = db.Column(db.String(255), nullable=True)
    numero = db.Column(db.String(255), nullable=True)
    complemento = db.Column(db.String(255), nullable=True)
    bairro = db.Column(db.String(255), nullable=True)
    cidade = db.Column(db.String(255), nullable=True)
    estado = db.Column(db.String(255), nullable=True)
    cep = db.Column(db.String(255), nullable=True)    
    qtde_filhos = db.Column(db.Integer, nullable=True)
    data_de_nascimento = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    telefone = db.Column(db.String(255), nullable=True)
    celular = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    gestor_1 = db.Column(db.String(255), nullable=True)
    gestor_2 = db.Column(db.String(255), nullable=True)
    gestor_3 = db.Column(db.String(255), nullable=True)
    gestor_4 = db.Column(db.String(255), nullable=True)
    gestor_5 = db.Column(db.String(255), nullable=True)
    cod_emp_gestor_1 = db.Column(db.Integer, nullable=False, default=0)
    cod_emp_gestor_2 = db.Column(db.Integer, nullable=False, default=0)
    cod_emp_gestor_3 = db.Column(db.Integer, nullable=False, default=0)
    cod_emp_gestor_4 = db.Column(db.Integer, nullable=False, default=0)
    cod_emp_gestor_5 = db.Column(db.Integer, nullable=False, default=0)
    matricula_gestor_1 = db.Column(db.String(255), nullable=True)
    matricula_gestor_2 = db.Column(db.String(255), nullable=True)
    matricula_gestor_3 = db.Column(db.String(255), nullable=True)
    matricula_gestor_4 = db.Column(db.String(255), nullable=True)
    matricula_gestor_5 = db.Column(db.String(255), nullable=True)
    data_estabilidade_inicio = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    data_estabilidade_fim = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    motivo_estabilidade = db.Column(db.String(255), nullable=True)
    estado_civil = db.Column(db.String(255), nullable=True)
    escolaridade = db.Column(db.String(255), nullable=True)
    dataAtualizacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(15), nullable=True)

    #construtor
    def __init__(self, id, nome_empresa, matricula, nome_associado):
        self.id = id
        self.nome_empresa = nome_empresa
        self.matricula = matricula
        self.nome_associado = nome_associado
    
    def __repr__(self):
        #return "<Id: %r, Nome Empresa: %r>" % (self.id, self.nome_empresa)
        return "<Id: %r; Nome Empresa: %r; Matrícula: %r; Nome Associado: %r>" % (self.id, self.nome_empresa, self.matricula, self.nome_associado)


class Laudos(db.Model):
    __tablename__ = 'w_laudos'
    id = db.Column(db.Integer, primary_key=True)
    protocolo_senttinela = db.Column(db.Integer, nullable=False, default=0)
    nome_arquivo = db.Column(db.String(100), nullable=False, default='SEM ARQUIVO')
    data_geracao = db.Column(db.DateTime, nullable=False, default='1900-01-01 00:00:00')
    resumo_incidente = db.Column(db.String(max), nullable=False, default='SEM RESUMO')
    resultado_analise = db.Column(db.String(max), nullable=False, default='RESULTADO NAO INFORMADO')
    endereco_laudo = db.Column(db.String(max), nullable=True)

    #construtor
    def __init__(self, id, protocolo_senttinela, resumo_incidente, resultado_analise):
        self.id = id
        self.protocolo_senttinela = protocolo_senttinela
        self.resumo_incidente = resumo_incidente
        self.resultado_analise = resultado_analise
    
    def __repr__(self):
        return "<Id: %r; Protocolo Sentinella: %r; Resumo Incidente: %r; Resultado Análise: %r>" % self.id, self.protocolo_senttinela, self.resumo_incidente, self.resultado_analise

class LaudosEvidencias(db.Model):
    __tablename__ = 'w_laudos_evidencias'
    id = db.Column(db.Integer, primary_key=True)
    id_senttinela = db.Column(db.Integer, nullable=False, default=0)
    evidencia = db.Column(db.String(max), nullable=False, default='SEM EVIDENCIA')
    imagem_evidencia = db.Column(db.Binary, nullable=True)
    
    #construtor
    def __init__(self, id, id_senttinela, evidencia):
        self.id = id
        self.id_senttinela = id_senttinela
        self.evidencia = evidencia
    
    def __repr__(self):
        return "<Id: %r; Protocolo Sentinella: %r; Evidência: %r>" % self.id, self.id_senttinela, self.evidencia

class MainFrame(db.Model):
    __tablename__ = 'w_MainFrame'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False, default=0)
    mainframe = db.Column(db.String(255), nullable=True)
    nome = db.Column(db.String(255), nullable=True)
    usuario = db.Column(db.String(255), nullable=True)
    senha = db.Column(db.String(255), nullable=True)
    sessao = db.Column(db.String(255), nullable=True)
    dt_alterar_senha = db.Column(db.DateTime, nullable=True)
    
    #construtor
    def __init__(self, id, mainframe, nome, usuario):
        self.id = id
        self.mainframe = mainframe
        self.nome = nome
        self.usuario = usuario
    
    def __repr__(self):
        return "<Id: %r; MainFrame: %r; Nome: %r; Usuário: %r>" % self.id, self.mainframe, self.nome, self.usuario

class Manutencoes(db.Model):
    __tablename__ = 'w_manutencoes'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(20), nullable=True)
    cartao = db.Column(db.String(20), nullable=True)
    bin = db.Column(db.String(6), nullable=True)
    task = db.Column(db.String(10), nullable=True)
    descricaoManutencao = db.Column(db.String(255), nullable=True)
    dataManutencao = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    horaManutencao = db.Column(db.String(20), nullable=False, default='00:00:00')
    usuarioRealizouManutencao = db.Column(db.String(10), nullable=True)
    departamentoManutencao = db.Column(db.String(10), nullable=True)
    dataAtualizacao = db.Column(db.DateTime, nullable=False, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, cpf, cartao, descricaoManutencao):
        self.id = id
        self.cpf = cpf
        self.cartao = cartao
        self.descricaoManutencao = descricaoManutencao
    
    def __repr__(self):
        return "<Id: %r; Cpf: %r; Cartão: %r; Descrição Manutenção: %r>" % self.id, self.cpf, self.cartao, self.descricaoManutencao

class SysFilas(db.Model):
    __tablename__ = 'w_sysFilas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=True)
    grupo = db.Column(db.String(100), nullable=True)
    sla = db.Column(db.Integer, nullable=False, default=1)
    regraNegocio = db.Column(db.String(500), nullable=True)
    ativo = db.Column(db.Boolean, nullable=False, default=0)
    dataAtualizacao = db.Column(db.DateTime, nullable=True, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, descricao, ativo):
        self.id = id
        self.descricao = descricao
        self.ativo = ativo        
    
    def __repr__(self):
        return "<Id: %r; Descrição: %r; Ativo: %r>" % self.id, self.descricao, self.ativo

class SysFinalizacoes(db.Model):
    __tablename__ = 'w_sysFinalizacoes'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=True)
    ativo = db.Column(db.Boolean, nullable=False, default=0)
    fila_id = db.Column(db.Integer, nullable=True)
    geraNovoCaso = db.Column(db.Boolean, nullable=False, default=0)
    agingNovoCaso = db.Column(db.Integer, nullable=False, default=0)
    filaNovoCaso = db.Column(db.Integer, nullable=False, default=0)
    dataAtualizacao = db.Column(db.DateTime, nullable=True, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, descricao, ativo):
        self.id = id
        self.descricao = descricao
        self.ativo = ativo        
    
    def __repr__(self):
        return "<Id: %r; Descrição: %r; Ativo: %r>" % self.id, self.descricao, self.ativo

class SysSubFinalizacoes(db.Model):
    __tablename__ = 'w_sysSubFinalizacoes'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=0)
    finalizacao_id = db.Column(db.Integer, nullable=True)
    fila_id = db.Column(db.Integer, nullable=True)
    geraNovoCaso = db.Column(db.Boolean, nullable=False, default=0)
    agingNovoCaso = db.Column(db.Integer, nullable=False, default=0)
    filaNovoCaso = db.Column(db.Integer, nullable=True, default=0)
    dataAtualizacao = db.Column(db.DateTime, nullable=True, default=dt.datetime.today())
    idAtualizacao = db.Column(db.String(10), nullable=True)

    #construtor
    def __init__(self, id, descricao, ativo):
        self.id = id
        self.descricao = descricao
        self.ativo = ativo        
    
    def __repr__(self):
        return "<Id: %r; Descrição: %r; Ativo: %r>" % self.id, self.descricao, self.ativo

class SysLogImportacao(db.Model):
    __tablename__ = 'w_sysLogImportacao'
    id = db.Column(db.Integer, primary_key=True)
    acao = db.Column(db.String(50), nullable=True)
    data_Hora = db.Column(db.DateTime, nullable=True)
    fila_id = db.Column(db.Integer, nullable=False)
    fila_nome = db.Column(db.String(50), nullable=True)
    qtde_registros = db.Column(db.Integer, nullable=False, default=0)
    id_rede = db.Column(db.String(10), nullable=True)
    hostname = db.Column(db.String(20), nullable=True)
    ip = db.Column(db.String(20), nullable=True)
    mac = db.Column(db.String(20), nullable=True)
    versao_Sistema = db.Column(db.String(255), nullable=True)

    #construtor
    def __init__(self, id, acao, fila_nome, data_Hora, qtde_registros):
        self.id = id
        self.acao = acao
        self.fila_nome = fila_nome
        self.data_Hora = data_Hora
        self.qtde_registros = qtde_registros
    
    def __repr__(self):
        return "<Id: %r; Ação: %r; Fila nome: %r; Data Hora: %r; Qtde Registros: %r>" % self.id, self.acao, self.fila_nome, self.data_Hora, self.qtde_registros

class SysLogs(db.Model):
    __tablename__ = 'w_sysLogs'
    id = db.Column(db.Integer, primary_key=True)    
    data = db.Column(db.DateTime, nullable=True, default=dt.datetime.today())
    idRede = db.Column(db.String(20), nullable=True)
    idFerramenta = db.Column(db.String(20), nullable=True)
    log = db.Column(db.String(1000), nullable=True)
    funcaoExecutada = db.Column(db.String(255), nullable=True)
    versaoSistema = db.Column(db.String(255), nullable=True)
    idioma = db.Column(db.String(50), nullable=True)
    hostname = db.Column(db.String(50), nullable=True)
    ip = db.Column(db.String(30), nullable=True)
    macAddress = db.Column(db.String(30), nullable=True)
    
    #construtor
    def __init__(self, id, acao, data, log):
        self.id = id
        self.acao = acao
        self.data = data
        self.log = log
            
    def __repr__(self):
        return "<Id: %r; Ação: %r; Data: %r; Log: %r>" % self.id, self.acao, self.data, self.log

class SysProdutos(db.Model):
    __tablename__ = 'w_sysProdutos'
    id = db.Column(db.Integer, primary_key=True)
    bin = db.Column(db.String(255), nullable=True)
    tipoCartao = db.Column(db.String(255), nullable=True)
    produto = db.Column(db.String(255), nullable=True)
    emissor = db.Column(db.String(255), nullable=True)
    eps = db.Column(db.String(255), nullable=True)
    prioridade = db.Column(db.Integer, nullable=True)
    
    #construtor
    def __init__(self, bin, tipoCartao, produto, emissor, eps):
        self.bin = bin
        self.tipoCartao = tipoCartao
        self.produto = produto
        self.emissor = emissor
        self.eps = eps
            
    def __repr__(self):
        return "<Bin: %r; Tipo Cartão: %r; Produto: %r; Emissor: %r; EPS: %r>" % self.bin, self.tipoCartao, self.produto, self.emissor, self.eps

class SysUsuariosPerfilDeAcesso(db.Model):
    __tablename__ = 'w_sysUsuariosPerfilDeAcesso'
    id = db.Column(db.Integer, primary_key=True)
    perfilAcesso = db.Column(db.String(50), nullable=True)

    
    def campoSelecao():
        lista = []
        dados = SysUsuariosPerfilDeAcesso.query
        lista = [('', 'SELECIONE UM PERFIL')] + [(str(x.id), x.perfilAcesso) for x in dados]
        return lista


    #construtor
    def __init__(self, id, perfilAcesso):
        self.id = id
        self.perfilAcesso = perfilAcesso
            
    def __repr__(self):
        return "<ID: {}; Perfil de Acesso: {}>" .format(self.id, self.perfilAcesso)
