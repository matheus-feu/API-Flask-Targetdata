# Apartir do mongo na versão latest
LABEL maintainer="Matheus Feu Soares de Assis - matheusfeu@gmail.com"

# Python versão 3.11
FROM python:3.11

# Instrução para criar o diretório /app dentro do container
WORKDIR /app-flask

# O ARG é usado em tempo de build, para definir variáveis de ambiente
ARG PORT=5000

# Especifica uma variável de ambiente dentro do container
ENV PORT=$PORT

# Por padrão, definir a porta 5000 como a porta exposta
EXPOSE $PORT

# Copiar diretório atual (HOST) para o diretório /app-flask (CONTAINER)
COPY . .

# Executar o comando pip install -r requirements.txt
RUN pip install -r requirements.txt

# Diretiva ENTRYPOINT, especifica o comando que será executado quando o container for iniciado
ENTRYPOINT ["python"]

# Diretiva CMD, especifica os argumentos que serão passados para o comando ENTRYPOINT
CMD ["app.py"]
