# Gebruik de officiële Python image als basis
FROM python:3.8-slim

# Voeg metadata toe aan de image
LABEL maintainer="Emile Loosveld <emile.loosveld@student.odisee.be>"

# Zet de werkdirectory in de container
WORKDIR /app

# Kopieer de inhoud van de huidige directory naar de werkdirectory in de container
COPY . .

# Installeer de vereiste bibliotheken voor de Netcat-applicatie
RUN pip install --no-cache-dir netcat

# Commando om de applicatie uit te voeren wanneer de container wordt gestart
CMD ["python", "applicatie.py"]
