# Vk-api-shell
# Marakulin Andrey @annndruha
# 2021
import os

from shell import shell
from src import followers_monitor

if __name__ == '__main__':
    FM = followers_monitor.FollowersMonitor()
    target = FM.follow
    config_path = os.path.join("secret", "config.json")

    shell = shell.Shell(config_path=config_path, target=target)
    shell.start()
    shell.join()
