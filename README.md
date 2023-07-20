# "Memegenerator" Telegram Bot
![python-version](https://img.shields.io/badge/python-3.9-blue.svg)

A [Telegram bot](https://core.telegram.org/bots/api) that generate memes by your keywords and data. Uses http://apimeme.com/meme

## Prerequisites
- Python 3.9+
- A [Telegram bot](https://core.telegram.org/bots#6-botfather) and its token (see [tutorial](https://core.telegram.org/bots/tutorial#obtain-your-bot-token))

## Getting started

### Configuration
Customize the configuration `token.env`, editing the required parameters as desired:

| Parameter                   | Description                                                                                                                                                                                                                   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TELEGRAM_BOT_TOKEN`            | Your Telegram bot's token, obtained using [BotFather](http://t.me/botfather) (see [tutorial](https://core.telegram.org/bots/tutorial#obtain-your-bot-token))                                                              |



### Installing
Clone the repository and navigate to the project directory:

```shell
git clone https://github.com/wolfhound1995/memegeneratorbot.git
cd memegeneratorbot
```

#### From Source
1. Create a virtual environment:
```shell
python -m venv venv
```

2. Activate the virtual environment:
```shell
# For Linux or macOS:
source venv/bin/activate

# For Windows:
venv\Scripts\activate
```

3. Install the dependencies using `requirements.txt` file:
```shell
pip install -r requirements.txt
```

4. Use the following command to start the bot:
```
python main.py
```
#### Docker manual build
```shell
docker build -t memegeneratorbot .
docker run -it --env-file token.env memegeneratorbot
```

## Credits
- https://pypi.org/project/pyTelegramBotAPI/
- http://apimeme.com/meme

