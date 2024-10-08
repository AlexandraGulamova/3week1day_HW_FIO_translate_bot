FROM python:3.12.6-slim
ENV TOKEN='8199809520:AAH3OWj4fFIX9bigsOhxD-FOdfE9Lo4NHfE'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","FIO_translate_bot.py"]
