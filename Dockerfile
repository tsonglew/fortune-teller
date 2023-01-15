FROM python:3.9
ADD . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt

WORKDIR /app/src
CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0", "app:app" ]
