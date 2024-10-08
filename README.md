# 3week1day_HW_FIO_translate_bot
**Описание Бота**

FIO_translate_bot можно использовать для транслитерации имен написанных на кириллице.

На вход боту необходимо подать .стартовую команду /start

Затем можно ввести имя для последующей транслитерации по правилам [Приказом МИД России от 12.02.2020 № 2113](https://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/)

Ограничения - имя не может начинаться с мягкого знака, из символов отличных от кириллицы бот на вход принимает только пробелы и "-"

**Инструкция по запуску Бота через Docker**

1. Установить [Docker Desktop](https://docs.docker.com/engine/install/) (если не установлен)
2. Создать Бота в @BotFather "/start" -> "/newbot"
3. Сохранить полученную ссылку на Бота и TOKEN
4. Сделать Fork настоящего репозитория в свой профиль
5. Клонировать Fork репозитория на рабочий компьютер
6. Открыть сохраненный "dockerfile" в текстовом редакторе и вместо "Token from @BotFather" указать полученный от @BotFather Token, сохранить
   
   *Дальнейшая инструкция написана для Linux, для прочих систем может отличаться*
7. Из папки, в которой выложен "dockerfile", запустить команду в терминале "docker build ."
8. Проверяем, что образ был успешно создан: "docker images"
9. Если образ был создан, запускаем образ командой "docker run -d -p 80:80 *imageid*" - вместо *imageid* следует указать id образа, полученный на предыдущем этапе (8)
10. Проверяем, был ли успешно создан Docker container: "docker ps"
11. Тестируем работу Бота по ссылке, полученной на этапах 2-3. 

