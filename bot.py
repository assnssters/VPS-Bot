import telebot
import subprocess
import psutil
import platform
import requests
import os
import time
from datetime import datetime

TOKEN = 'TELE_BOT_TOKEN'
OWNER_ID = CHATID
PC_NAME = platform.node()
bot = telebot.TeleBot(TOKEN)
start_time = time.time()

def send_start_message():
    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    message_text = f"✅ VPS ({PC_NAME}) Đã Online, Bot bật lúc {formatted_time}"
    try:
        bot.send_message(OWNER_ID, message_text)
    except:
        pass

def is_old_message(message):
    return message.date < start_time

@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    if is_old_message(message): return
    help_text = "Lệnh có sẵn:\n\n/tasklist\n/taskls\n/pcinfo\n/cmd\n/upload"
    bot.reply_to(message, help_text)

#-Linud

if platform.system() == "Linux":
    @bot.message_handler(commands=['tasklist'])
    def handle_tasklist_linux(message):
        if is_old_message(message): return
        try:
            lines = subprocess.getoutput("ps -eo user,pid,time,comm").splitlines()[1:]
            output = "\n".join(lines[:20])
            bot.reply_to(message, f"Task List:\n\n{output}")
        except:
            bot.reply_to(message, "Lỗi")

    @bot.message_handler(commands=['taskls'])
    def handle_taskls_linux(message):
        if is_old_message(message): return
        try:
            lines = subprocess.getoutput("ps -eo user,pid,comm").splitlines()[1:]
            output = "\n".join(lines[:20])
            bot.reply_to(message, f"Task List:\n\n{output}")
        except:
            bot.reply_to(message, "Lỗi")

    @bot.message_handler(commands=['pcinfo'])
    def handle_pcinfo_linux(message):
        if is_old_message(message): return
        try:
            ram_info = psutil.virtual_memory()
            ip = requests.get('https://ifconfig.me').text
            total_ram_gb = ram_info.total / (1024**3)
            used_ram_gb = ram_info.used / (1024**3)
            cpu_name = subprocess.check_output('lscpu | grep "Model name" | awk -F: "{print $2}" | tr -s " "', shell=True).decode('utf-8').strip()
            cores = psutil.cpu_count(logical=False)
            response = f"Tên máy: {PC_NAME}\nIP Public: {ip}\nRAM: {used_ram_gb:.2f}/{total_ram_gb:.2f} Gb\nCPU: {cpu_name}\nCores: {cores}"
            pmcode = f"```\n{response}\n```"
            bot.reply_to(message, pmcode, parse_mode='Markdown')
        except:
            bot.reply_to(message, "Lỗi")

    @bot.message_handler(commands=['cmd'])
    def run_cmd_linux(message):
        if is_old_message(message): return
        try:
            command = message.text.replace('/cmd ', '', 1)
            result = subprocess.getoutput(f"bash -c \"{command}\"")
            bot.reply_to(message, f'Kết quả:\n{result[:4000]}')
        except:
            bot.reply_to(message, "Lỗi")


    @bot.message_handler(commands=['upload'])
    def upload_file_to_telegram(message):
        try:
            if message.date < start_time:
                return
            file_path = message.text.replace('/upload', '', 1).strip()
            if not file_path:
                bot.reply_to(message, "⚠️ Vui lòng cung cấp đường dẫn file để tải lên, ví dụ: `/upload results.txt`")
                return
            if not os.path.exists(file_path):
                bot.reply_to(message, f"❌ Không tìm thấy file: `{file_path}`")
                return
            with open(file_path, 'rb') as doc:
                bot.send_document(message.chat.id, doc, caption=f"✅ File đã tải lên từ:\n`{file_path}`")
        except Exception as e:
            bot.reply_to(message, f"Lỗi: {e}")

    @bot.message_handler(commands=["cfk"])
    def cfk_handler(message):
        try:
            bot.reply_to(message, "Chỉ cho Windows")
        except: pass





#-Windows



elif platform.system() == "Windows":
    @bot.message_handler(commands=['tasklist'])
    def handle_tasklist_windows(message):
        if is_old_message(message): return
        try:
            lines = subprocess.getoutput("tasklist /fo csv /nh").splitlines()
            output = "\n".join(lines[:20])
            bot.reply_to(message, f"Task List:\n\n{output}")
        except:
            bot.reply_to(message, "Lỗi")

    @bot.message_handler(commands=['taskls'])
    def handle_taskls_windows(message):
        if is_old_message(message): return
        try:
            lines = subprocess.getoutput("tasklist /fo csv /nh").splitlines()
            output = "\n".join(lines[:20])
            bot.reply_to(message, f"Task List:\n\n{output}")
        except:
            bot.reply_to(message, "Lỗi")

    @bot.message_handler(commands=['pcinfo'])
    def handle_pcinfo_windows(message):
        if is_old_message(message): return
        try:
            ram_info = psutil.virtual_memory()
            ip = requests.get('https://ifconfig.me').text
            total_ram_gb = ram_info.total / (1024**3)
            used_ram_gb = ram_info.used / (1024**3)
            cpu_name = subprocess.getoutput('powershell "Get-WmiObject -Class Win32_Processor | Select-Object -ExpandProperty Name"').strip()
            cores = psutil.cpu_count(logical=False)
            response = f"Tên máy: {PC_NAME}\nIP Public: {ip}\nRAM: {used_ram_gb:.2f}/{total_ram_gb:.2f} Gb\nCPU: {cpu_name}\nCores: {cores}"
            pmcode = f"```\n{response}\n```"
            bot.reply_to(message, pmcode, parse_mode='Markdown')
        except:
            bot.reply_to(message, "Lỗi")

    @bot.message_handler(commands=['cmd'])
    def run_cmd_windows(message):
        if is_old_message(message): return
        try:
            command = message.text.replace('/cmd ', '', 1)
            result = subprocess.getoutput(f"cmd /c \"{command}\"")
            bot.reply_to(message, f'Kết quả:\n{result[:4000]}')
        except:
            bot.reply_to(message, "Lỗi")



    @bot.message_handler(commands=['upload'])
    def upload_file_to_telegram(message):
        try:
            if message.date < start_time:
                return
            file_path = message.text.replace('/upload', '', 1).strip()
            if not file_path:
                bot.reply_to(message, "⚠️ Vui lòng cung cấp đường dẫn file để tải lên, ví dụ: `/upload results.txt`")
                return
            if not os.path.exists(file_path):
                bot.reply_to(message, f"❌ Không tìm thấy file: `{file_path}`")
                return
            with open(file_path, 'rb') as doc:
                bot.send_document(message.chat.id, doc, caption=f"✅ File đã tải lên từ:\n`{file_path}`")
        except Exception as e:
            bot.reply_to(message, f"Lỗi: {e}")



    @bot.message_handler(commands=["cfk"])
    def cfk_handler(message):
        try:
            data = requests.get("https://raw.githubusercontent.com/assnssters/cfk-pkgmgr/refs/heads/main/repo.json").json()
        except:
            bot.reply_to(message, "Failed to fetch package list.")
            return

        parts = message.text.strip().split()
        if len(parts) == 2 and parts[1] == "list":
            pkgs = "\n".join(data.keys())
            bot.reply_to(message, pkgs)
        elif len(parts) == 3 and parts[1] == "install":
            pkg = parts[2]
            if pkg not in data:
                bot.reply_to(message, f"Package not found: {pkg}")
                return
            info = data[pkg]
            url = info["url"]
            cmd = info["install_cmd"]
            filename = url.split("/")[-1]
            try:
                r = requests.get(url)
                open(filename, "wb").write(r.content)
                subprocess.run([filename] + cmd.split(), shell=True)
                bot.reply_to(message, f"Đã tải gói: {pkg}")
                os.remove(filename)
            except Exception as e:
                bot.reply_to(message, f"Tải gói lỗi:: {e}")
        else:
            bot.reply_to(message, "Sử dụng:\n/cfk list\n/cfk install <package>")


if __name__ == '__main__':
    send_start_message()
    print("✅ Started!")
    bot.polling(none_stop=True)
