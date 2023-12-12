FROM python:3.11

WORKDIR /app

### copy files into the container at /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY config.json /app/config.json
COPY data.json /app/data.json
COPY data_handler.py /app/data_handler.py
COPY db_handler.py /app/db_handler.py
COPY main.py /app/main.py

CMD ["python", "/app/main.py"]

