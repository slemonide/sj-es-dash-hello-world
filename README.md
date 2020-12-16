# sj-es-dash-hello-world
Hello world example of a Dash dashboard as an external service for simple_jupyterhub

To make your own dashboard:
1. Create a dockerhub account
2. Fork this repository
3. Rename it to whatever you want
4. On GitHub, go to Settings->Secrets, and add two secrets, `DOCKER_USERNAME` and `DOCKER_PASSWORD`, which
would contain your previously registered dockerhub username and password
5. Edit docker image name (line 14, `name:  slemonide/sj-es-dash-hello-world`) in `.github/workflows/publish.yml`,
and replace it with the name of your own dockerhub image.

## Local usage

Install Docker and Docker Compose.

Use `docker-compose up --build dev` to run a local development environment using docker.
This has debug mode enabled and will automatically re-load the page when you edit
dashboard source code.

To try production environment, use `docker-compose up --build prod`.

Open http://localhost:8000/ to access locally running dash dashboard.
