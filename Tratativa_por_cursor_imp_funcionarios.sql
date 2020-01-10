--variáveis
DECLARE	@matricula_fun varchar(10)
		,@cod_emp_gestor_1 int
		,@cod_emp_gestor_2 int
		,@cod_emp_gestor_3 int
		,@cod_emp_gestor_4 int
		,@cod_emp_gestor_5 int
		,@mat_gestor_1 varchar(10)
		,@mat_gestor_2 varchar(10)
		,@mat_gestor_3 varchar(10)
		,@mat_gestor_4 varchar(10)
		,@mat_gestor_5 varchar(10)


--Declaração do cursor
DECLARE crs_gestores CURSOR FOR
SELECT matricula
		,cod_emp_gestor_1 
		,cod_emp_gestor_2 
		,cod_emp_gestor_3 
		,cod_emp_gestor_4 
		,cod_emp_gestor_5 
		,matricula_gestor_1
		,matricula_gestor_2
		,matricula_gestor_3
		,matricula_gestor_4
		,matricula_gestor_5
from w_funcionarios_historico 
where gestor_1 is null 

--Abrindo cursor, ou seja, realizando efetivamente a consulta declarada acima.
OPEN crs_gestores

--capturando a primeira linha, e armazenado nas variáveis
FETCH crs_gestores
INTO @matricula_fun
	,@cod_emp_gestor_1
	,@cod_emp_gestor_2
	,@cod_emp_gestor_3
	,@cod_emp_gestor_4
	,@cod_emp_gestor_5
	,@mat_gestor_1
	,@mat_gestor_2
	,@mat_gestor_3
	,@mat_gestor_4
	,@mat_gestor_5

-- Loop. O Fetch_Status retorna os valores 0 [Ok], -1[Falha] e -2 [Registro perdido]
WHILE (@@FETCH_STATUS <> -1)
BEGIN
	if not @mat_gestor_1 is null 
		update w_funcionarios_historico set 
		gestor_1 = (select top 1 nome_associado from w_funcionarios_historico where matricula = @mat_gestor_1 and cod_empresa = @cod_emp_gestor_1)
		where matricula = @matricula_fun

	if not @mat_gestor_2 is null 
		update w_funcionarios_historico set 
		gestor_2 = (select top 1 nome_associado from w_funcionarios_historico where matricula = @mat_gestor_2 and cod_empresa = @cod_emp_gestor_2)
		where matricula = @matricula_fun

	if not @mat_gestor_3 is null 
		update w_funcionarios_historico set 
		gestor_3 = (select top 1 nome_associado from w_funcionarios_historico where matricula = @mat_gestor_3 and cod_empresa = @cod_emp_gestor_3)
		where matricula = @matricula_fun

	if not @mat_gestor_4 is null 
		update w_funcionarios_historico set 
		gestor_4 = (select top 1 nome_associado from w_funcionarios_historico where matricula = @mat_gestor_4 and cod_empresa = @cod_emp_gestor_4)
		where matricula = @matricula_fun

	if not @mat_gestor_5 is null 
		update w_funcionarios_historico set 
		gestor_5 = (select top 1 nome_associado from w_funcionarios_historico where matricula = @mat_gestor_5 and cod_empresa = @cod_emp_gestor_5)
		where matricula = @matricula_fun

--Próximo registro da consulta
FETCH crs_gestores
INTO @matricula_fun
	,@cod_emp_gestor_1
	,@cod_emp_gestor_2
	,@cod_emp_gestor_3
	,@cod_emp_gestor_4
	,@cod_emp_gestor_5
	,@mat_gestor_1
	,@mat_gestor_2
	,@mat_gestor_3
	,@mat_gestor_4
	,@mat_gestor_5

END

-- Fecha o cursor
CLOSE crs_gestores
-- Remove a referência do cursor
DEALLOCATE crs_gestores