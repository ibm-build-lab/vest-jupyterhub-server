import os
from dotenv import load_dotenv

load_dotenv()

c = get_config()  # noqa: F821

# Spawn docker container for each person signing in
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# Use this image: Langchain lab image
c.DockerSpawner.image = os.environ["DOCKER_NOTEBOOK_IMAGE"]

# Connect containers to the Docker network
network_name = os.environ.get("DOCKER_NETWORK_NAME", "jupyterhub-network")
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name

notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jovyan/work")
c.DockerSpawner.notebook_dir = notebook_dir

c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}

# Remove containers once they are stopped
c.DockerSpawner.remove = True

# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

# User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.hub_port = 8080

# Persist hub data on volume mounted inside container
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

# Authenticate users with Native Authenticator
c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

admin = os.environ.get("JUPYTERHUB_ADMIN", "VEST-Admin")
c.Authenticator.admin_users = [admin]

users = os.environ.get('JUPYTERHUB_USERS', "VEST-Admin")
c.Authenticator.allowed_users = users


