-- /postgres_init/4_produtos_post_load.sql

-- Este comando passa por cada linha da tabela 'produtos' e atualiza a coluna 'descricao_search'
-- com o valor da coluna 'descricao', já aplicando a transformação de remover acentos e
-- converter para maiúsculas.
-- Usamos COALESCE(descricao, '') para garantir que, se a descrição for nula, não ocorra um erro.
UPDATE produtos SET descricao_search = UPPER(f_unaccent(COALESCE(descricao, '')));