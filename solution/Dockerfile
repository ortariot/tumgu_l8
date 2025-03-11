FROM python:3.13

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY ./requirements.txt /app/requirements.txt
# COPY ./ /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
     

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

ENTRYPOINT [ "python", "main.py"]



