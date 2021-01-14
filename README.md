# vk-api-docker-shell

Оболочка для упрощённого доступа к методам vk-api и возможности развертывания скрипта в докере.

Зачем? Чтобы в пару строк и пару кликов появился контейнер с полезной нагрузкой и работющий без отказов.

## Как пользоваться?

1. Создайте функцию с целевым кодом в другом файле

2. Импортируйте её в `main.py` и укажите как target

3. Укажите config_path -- путь к json файлу с данными входа

    * Примеры полей json файла уже есть в нём
    
    * Чтобы конфиденциальные данные не попали на сервера докера. Файл связывается с docker-volume по пути команды запуска. Не забудьте положить его туда.

    * Данные могут различаться в зависимости от задачи. Это обычно логин+пароль, либо токен группы.

4. Укажите нужные поля для конструктора класса

    * auth_type = "user" or "group" -- выбор метода входа

    * one_run = False -- целевая функция while True или запускается лишь один раз

### System

Python 3.7.9

Tested on Windows 10 and Ubuntu 18|16

### Third Party Libraries and Dependencies

The  libraries from requirements.txt must be installed.

For easy windows install just run `create_venv.bat`

### Docker
1. Change PROJECT_NAME for your poject name in dockerfile

2. Build docker container

3. Push&Pull to your host machine. Copy IMAGENAME

4. Run it:

```bash
docker run -d --name PROJECT_NAME --restart always -v /root/PROJECT_NAME/secret/config.json:/PROJECT_NAME/secret/config.json IMAGENAME
```

5. See logs:

```bash
docker logs PROJECT_NAME -follow
```
