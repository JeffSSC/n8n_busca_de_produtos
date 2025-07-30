# Use uma versão específica e leve
FROM postgres:17-alpine

# Recebe a senha de forma segura durante o build
ARG POSTGRES_PASSWORD

# Define as variáveis de ambiente
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

# Copia todos os scripts de inicialização em ordem alfabética
COPY *.sql /docker-entrypoint-initdb.d/

# Expõe a porta
EXPOSE 5432