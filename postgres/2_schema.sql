-- /postgres_init/2_produtos_schema.sql

-- Cria a tabela 'produtos' no esquema 'public'.
CREATE TABLE public.produtos (
    -- 'SERIAL' cria um ID numérico que se auto-incrementa. 'PRIMARY KEY' garante que ele seja único.
    id SERIAL PRIMARY KEY,
    
    -- Colunas para os dados brutos do produto.
    codigo VARCHAR(30),
    descricao TEXT,
    codigo_barras VARCHAR(30),
    referencia TEXT,
    
    -- Nossa coluna otimizada para busca. Ela armazenará a descrição sem acentos e em maiúsculas.
    descricao_search TEXT
);

-- Cria o índice otimizado do tipo GIN na nossa coluna de busca.
-- Este índice é a chave para que as buscas por similaridade sejam extremamente rápidas.
CREATE INDEX idx_gin_produtos_search 
ON produtos 
USING gin (descricao_search gin_trgm_ops);