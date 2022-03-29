FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY requirements /code/requirements

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

EXPOSE 5001

CMD ["uvicorn", "src.main:app", "--reload", "--port", "5001"]