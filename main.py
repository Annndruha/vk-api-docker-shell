# Vk-api-shell
# Marakulin Andrey @annndruha
# 2021
import os

from shell import shell
from src.followers_monitor import FollowersMonitor

if __name__ == '__main__':
    FM = FollowersMonitor()
    target = FM.follow
    config_path = os.path.join("secret", "config.json")
    auth_type = "user"
    one_run = False

    shell = shell.Shell(config_path=config_path, target=target, auth_type=auth_type, one_run=one_run)
    shell.start()
    shell.join()
