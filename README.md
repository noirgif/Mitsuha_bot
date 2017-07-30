A telegram bot aimed to precisely emulate the ecology of Miyamizu Mitsuha.

Requirements:

    python >=3.6

    pyTelegramBotAPI

    pytz

    ...

How-to:

```
$ mkdir config
$ echo "{'TOKEN':'<your token here>'}" config/token.json
$ python mitsuha.py
```

Features:

Say "/zao@zao_bot" at about 5am Beijing time.

Say "/wan@zao_bot" at about 11pm Beijing time.

(implemented, under test)Reply with a "mua" , a "😘"*randint(1, 3) or a kissing sticker when:

    1. A person showed up after a day of inactivity

    2. A person replying to him/her with the expressions listed above

(implemented)Reply with a "那是你" sticker when:

    1. Somebody says "三爷.*(给|gay)" | "(给|gay).*三爷"


