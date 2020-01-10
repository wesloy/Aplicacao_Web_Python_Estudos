--Inserindo informações históricas de funcionários, recebidas por planilha
INSERT INTO w_funcionarios_historico (
nome_empresa, 
cod_empresa, 
cpf, 
matricula, 
ub, 
nome_associado, 
data_de_admissao, 
data_demissao, 
codcentro_de_custo, 
descrcentro_de_custo, 
cargo_do_associado, 
sexo, 
rua, 
numero, 
complemento, 
bairro, 
cidade, 
estado, 
cep, 
qtde_filhos, 
data_de_nascimento, 
telefone, 
celular, 
email, 
gestor_1, 
gestor_2, 
gestor_3, 
gestor_4, 
gestor_5, 
cod_emp_gestor_1, 
cod_emp_gestor_2, 
cod_emp_gestor_3, 
cod_emp_gestor_4, 
cod_emp_gestor_5,
matricula_gestor_1, 
matricula_gestor_2, 
matricula_gestor_3, 
matricula_gestor_4, 
matricula_gestor_5, 
data_estabilidade_inicio, 
data_estabilidade_fim, 
motivo_estabilidade, 
estado_civil, 
escolaridade, 
dataAtualizacao, 
idAtualizacao
) 
Select 
nome_empresa, 
'', 
cpf, 
matricula, 
ub, 
nome_associado, 
data_de_admissao, 
data_demissao, 
codcentro_de_custo, 
descrcentro_de_custo, 
cargo_do_associado, 
sexo, 
rua, 
numero, 
complemento, 
bairro, 
cidade, 
estado, 
cep, 
num_filhos, 
data_de_nascimento, 
telefone, 
celular, 
email, 
responsavel_gh, 
Null, 
Null, 
Null, 
Null, 
0, 
0, 
0, 
0, 
0, 
Null, 
Null, 
Null, 
Null, 
Null, 
'1900-01-01', 
'1900-01-01', 
'', 
'', 
'', 
dataAtualizacao, 
idAtualizacao  
from w_funcionarios



--Atualizando o Gestor 2
update a set 
a.gestor_2 = b.gestor_1 
from w_funcionarios_historico a 
inner join w_funcionarios_historico b 
on a.gestor_1 = b.nome_associado 
where a.gestor_2 is null

--Atualizando o Gestor 3
update a set 
a.gestor_3 = b.gestor_1 
from w_funcionarios_historico a 
inner join w_funcionarios_historico b 
on a.gestor_2 = b.nome_associado 
where a.gestor_3 is null

--Atualizando o Gestor 4
update a set 
a.gestor_4 = b.gestor_1 
from w_funcionarios_historico a 
inner join w_funcionarios_historico b 
on a.gestor_3 = b.nome_associado 
where a.gestor_4 is null

--Atualizando o Gestor 5
update a set 
a.gestor_5 = b.gestor_1 
from w_funcionarios_historico a 
inner join w_funcionarios_historico b 
on a.gestor_4 = b.nome_associado 
where a.gestor_5 is null


--select * from w_funcionarios_historico where format(dataAtualizacao,'yyyy-MM-dd') < '2019-12-05'