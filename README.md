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

## Unit testing

To run tests, first switch to production version: `docker-compose up --build dev`.

And then start tests container: `docker-compose up --build tests`.

Tests will automatically re-run when you modify code or tests.

These tests test api responses of dash backend. For that, you need
to describe API request that dash makes to the backend. That is a simple
piece of json. To get an idea what it looks like, use web inspector in
your web browser.

Right click on a web page and select "Inspect Element" or something similiar.
Then select "Network". There, you would be able to see requests that web page
makes. Try clicking some buttons to see if you can intercept some "POST" requests.

Click on one and study "Request" and "Response".

Also see tests provided for examples.

Unfortunately, dash currently doesn't provide official documentation for this API
so you have to learn it by observation.

