# Vk-api-shell
# Marakulin Andrey @annndruha
# 2021
import os

from shell import shell
from src import frends_avg

# from src import followers_monitor

if __name__ == '__main__':
    # FM = followers_monitor.FollowersMonitor()
    # target = FM.follow
    target = frends_avg.work
    config_path = os.path.join("secret", "config.json")

    shell = shell.Shell(config_path=config_path, target=target, auth_type="user", one_run=True)
    shell.start()
    shell.join()
