FROM python:3.8-slim-buster

# Create a working directory.
RUN mkdir wd

# Copy code
COPY ./ /wd/
WORKDIR /wd

# Install Python dependencies.
RUN pip3 install -r requirements.txt

# Finally, run gunicorn.
CMD [ "ptw" ]
