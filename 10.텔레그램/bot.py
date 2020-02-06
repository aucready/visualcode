import telepot
import os
import logging
import module
from module import get_dir_list
from module import get_weather


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


TELEGRAM_TOKEN = '1087258823:AAFxn_VmXy8WpyzZaqT6mMWV90frYwf5Row'



def handler(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)

    print(msg)

    if content_type == 'text':
        str_message = msg['text']
        if str_message[0:1] == '/':

            args = str_message.split(' ')
            command = args[0]
            del args[0]

            if command == '/dir':
                filepath = ' '.join(args)

                if filepath.strip() == '':
                   bot.sendMessage(chat_id, '/dir [대상폴더]를 입력하세요')

                else:
                   filelist = module.get_dir_list(filepath)
                   bot.sendMessage(chat_id, filelist)
            elif command == '/weather' or command == '/날씨':
                w = ' '.join(args)
                weather = module.get_weather(w)
                bot.sendMessage(chat_id, weather)
            elif command == '/money' or command == '/환율':
                w = ' '.join(args)
                output = module.money_translate(w)
                bot.sendMessage(chat_id, output)



            elif command[0:4] == '/get':

                filepath = ' '.join(args)
                if os.path.exists(filepath):
                    if command == '/getfile':
                        bot.sendDocument(chat_id, open(filepath, 'rb'))
                    
                    elif command == '/get_iamge':
                        bot.sendPhoto(chat_id, open(filepath, 'rb'))

                    elif command == '/get_audio':
                        bot.sendAudio(chat_id, open(filepath, 'rb'))
    
                    elif command == '/get_video':
                        bot.sendVideo(chat_id, open(filepath, 'rb'))

                else:
                   bot.sendMessage(chat_id, '파일이 존재하지 않습니다.')


# /Users/aucready/path_study
bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)
