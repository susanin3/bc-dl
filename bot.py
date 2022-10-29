import aiogram
from aiogram import types
import logs
import parser
import track

logs.LOGGING = False
bot = aiogram.Bot(token="")
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_cmd(mes: types.Message):
    await mes.answer("Hi! Send me a link to the artist, album or track on the Bandcamp and I'll download it.\n"
                     "Example: https://scowitchboy.bandcamp.com/", disable_web_page_preview=True)


@dp.message_handler(content_types="text")
async def msg_hdlr(mes: types.Message):
    text = mes.text
    if parser.is_url_valid(text):
        await mes.answer("Parsing has started")
        tracks = parser.parse(text)
        t_len = len(tracks)
        if t_len > 0:
            await mes.answer(f"✅Found {str(t_len) + (' track' if t_len == 1 else ' tracks')}.\n⬇The download begins.")
            for i in tracks:
                cont = track.get_url_content(i.get_best_file())
                await mes.answer_audio(audio=cont, caption=i.lyrics, title=f"{i.artist} - {i.title}")
        else:
            await mes.answer(f"❌No tracks found.")
    else:
        await mes.answer(f"❌Link is invalid.")


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
