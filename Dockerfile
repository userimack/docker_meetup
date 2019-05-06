FROM python:latest
ADD web /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
