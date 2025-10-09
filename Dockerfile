FROM python:3.12-alpine

WORKDIR /MaxToTgBot_main

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /MaxToTgBot_main

CMD ["python", "main.py"]
