# Followers bot

### System

Tested on Windows 10 and Ubuntu 18|16
Python 3.7

### Third Party Libraries and Dependencies

The  libraries  from requirements.txt must be installed when using sessiyabot.

### Docker

If you use  docker, you can run bot with this example docker command:

```bash
docker run -d --name followersbot imagename
```

Or this, if you want to keep config data in secret:

```bash
docker run -d --name followersbot --restart always -v /root/followersbot/configvolume.py:/followersbot/data/config.py imagename
```

See logs:

```bash
docker logs followersbot -follow
```
