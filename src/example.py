from shell.shell import timestamp
import requests


def my_function(shell):
    resp = shell.vk.method('friends.get')
    friends = resp["items"]
    user_ids = ",".join(map(str, friends))
    res = shell.vk.method('users.get', {'user_ids': user_ids, 'fields': 'photo_100'})

    for r in res:
        id = r["id"]
        photo_100 = r["photo_100"]
        with open(f'photos//{id}.jpg', 'wb') as handle:
            response = requests.get(photo_100, stream=True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
