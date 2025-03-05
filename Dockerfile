# Usar una imagen oficial de Python como base
FROM python:3.12

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias y luego instalar las dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la API al contenedor
COPY . .

# Exponer el puerto en el que se ejecutará la API
EXPOSE 8000

# Comando para ejecutar la API con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]