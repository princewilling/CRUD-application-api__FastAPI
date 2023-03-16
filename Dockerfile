FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update && apt-get install libpq-dev python3-dev -y

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]