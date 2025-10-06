# imagem base
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# instalar dependências do sistema (se necessário)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# copiar e instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# copiar o código da aplicação
COPY . .


EXPOSE 8080

# comando padrão (ajuste o path conforme sua estrutura)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
