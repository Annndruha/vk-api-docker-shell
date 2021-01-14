import math
import json

def get_friends(shell, id):
    friends = shell.vk.method('friends.get', {'user_id': id})
    items = friends["items"]

    # print(friends)
    #str_friends = str(",".join(list(map(str, items))))
    friends_friends = []
    gets = []
    for i, item in enumerate(items):
        try:
            get = shell.vk.method('users.get', {'user_ids': item, 'fields':'counters'})[0]
            gets.append(get)
            friends_friends.append(get["counters"]["friends"])
            print(i, " ", friends_friends[i])
        except Exception as err:
            print(i, " Error")

    with open('gets.txt', 'w') as outfile:
        json.dump(gets, outfile)

    print("Roman friends:", len(friends))
    print("Avg friends for Roman's friends:", sum(friends_friends) / len(friends_friends))

def work(shell):
    id = 35886154
    get_friends(shell, id)