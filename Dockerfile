FROM python:3.7

WORKDIR /app

RUN pip install spacy
RUN python -m spacy download en_core_web_sm

COPY program.py /app
COPY input.txt /app

CMD [ "python", "program.py"]