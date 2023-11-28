FROM jupyterhub/jupyterhub

COPY requirements.txt requirements.txt
COPY jupyterhub_config.py jupyterhub_config.py

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["jupyterhub", "-f", "jupyterhub_config.py"]
