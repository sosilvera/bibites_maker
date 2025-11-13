# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /bibites_maker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 30095
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "30095"]