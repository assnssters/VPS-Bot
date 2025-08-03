## HƯỚNG DẨN SỬ DỤNG VPS-BOT ĐỂ ĐIỀU KHIỂN BẰNG BOT TELEGRAM

### Bước 1 Tải các gói cần thiết:
 *  Debian, Ubuntu..
    ```bash
    sudo apt update -y && sudo apt install python3 python3-pip git nano -y
    ```
* Arch Linux
  ```bash
  sudo pacman -Syu && sudo pacman -S git python python-pip nano
  ```
  * Alpine Linux
  ```bash
  sudo apk update && sudo apk add python3 py3-pip nano```
  
### Bước 2 Clone repo này:
```bash
git clone https://github.com/assnssters/VPS-Bot.git```

### Bước 3 cấu hình vào Bot:
```bash
nano VPS-Bot/bot.py
```
rồi tìm đến dòng thứ 3 `TOKEN` và thứ 4 `OWNER_ID`
* Để TOKEN là TOKEN của BOT Telegram
* OWNER_ID là ChatID
  #### Ví dụ
  ```console TOKEN = '7625947522:AAGeun6V3Bve1_-_164CDDFhbyvv0HAxhUX'
OWNER_ID = -1002595785617
```
sau đó Ctrl + X + Y + Enter để lưu lại.
### Bước 3 chạy:
```bash
cd VPS-Bot
```
```bash
python3 bot.py
```


 ## CREDIT:
 * ĐINH ĐỨC TRÍ
 * EMAIL: dinhductri2023@gmail.com
