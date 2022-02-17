FROM python:3.7-slim

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN /usr/local/bin/python -m pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 