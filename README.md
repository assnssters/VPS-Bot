## HƯỚNG DẨN SỬ DỤNG VPS-BOT ĐỂ ĐIỀU KHIỂN BẰNG BOT TELEGRAM


## Linux
### Bước 1 Tải các gói cần thiết:
 *  Debian, Ubuntu..
    ```bash
    sudo apt update -y && sudo apt install python3 python3-pip git nano -y
    ```
* Arch Linux
* 
  ```bash
  sudo pacman -Syu && sudo pacman -S git python python-pip nano
  ```
* Alpine Linux
* 
  ```bash
  sudo apk update && sudo apk add python3 py3-pip nano
  ```
  
### Bước 2 Clone repo này:

```bash
git clone https://github.com/assnssters/VPS-Bot.git
```
#### Tải Modules cần thiết

```bash
pip3 install -r VPS-Bot/requirements.txt
```
### Bước 3 cấu hình vào Bot:


```bash
nano VPS-Bot/bot.py
```


rồi tìm đến dòng thứ 3 `TOKEN` và thứ 4 `OWNER_ID`
* Để TOKEN là TOKEN của BOT Telegram
* OWNER_ID là ChatID
#### Ví dụ

```bash
TOKEN = '7625947522:AAGeun6V3Bve1_-_164CDDFhbyvv0HAxhUX'
OWNER_ID = -1002595785617
```

sau đó Ctrl + X + Y + Enter để lưu lại.
### Bước 4 chạy:

```bash
cd VPS-Bot
```

```bash
python3 bot.py
```

## Windows
### Bước 1 tải:
Tải [Python](https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe) về VPS
### Bước 2 tải repo, giải nén, tải Modules: 
Tải [repo này dưới dạng zip](https://github.com/assnssters/VPS-Bot/archive/refs/heads/main.zip) và giải nén ra thư mục, mở cmd ở đây hoặc mở cmd ( Run As Administrator) sau đó chạy ` cd <Thư mục vừa giải nén>/VPS-Bot-main `  và  `pip3 install -r requirements.txt`
### Bước 3 Cấu hình vào bot:
Edit cái bot.py và làm như bên Linux rồi save lại, sau đó ấn vào bot.py python để run

 ## CREDIT:
 * ĐINH ĐỨC TRÍ
 * EMAIL: dinhductri2023@gmail.com
 ## NOTE:
- Bài học rút ra: làm cái này hao mòn Tay tay vãi :)))
- Đang buồn ngủ mà viết README bị skibidi mong thông cảm 😭
