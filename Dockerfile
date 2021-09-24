FROM python

WORKDIR /project

COPY . .

CMD RUN pip install --no-cache-dir -r requirements.txt
CMD pytest test/test_simple.py
