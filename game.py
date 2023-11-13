import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from btn import *

BOT_TOKEN = "6502882014:AAE31XBkaUL1HrUh4E1Wb7VwmbiGXDdLGQ8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


async def command_menu(dp: Dispatcher):
  await dp.bot.set_my_commands(
    [
      types.BotCommand('start', 'Ishga tushirish'),
    ]
  )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
  await message.answer("Men sizga o'yinlar qidirib beradigan bot man",reply_markup=menu)



@dp.message_handler(text="Pc game")
async def pc_game(message: types.Message):
  await message.answer("Kampyuter o'yinlar",reply_markup=menu_game)



@dp.message_handler(text="GTA 5")
async def pc_game_gta(message: types.Message):
  await message.answer_photo(photo="https://cdn.cloudflare.steamstatic.com/steam/apps/271590/capsule_616x353.jpg?t=1695060909", 
                             caption="""Эта видеоигра понравилась 95% пользователей
Пользователи Google
Grand Theft Auto V — компьютерная игра в жанре action-adventure с открытым миром, разработанная компанией Rockstar North и изданная компанией Rockstar Games. Википедия
Дата выпуска: 17 сентября 2013 г.""")





@dp.message_handler(text="Need for Speed")
async def pc_game_need(message: types.Message):
  await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/ru/thumb/1/15/NFS-Most-Wanted-Front.jpg/274px-NFS-Most-Wanted-Front.jpg", 
                             caption="""ЭПереведено с английского языка.-Need for Speed ​​— это серия гоночных игр, выпущенная Electronic Arts и в настоящее время разрабатываемая Criterion Games, разработчиками Burnout. Википедия (Английский язык)
Оригинал описания""")



@dp.message_handler(text="CS 16")
async def pc_game_contr(message: types.Message):
  await message.answer_photo(photo="https://static.wikia.nocookie.net/counterstrike/images/3/3c/Cs_1.6_background.png/revision/latest?cb=20140922174445&path-prefix=ru", 
                             caption="""ЭЭта видеоигра понравилась 97% пользователей
Пользователи Google
Дата выпуска: 12 сентября 2003 г.""")


@dp.message_handler(text="Cs go 2")
async def pc_game_cs(message: types.Message):
  await message.answer_photo(photo="https://cdn.akamai.steamstatic.com/apps/csgo/images/csgo_react/social/cs2.jpg", 
                             caption="""Эта видеоигра понравилась 63% пользователей
Пользователи Google
Counter-Strike 2 — компьютерная игра в жанре многопользовательского тактического шутера от первого лица, разрабатываемая компанией Valve. Стала 5-й игрой в серии Counter-Strike. Valve анонсировала игру 22 марта 2023 года, объявив, что разработчики готовят релиз на лето 2023 года. Википедия
Дата выпуска: 27 сентября 2023 г.""")


@dp.message_handler(text="Pubg Mobile")
async def pc_game_cs(message: types.Message):
  await message.answer_photo(photo="https://wstatic-prod.pubg.com/web/live/static/og/img-og-pubg.jpg", 
                             caption="""Гейм-дизайнер: Брендан Грин
Разработчики: PUBG Corporation, Krafton, KRAFTON, Inc., Lightspeed & Quantum
Издатели: PUBG Corporation, Krafton, Tencent Games, ЕЩЁ""")











################################## Mobil ################# 






@dp.message_handler(text="Mobile phone")
async def pc_game(message: types.Message):
  await message.answer("Kampyuter o'yinlar",reply_markup=menu_game)



@dp.message_handler(text="GTA 5")
async def pc_game_gta(message: types.Message):
  await message.answer_photo(photo="https://cdn.cloudflare.steamstatic.com/steam/apps/271590/capsule_616x353.jpg?t=1695060909", 
                             caption="""Эта видеоигра понравилась 95% пользователей
Пользователи Google
Grand Theft Auto V — компьютерная игра в жанре action-adventure с открытым миром, разработанная компанией Rockstar North и изданная компанией Rockstar Games. Википедия
Дата выпуска: 17 сентября 2013 г.""")





@dp.message_handler(text="Need for Speed")
async def pc_game_need(message: types.Message):
  await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/ru/thumb/1/15/NFS-Most-Wanted-Front.jpg/274px-NFS-Most-Wanted-Front.jpg", 
                             caption="""ЭПереведено с английского языка.-Need for Speed ​​— это серия гоночных игр, выпущенная Electronic Arts и в настоящее время разрабатываемая Criterion Games, разработчиками Burnout. Википедия (Английский язык)
Оригинал описания""")



@dp.message_handler(text="CS 16")
async def pc_game_contr(message: types.Message):
  await message.answer_photo(photo="https://static.wikia.nocookie.net/counterstrike/images/3/3c/Cs_1.6_background.png/revision/latest?cb=20140922174445&path-prefix=ru", 
                             caption="""ЭЭта видеоигра понравилась 97% пользователей
Пользователи Google
Дата выпуска: 12 сентября 2003 г.""")


@dp.message_handler(text="Cs go 2")
async def pc_game_cs(message: types.Message):
  await message.answer_photo(photo="https://cdn.akamai.steamstatic.com/apps/csgo/images/csgo_react/social/cs2.jpg", 
                             caption="""Эта видеоигра понравилась 63% пользователей
Пользователи Google
Counter-Strike 2 — компьютерная игра в жанре многопользовательского тактического шутера от первого лица, разрабатываемая компанией Valve. Стала 5-й игрой в серии Counter-Strike. Valve анонсировала игру 22 марта 2023 года, объявив, что разработчики готовят релиз на лето 2023 года. Википедия
Дата выпуска: 27 сентября 2023 г.""")


@dp.message_handler(text="Pubg Mobile")
async def pc_game_cs(message: types.Message):
  await message.answer_photo(photo="https://wstatic-prod.pubg.com/web/live/static/og/img-og-pubg.jpg", 
                             caption="""Гейм-дизайнер: Брендан Грин
Разработчики: PUBG Corporation, Krafton, KRAFTON, Inc., Lightspeed & Quantum
Издатели: PUBG Corporation, Krafton, Tencent Games, ЕЩЁ""")





@dp.message_handler(text="Ortga")
async def back_handler(message: types.Message):
    await message.answer(text="Bosh menu", reply_markup=menu)





if __name__ == "__main__":
  executor.start_polling(dp, on_startup=command_menu)