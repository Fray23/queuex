FROM python:3.13-alpine3.22
RUN mkdir code
WORKDIR code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "/code/app/main.py", "--port", "8000"]


