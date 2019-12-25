```
docker build . -t aprstg
docker run -e APRS_USER= -e APRS_PASSCODE= -e TELEGRAM_API_KEY="" aprstg
```

send a message to `TGSRV` with your TG group @ name, followed by your message. The bot `aprsisbot` needs to be in the group already.