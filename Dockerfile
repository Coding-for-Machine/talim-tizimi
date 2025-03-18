FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt  # Typo to'g'rilandi: 'requirments.txt' -> 'requirements.txt'

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.app.wsgi:application"]

