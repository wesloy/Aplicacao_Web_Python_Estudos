---Criação da PROCEDURE
USE db_Sentinella;  
GO  
CREATE PROCEDURE selecao
    @cpf nvarchar(20)    
AS   
    SET NOCOUNT ON;  
    SELECT *   
    FROM w_base  
    WHERE cpf = @cpf;    
GO  
	
---Execução da PROCEDURE
EXECUTE selecao N'5248163609'; 




--EXEMPLO DE LOOPING...
DECLARE @vQtd_cupons varchar(50)
       ,@vApuracao_ptsvp varchar(50)
       ,@vApuracao_mesfch varchar(50)
       ,@vApuracao_anofch varchar(50)
       ,@vApuracao_id_client varchar(50)
       ,@vClients_username varchar(50)

-- Declaração do cursor. Nesse ponto você especifica a qual consulta o cursor irá manipular
DECLARE Crs_teste CURSOR FOR
SELECT qtd_cupons
      ,apuracao_ptsvp
      ,apuracao_mesfch
      ,apuracao_anofch
      ,apuracao_id_client
      ,clients_username
from #tmp_teste

-- Abertura do cursor. Aqui a consulta é feita e o Cursor mantem as informações
OPEN Crs_teste 

-- Recupera a linha do cursor 
FETCH Crs_teste 
-- Define o valor das variáveis com os valores da linha que ele está percorrendo. 
-- É importante que as variáveis estejam na mesma ordem que as colunas na consulta
INTO @vQtd_cupons
    ,@vApuracao_ptsvp
    ,@vApuracao_mesfch
    ,@vApuracao_anofch
    ,@vApuracao_id_client
    ,@vClients_username

-- Loop. O Fetch_Status retorna os valores 0 [Ok], -1[Falha] e -2 [Registro perdido]
WHILE (@@FETCH_STATUS <> -1)
BEGIN
  /* Tratamentos para geração do Código de barras
  ** Insert into em outra tabela
  **
  */

  -- Passa para o proximo registro, caso seja o ultimo registro da consulta, o @@Fetch_status passa a ser -1
  FETCH Crs_teste 
  -- Insere os valores das linhas nas variáveis
  INTO @vQtd_cupons
      ,@vApuracao_ptsvp
      ,@vApuracao_mesfch
      ,@vApuracao_anofch
      ,@vApuracao_id_client
      ,@vClients_username
END
-- Fecha o cursor
CLOSE Crs_teste
-- Remove a referência do cursor. 
DEALLOCATE Crs_teste



