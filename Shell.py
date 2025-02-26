# -*- coding: utf-8 -*-
# Coded By @zero0sec
from datetime import datetime
from random import choice, randint
import subprocess
import os
import time

class Shell:
    def __init__(self, language, code, bot_session, chat_id):
        language = language.title()
        if language == "Shell":
            result = self.__Execute__(code)
            if (result[1]) == "":
                if (result[0]) == "":
                    result[0] = "Success !!!"
                result[1] = "NULL"
            elif (result[0]) == "":
                result[0] = "NULL"

            text = f"**==============================**\n**Language : {language}**\n**==============================**\n**Result :**\n\n\n{result[0]}\n**==============================**\n**Error :**\n\n{result[1]}\n**==============================**\n**Time(s) : {result[2]}**\n**==============================**"
            if (len(text)) >= 900:
                file_name = self.__TempFileName__("txt")
                with open(file_name, "w") as f:
                    f.write(text)
                bot_session.send_document(chat_id, file_name)
                os.remove(file_name)
            else:
                bot_session.send_message(chat_id, text)

    def __TempFileName__(self, file_format):
        return ((datetime.now().strftime("%Y%m%d%H%M%S")) + "-" + ("".join([(choice(ascii_letters)) for i in range(randint(10, 20))])) + "." + file_format)

    def __Execute__(self, code, timeout=None):
        start_time = time.time()
        proc = subprocess.Popen(
            [code],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        if timeout is None:
            proc_result, proc_error = proc.communicate(b" ")
        else:
            try:
                proc_result, proc_error = proc.communicate(b" ", timeout=timeout)
            except Exception:
                proc.kill()
                proc_result, proc_error = proc.communicate()

        end_time = time.time()
        proc = [proc_result.decode(), proc_error.decode(), ("%.2f" % (end_time - start_time))]
        return proc
# Coded By @zero0sec
