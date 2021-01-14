# vk-api-docker-shell

Оболочка для упрощённого доступа к методам vk-api и возможности развертывания скрипта в докере.
Зачем? Чтобы в пару строк и пару кликов появился контейнер с полезной нагрузкой и работющий без отказов.

### System

Python 3.7.9

Tested on Windows 10 and Ubuntu 18|16

### Third Party Libraries and Dependencies

The  libraries from requirements.txt must be installed.

For easy windows install just run `create_venv.bat`

### Docker
1. Build docker container

2. Push&Pull to your host machine

3. Run it:

```bash
docker run -d --name vkshell --restart always -v /root/vkshell/secret/config.json:/vkshell/secret/config.json imagename
```

4. See logs:

```bash
docker logs vkshell -follow
```
