<img alt=".srt editor" src="https://i.ibb.co/cFsP1qT/srt-editor.png" width="500" />

# .srt editor

###### A Telegram bot to edit .srt files faster.

## Running

1. Clone the repository:

```bash
git clone https://github.com/shafilm/dot-srt-editor.git
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Copy `example.env` to `.env`.
4. Open `.env` and put your credentials:

   `TOKEN` a bot token from [@BotFather](https://t.me/BotFather).

   `SUPERUSERS` a list of user IDs who can upload files.

   `LANGUAGE` either `en` (for English) or `ckb` (for Kurdish).

   `LOG_CHAT` a chat ID to send errors to.
5. Run the main file:

```bash
python main.py
```

## Usage

1. A super user sends a `.srt` file to the bot.
2. Someone opens it with the `/open` command:

```
/open some_uploaded_file.srt
```

3. The bot will send the lines in that file one by one and the user can send a replacement for it.
4. The file is saved whenever the bot recieves a replacement from the user.

### Other commands

| Command   | Description                                        |
| --------- | -------------------------------------------------- |
| /prev     | moves to the previous line                         |
| /next     | moves to the next line                             |
| /new      | add a new line                                     |
| /line X   | moves to line X                                    |
| /search X | searches for X and returns first 10 results        |
| /empty    | makes the current line empty                       |
| /download | sends the opened file with all of the made edits   |

## 💫️ Credits

- Hama Shareef
- Sivar Mhamad
- Ara Walker
- Roj Serbest
