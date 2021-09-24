FROM python

WORKDIR /project

COPY . .

CMD pytest test/test_simple.py
