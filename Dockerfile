# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho na imagem
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o servidor
CMD ["python3", "app.py"]
