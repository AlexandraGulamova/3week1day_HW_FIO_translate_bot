FROM python:3.12.6-slim
ENV TOKEN='Token from @BotFather'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","FIO_translate_bot.py"]
