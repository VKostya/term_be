FROM python:3.9

WORKDIR /app

RUN apt-get update 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["python", "main.py"]