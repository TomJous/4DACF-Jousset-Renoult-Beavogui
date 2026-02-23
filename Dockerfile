FROM apache/nifi:2.7.2

USER root

# Installer Python + venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv 

# Créer un virtualenv dédié
RUN python3 -m venv venv

# Installer les librairies dans le venv
RUN venv/bin/pip install --no-cache-dir \
    pandas \
    faker

RUN mkdir -p /scripts && \
    chown -R nifi:nifi /opt/nifi /scripts && \
    chmod +x /opt/nifi/nifi-current/venv/bin/python

USER nifi
