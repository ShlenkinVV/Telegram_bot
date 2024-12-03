FROM python:3.12

WORKDIR /bot

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY run.py run.py
COPY app/ ./app

ENTRYPOINT ["python3", "run.py"]