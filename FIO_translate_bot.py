import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import os

TOKEN=os.getenv('TOKEN')
bot=Bot(token=TOKEN)
dp=Dispatcher()


def FIO_translate (fio):
    fio_translated=''
    dict={'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Ъ': 'Ie', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Iaa', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': 'ie', 'э': 'e', 'ю': 'iu', 'я': 'iaa','ь':'', 'Ь':'',' ':' ','-':'-'}
    for i in str(fio):
        if dict.get(i)!=None:
            fio_translated+=dict.get(i)
        else:
            return 'Есть символы помимо кириллицы, попробуйте еще раз'
    return fio_translated
            

logging.basicConfig(level=logging.INFO, filename="mylog.log")
logger=logging.getLogger(__name__)
logger.info("Бот запущен!")

@dp.message(Command(commands=['start']))

async def process_command_start (message: Message):
    user_id=message.from_user.id
    user_name=message.from_user.full_name
    text=f'Привет, {user_name}, введите ФИО для последующей транслитерации'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message (chat_id=user_id, text=text)

@dp.message()
async def fio_translate (message: Message):
    user_id=message.from_user.id
    user_name=message.from_user.full_name
    text=message.text
    logging.info(f'{user_name} {user_id}:{text}')
    text2=FIO_translate(text)
    await message.answer (text=text2)

if __name__=='__main__':
    dp.run_polling(bot)



