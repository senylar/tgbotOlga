from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from datetime import datetime as dt

bot = Bot(token='5882345995:AAFBrwJtd7ZYwnxBwUe-raiNhxaZdNsB5GI')
# bot = Bot(token='6177906462:AAE4QbSASTkNdDM_BdcI1CfG_E0up4OSjQs')
dp = Dispatcher(bot)

b1 = "📒Описание Акции"
b2 = '📱Конкурс в соц сетях'
b3 = '❔Как участвовать?'
b4 = '❓Задать вопрос по акции'

button_hi = KeyboardButton(b1)
button_hi2 = KeyboardButton(b2)
button_hi3 = KeyboardButton(b3)
button_hi4 = KeyboardButton(b4)
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_hi, button_hi2).row(button_hi3, button_hi4)
# greet_kb1 = ReplyKeyboardMarkup().add(button_hi).add(button_hi2).add(button_hi3).add(button_hi4)

@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):


    # await bot.send_sticker(msg.chat.id,sticker='CAACAgIAAxkBAAEG3gVjnf9piTtC2JvvVw9Uk0KEWfadbwACYhIAArQxyEs8A3YD_xAHOiwE')
    await bot.send_message(msg.chat.id,"Добро пожаловать!",reply_markup=greet_kb1)

@dp.message_handler()
async def process_start_command(msg: types.Message):

    if msg.text == b1:
        await bot.send_message(msg.chat.id, """Акция действительна для посетителей салонов Kimmy Lab и баров Винный Базар с 1 по 30 июня.

Для всех посетителей салонов Kimmy Lab, которые воспользовались одной из перечисленных услуг, мы дарим сертификат на бокал вина из подборки сети баров Винный Базар. 
Список услуг Kimmy Lab, участвующих в акции:
- Комплекс (руки + ноги) с покрытием и снятием гель-лака
- Комплекс (руки + ноги) с покрытием без снятия 
- Комплекс (руки + ноги) Всё лучшее
- Комплекс Здоровые ногти - (руки + ноги) без покрытия

Для всех посетителей сети баров Винный Базар, которые воспользовались одной из перечисленных услуг, мы дарим сертификат на спа-уход для рук в салонах Kimmy Lab.
Список вин, участвующих в акции:
- Simonsig Kaapse Vonkel Brut
- Conca d'Oro Prosecco Rose Millesimato 2021
- Cava Raimat Brut Nature Chardonnay Xarel-lo
- Herxheim Riesling Sekt Brut
- Cremant d`Alsace AOC Bestheim Brut White

Воспользоваться сертификатом можно 1 раз (на 1 персону).""")

    elif msg.text == b2:
        await bot.send_message(msg.chat.id,  """Для получения бесплатного бокала вина из специальной подборки от "Винный Базар" воспользуйтесь любым Комплексом из подборки сети салонов Kimmy Lab. Запишитесь в любой из салонов в Москве с 1 по 30 июня удобным способом. После процедуры администратор салона даст персональный сертификат, которым вы сможете воспользоваться в сети баров Винный Базар. 

Для получения спа-ухода для рук от Kimmy Lab предлагаем вам приобрести вино из специальной подборки сети баров "Винный Базар" с 1 по 30 июня. После заказа вам дадут персональный сертификат, которым вы сможете воспользоваться в любом из салонов Kimmy Lab.""")

    elif msg.text ==  b3:
        await bot.send_message(msg.chat.id, """Для участия в конкурсе переходите на профили партнеров:
https://instagram.com/vinniy_bazar
https://instagram.com/kimmy.lab""")

    elif msg.text == b4:
        await bot.send_message(msg.chat.id, "https://t.me/Dianaist96")







if __name__ == '__main__':
    executor.start_polling(dp)