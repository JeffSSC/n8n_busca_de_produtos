-- /postgres_init/1_setup.sql

-- Habilita a extensão para remover acentos de textos.
-- 'IF NOT EXISTS' evita erros se a extensão já estiver instalada.
CREATE EXTENSION IF NOT EXISTS unaccent;

-- Habilita a extensão para calcular a similaridade entre textos (fuzzy search).
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Cria a nossa função "wrapper" que chama a unaccent e se declara como 'IMMUTABLE'.
-- Isso é necessário para que possamos criar um índice sobre a função, o que garante performance.
CREATE OR REPLACE FUNCTION f_unaccent(text)
RETURNS text AS
$func$
SELECT unaccent($1);
$func$  LANGUAGE sql IMMUTABLE;