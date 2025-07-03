# Use uma imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

## Copia os arquivos da aplicação para o container
COPY . .

## Instala o FastAPI e o servidor Uvicorn
RUN pip install -r requirements.txt
#
## Expõe a porta usada pelo Uvicorn
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
