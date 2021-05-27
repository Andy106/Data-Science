FROM python:3

COPY . .

CMD [ "python", "src/test_script.py" ]