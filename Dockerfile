FROM python:3.6-slim

COPY . /nearest-word
WORKDIR /nearest-word

# install Python modules needed by the Python app
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 1234

# run the application
CMD ["python3", "API.py"]

# CMD ["gunicorn", "-w 2", "API:app"]