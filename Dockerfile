FROM python:3.8-slim-buster

# Create a working directory.
RUN mkdir wd

# Copy code
COPY ./src /wd/src
WORKDIR /wd/src

# Install Python dependencies.
RUN pip3 install -r requirements.txt

# Finally, run gunicorn.
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8000", "app:server"]
