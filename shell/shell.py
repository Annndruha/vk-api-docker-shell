import time
import json
import datetime
import threading
import traceback

import vk_api


def timestamp():
    td = datetime.timedelta(hours=3)
    tz = datetime.timezone(td)
    now = datetime.datetime.now(tz)
    return f"[{datetime.datetime.strftime(now, '%d.%m.%Y %H:%M:%S')}]"


class Shell(threading.Thread):
    def __init__(self, target=None, config=None, config_path=None):
        super().__init__()
        self.target = target
        self.config = config
        self.config_path = config_path
        self.vk = None

    def run(self) -> None:
        print("=============== VK-API SHELL STARTING ===============")
        self.auth()
        while True:
            try:
                self.target(self)

            except OSError:
                try:
                    print(f"---{timestamp()} Try to reconnect VK...")
                    self.auth()
                    print(f"---{timestamp()} VK connected successful")
                    time.sleep(1)
                except Exception as err:
                    print(f"---{timestamp()} Exception, description:")
                    print(err)
                    traceback.print_tb(err.__traceback__)
                    time.sleep(10)
            except Exception as err:
                print(f"---{timestamp()} Exception, description:")
                print(err)
                traceback.print_tb(err.__traceback__)
                time.sleep(60)
            print(f"==={timestamp()} VK-API SHELL RESTART")

    def load_tokens(self):
        if self.config is None and self.config_path is None:
            raise Exception("Please, specify config or config_path")
        if self.config_path is not None:
            with open(self.config_path) as f:
                self.config = json.load(f)

    def auth(self):
        self.load_tokens()
        self.vk = vk_api.VkApi(token=self.config["access_token"])
