#!/usr/bin/env python3 
import aprs
import telegram
import os
import sys, traceback

def receive(message):
    try:
        print(message)
        from_call = str(message.source)
        aprs_message = message.info.data.decode('ascii').split(":",2)[2]
        ack = False
        if "{" in aprs_message:
            (text_message, ack) = aprs_message.rsplit("{",1)
        else:
            text_message = aprs_message.rsplit("{",1)[0]
    
        (dest, message) = text_message.split(" ",1)

        tg_message = "[" + from_call + "] : " + message
        if dest[0] != "@":
            dest = "@" + dest

        bot.send_message(chat_id=dest, text=tg_message)
        if ack:
            ack_message = "TGSRV>APRS,TCPIP*::"+from_call+":ack"+str(ack)
            aprsTCP.send(ack_message.encode("ascii"))
            confirm_message = "TGSRV>APRS,TCPIP*::"+from_call+" :Sent to Telegram!"
            aprsTCP.send(confirm_message.encode("ascii"))
        print(dest)
        print(tg_message)
    except:
        try:
            confirm_message = "TGSRV>APRS,TCPIP*::"+from_call+" :Error - is @aprsisbot in group?!"
            aprsTCP.send(confirm_message.encode("ascii"))
        except:
            pass
        traceback.print_exc(file=sys.stdout)    


aprsTCP = aprs.TCP(os.environ['APRS_USER'].encode('utf-8'),os.environ['APRS_PASSCODE'].encode('utf-8'), aprs_filter='g/TGSRV')
bot = telegram.Bot(token=os.environ['TELEGRAM_API_KEY'])
aprsTCP.start()
aprsTCP.receive(callback=receive)
