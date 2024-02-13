FROM python:3.11.4-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install --no-cache --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]