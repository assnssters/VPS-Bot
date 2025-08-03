# @ CODE BY TRI GAY & MOT CHUT CHATGPT :))
import telebot, subprocess, psutil, platform, socket, requests, os, ctypes, signal, sys, time
from datetime import datetime

TOKEN = 'TELEGRAM_BOT_ID'
OWNER_ID = YOUR_CHAT_IF

bot = telebot.TeleBot(TOKEN)
PC_NAME = platform.node()
start_time = int(time.time())

now = datetime.now()
formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")


# Gửi cái tin nhắn khi bật bot
def send_start():
    try:
        bot.send_message(OWNER_ID, f"✅ VPS ({PC_NAME}) Đã Online, Bot bật lúc {formatted_time}")
    except: pass





#--------Linux-------#

if platform.system() == "Linux":


 @bot.message_handler(commands=['start', 'help'])
 def send_help(message):
     help_text = (
        "Lệnh có sẵn:\n\n"
         "/tasklist - Hiển thị Process đang chạy\n"
         "/taskls - tasklist mà nhỏ hơn\n"
         "/pcinfo - xem thông tin máy\n"
         "cmd - chạy lệnh\n"
         "cfk - pkg quản lý cơ bản\n"
         "/upload - upload file lên\n"
     )
     bot.reply_to(message, help_text)


 @bot.message_handler(commands=['tasklist'])
 def handle_tasklist(message):
    if platform.system() == "Linux":
        lines = subprocess.getoutput("ps -eo user,pid,time,comm").splitlines()[1:]
        output = ""
        count = 0
        for line in lines:
            parts = line.split(None, 3)
            if len(parts) == 4:
                user, pid, time_used, command = parts
                output += f"User {user} | PID: {pid} | Time: {time_used} | CMD: {command}\n"
                count += 1
                if count >= 20:
                    break
        bot.reply_to(message, f"Task List:\n\n{output}")
    else:
        bot.reply_to(message, "Lỗi không xác định :(")



 @bot.message_handler(commands=['taskls'])
 def handle_tasklist(message):
    if platform.system() == "Linux":
        lines = subprocess.getoutput("ps -eo user,pid,comm").splitlines()[1:]
        output = ""
        count = 0
        for line in lines:
            parts = line.split(None, 3)
            if len(parts) == 3:
                user, pid, command = parts
                command = os.path.basename(command)
                output += f"{user} | {pid} | {command}\n"
                count += 1
                if count >= 20:
                    break
        bot.reply_to(message, f"Task List:\n\n{output}")
    else:
        bot.reply_to(message, "Lỗi không xác định :(")

 @bot.message_handler(commands=['pcinfo'])
 def handle_ramchck(message):
     ram_info = psutil.virtual_memory()
     ip = requests.get('https://ifconfig.me').text
     total_ram_gb = ram_info.total / (1024**3)
     used_ram_gb = ram_info.used / (1024**3)
     cpu_name = subprocess.check_output('lscpu | grep "Model name" | awk -F: "{print $2}" | tr -s " "', shell=True).decode('utf-8').strip()
     cores = subprocess.check_output('nproc --all', shell=True).decode('utf-8').strip()
     response = f"Tên máy: {PC_NAME}\nIP Public: {ip}\nRAM: {used_ram_gb:.2f}/{total_ram_gb:.2f} Gb\n{cpu_name} \nCores: {cores}"
     bot.reply_to(message, response)

 @bot.message_handler(commands=['cmd'])
 def run_cmd(message):
     try:
         command = message.text.replace('/cmd ', '', 1)
         result = subprocess.getoutput(f"bash -c \"{command}\"")
         bot.reply_to(message, f'Kết quả:\n{result[:4000]}')
     except Exception as e:
         bot.reply_to(message, f"Lỗi khi chạy lệnh: {e}")

 @bot.message_handler(commands=['upload'])
 def upload(message):
     path = message.text.replace('/upload ', '', 1).strip()
     url = "https://dro.pm/fileman.php?secret=your_secret"

     if not os.path.isfile(path):
         return bot.reply_to(message, f" Không tìm thấy file: {path}")

     try:
        with open(path, 'rb') as f:
            files = {'f': f}
            headers = {'User-Agent': 'cli'}
            response = requests.post(url, files=files, headers=headers)
            print(response.text)
            result = response.text.split()[1]
            bot.reply_to(message, f"Link: {result}")
     except:
           pass




#----------Windows----------"




if platform.system() == "Windows":

    @bot.message_handler(commands=['start', 'help'])
    def send_help(message):
        help_text = (
            "Lệnh có sẵn:\n\n"
            "/tasklist - Hiển thị Process đang chạy\n"
            "/taskls - tasklist mà nhỏ hơn\n"
            "/pcinfo - xem thông tin máy\n"
            "/cmd - chạy lệnh\n"
            "cfk - pkg quản lý cơ bản"
            "/upload - upload file lên"
        )
        bot.reply_to(message, help_text)

    @bot.message_handler(commands=['tasklist'])
    def handle_tasklist(message):
        try:
            lines = subprocess.getoutput("tasklist /fo csv /nh").splitlines()
            output = ""
            count = 0
            for line in lines:
                parts = line.strip().split('","')
                if len(parts) >= 2:
                    image_name, pid = parts[0].replace('"', ''), parts[1].replace('"', '')
                    output += f"PID: {pid} | CMD: {image_name}\n"
                    count += 1
                    if count >= 20:
                        break
            bot.reply_to(message, f"Task List:\n\n{output}")
        except Exception as e:
            bot.reply_to(message, "Lỗi không xác định :(")

    @bot.message_handler(commands=['taskls'])
    def handle_tasklist_ls(message):
        try:
            lines = subprocess.getoutput("tasklist /fo csv /nh").splitlines()
            output = ""
            count = 0
            for line in lines:
                parts = line.strip().split('","')
                if len(parts) >= 2:
                    image_name, pid = parts[0].replace('"', ''), parts[1].replace('"', '')
                    output += f"{pid} | {image_name}\n"
                    count += 1
                    if count >= 20:
                        break
            bot.reply_to(message, f"Task List:\n\n{output}")
        except Exception as e:
            bot.reply_to(message, "Lỗi không xác định :(")

    @bot.message_handler(commands=['pcinfo'])
    def handle_pcinfo(message):
        try:
            ram_info = psutil.virtual_memory()
            ip = requests.get('https://ifconfig.me').text
            total_ram_gb = ram_info.total / (1024**3)
            used_ram_gb = ram_info.used / (1024**3)
            cpu_name = subprocess.getoutput('powershell "Get-WmiObject -Class Win32_Processor | Select-Object -ExpandProperty Name"').strip()
            cores = psutil.cpu_count(logical=False)
            response = f"Tên máy: {PC_NAME}\nIP Public: {ip}\nRAM: {used_ram_gb:.2f}/{total_ram_gb:.2f} Gb\n{cpu_name} \nCores: {cores}"
            bot.reply_to(message, response)
        except Exception as e:
            bot.reply_to(message, f"Lỗi: {e}")

    @bot.message_handler(commands=['cmd'])
    def run_cmd(message):
        try:
            command = message.text.replace('/cmd ', '', 1)
            result = subprocess.getoutput(f"powershell.exe -Command \"{command}\"")
            bot.reply_to(message, f'Kết quả:\n{result[:4000]}')
        except Exception as e:
            bot.reply_to(message, f"Lỗi khi chạy lệnh: {e}")


    @bot.message_handler(commands=['upload'])
    def upload(message):
        path = message.text.replace('/upload ', '', 1).strip()
        url = "https://dro.pm/fileman.php?secret=your_secret"

        if not os.path.isfile(path):
            return bot.reply_to(message, f" Không tìm thấy file: {path}")

        try:
           with open(path, 'rb') as f:
               files = {'f': f}
               headers = {'User-Agent': 'cli'}
               response = requests.post(url, files=files, headers=headers)
               print(response.text)
               result = response.text.split()[1]
               bot.reply_to(message, f"Link: {result}")
        except:
              pass









if __name__ == '__main__':
    send_start()
    print("✅ Started!")
    bot.polling(none_stop=True)
