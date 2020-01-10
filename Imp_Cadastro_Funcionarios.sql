

--EXECUTE IMP_CADASTRO_FUNCIONARIO N'WESLEY ELOY';

USE db_Sentinella;  
GO  
CREATE PROCEDURE IMP_CADASTRO_FUNCIONARIO 
    @usuario_manutencao varchar(50)   
AS   
    SET NOCOUNT ON;  

--ASSOCIADOS ACUMULATIVO
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
dataAtualizacao, 
idAtualizacao
) 
Select 
ia.Nom_Empresa, 
ia.Cod_Empresa, 
ia.Cod_Cpf, 
ia.Cod_Matricula, 
iif(len(ia.Cod_Matricula) < 7 and Not ia.Cod_Matricula is null, 'UB' + replicate('0',6 - len(ia.Cod_Matricula)) + ia.Cod_Matricula,ia.Cod_Matricula), 
ia.Nom_Usuario, 
iif(ia.Dt_Admissao is null, '1900-01-01',convert(date,ia.Dt_Admissao,109)),  
iif(ia.Dt_Demissao is null, '1900-01-01',convert(date,ia.Dt_Demissao,109)),   
ia.num_Centro_Custo, 
ia.Nom_Centro_Custo, 
ia.Nom_Cargo, 
ia.Tp_Sexo, 
ia.Des_Endereco, 
ia.Num_Endereco, 
ia.Des_Complemento, 
ia.Nom_Bairro, 
ia.Nom_Localidade, 
ia.UF_Localidade, 
ia.Num_Cep, 
iif(ia.Dt_Nascimento is null, '1900-01-01',convert(date,ia.Dt_Admissao,109)),  
ia.Idt_Telefone_Usuario, 
ia.Idt_Celular_Usuario, 
ia.Des_Email, 
NULL, 
NULL, 
NULL, 
NULL, 
NULL, 
iif(ia.Cod_Gestor_Hierarq_1 is null,'0', ia.Cod_Gestor_Hierarq_1),  
iif(ia.Cod_Gestor_Hierarq_2 is null,'0', ia.Cod_Gestor_Hierarq_2), 
iif(ia.Cod_Gestor_Hierarq_3 is null,'0', ia.Cod_Gestor_Hierarq_3), 
iif(ia.Cod_Gestor_Hierarq_4 is null,'0', ia.Cod_Gestor_Hierarq_4), 
iif(ia.Cod_Gestor_Hierarq_5 is null,'0', ia.Cod_Gestor_Hierarq_5), 
ge1.Nom_Usuario Gestor1, 
ge2.Nom_Usuario Gestor2, 
ge3.Nom_Usuario Gestor3, 
ge4.Nom_Usuario Gestor4, 
ge5.Nom_Usuario Gestor5, 
iif(ia.Dt_Inicio_Estabilidade_CIPA is null, '1900-01-01',convert(date,ia.Dt_Inicio_Estabilidade_CIPA,109)), 
iif(ia.Dt_Fim_Estabilidade_CIPA is null, '1900-01-01',convert(date,ia.Dt_Fim_Estabilidade_CIPA,109)), 
getdate(), 
@usuario_manutencao 
from db_Corporate_V3.dbo.tb_Imp_Associado ia 
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge1
    on ge1.Cod_Matricula = ia.Cod_Gestor_Hierarq_1
and ge1.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_1
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge2
    on ge2.Cod_Matricula = ia.Cod_Gestor_Hierarq_2
and ge2.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_2
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge3
    on ge3.Cod_Matricula = ia.Cod_Gestor_Hierarq_3
and ge3.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_3
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge4
    on ge4.Cod_Matricula = ia.Cod_Gestor_Hierarq_4
and ge4.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_4
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge5
    on ge5.Cod_Matricula = ia.Cod_Gestor_Hierarq_5
and ge5.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_5
where ia.Dt_Demissao is null

--DESLIGADOS INCREMENTAL
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
dataAtualizacao, 
idAtualizacao
) 
Select 
ia.Nom_Empresa, 
ia.Cod_Empresa, 
ia.Cod_Cpf, 
ia.Cod_Matricula, 
iif(len(ia.Cod_Matricula) < 7 and Not ia.Cod_Matricula is null, 'UB' + replicate('0',6 - len(ia.Cod_Matricula)) + ia.Cod_Matricula,ia.Cod_Matricula), 
ia.Nom_Usuario, 
iif(ia.Dt_Admissao is null, '1900-01-01',convert(date,ia.Dt_Admissao,109)),  
iif(ia.Dt_Demissao is null, '1900-01-01',convert(date,ia.Dt_Demissao,109)),   
ia.num_Centro_Custo, 
ia.Nom_Centro_Custo, 
ia.Nom_Cargo, 
ia.Tp_Sexo, 
ia.Des_Endereco, 
ia.Num_Endereco, 
ia.Des_Complemento, 
ia.Nom_Bairro, 
ia.Nom_Localidade, 
ia.UF_Localidade, 
ia.Num_Cep, 
iif(ia.Dt_Nascimento is null, '1900-01-01',convert(date,ia.Dt_Admissao,109)),  
ia.Idt_Telefone_Usuario, 
ia.Idt_Celular_Usuario, 
ia.Des_Email, 
NULL, 
NULL, 
NULL, 
NULL, 
NULL, 
iif(ia.Cod_Gestor_Hierarq_1 is null,'0', ia.Cod_Gestor_Hierarq_1),  
iif(ia.Cod_Gestor_Hierarq_2 is null,'0', ia.Cod_Gestor_Hierarq_2), 
iif(ia.Cod_Gestor_Hierarq_3 is null,'0', ia.Cod_Gestor_Hierarq_3), 
iif(ia.Cod_Gestor_Hierarq_4 is null,'0', ia.Cod_Gestor_Hierarq_4), 
iif(ia.Cod_Gestor_Hierarq_5 is null,'0', ia.Cod_Gestor_Hierarq_5), 
ge1.Nom_Usuario Gestor1, 
ge2.Nom_Usuario Gestor2, 
ge3.Nom_Usuario Gestor3, 
ge4.Nom_Usuario Gestor4, 
ge5.Nom_Usuario Gestor5, 
iif(ia.Dt_Inicio_Estabilidade_CIPA is null, '1900-01-01',convert(date,ia.Dt_Inicio_Estabilidade_CIPA,109)), 
iif(ia.Dt_Fim_Estabilidade_CIPA is null, '1900-01-01',convert(date,ia.Dt_Fim_Estabilidade_CIPA,109)), 
getdate(), 
@usuario_manutencao 
from db_Corporate_V3.dbo.tb_Imp_Associado ia 
  left join w_funcionarios_historico fh 
	on fh.matricula = ia.Cod_Matricula 
	and fh.cod_empresa = ia.Cod_Empresa  
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge1
   on ge1.Cod_Matricula = ia.Cod_Gestor_Hierarq_1
	and ge1.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_1
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge2
    on ge2.Cod_Matricula = ia.Cod_Gestor_Hierarq_2
	and ge2.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_2
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge3
    on ge3.Cod_Matricula = ia.Cod_Gestor_Hierarq_3
	and ge3.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_3
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge4
    on ge4.Cod_Matricula = ia.Cod_Gestor_Hierarq_4
	and ge4.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_4
  left join db_Corporate_V3.dbo.tb_Imp_Associado Ge5
    on ge5.Cod_Matricula = ia.Cod_Gestor_Hierarq_5
	and ge5.Cod_Empresa_FPW = ia.Cod_Empresa_Gestor_Hierarq_5
where Not ia.Dt_Demissao is null 
		and fh.data_demissao is null;

GO