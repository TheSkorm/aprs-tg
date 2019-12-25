```
docker build . -t aprstg
docker run -e APRS_USER= -e APRS_PASSCODE= -e TELEGRAM_API_KEY="" aprstg
```