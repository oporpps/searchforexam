FROM python:3.9


WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

EXPOSE 5000

CMD [ "python", "server.py" ]