# Utiliser une image de base Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .
COPY api.py .
COPY models/ ./models/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "api.py"]