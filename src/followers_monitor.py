import time

from vk_api.utils import get_random_id


class FollowersMonitor:
    def __init__(self):
        super().__init__()
        self.vk = None
        self.shell = None
        self.members_ids = None

    def follow(self, shell):
        self.shell = shell
        self.vk = shell.vk
        self.get_members()
        while True:
            self.update_members()
            time.sleep(5)

    def user_get(self, user_id):
        return self.vk.method('users.get', {'user_ids': user_id})

    def write_msg(self, user_id, message=None, attach=None, parse_links=False):
        params = {'user_id': user_id, 'random_id': get_random_id()}

        if message is not None and attach is not None:
            params['message'] = message
            params['attachment'] = attach
        elif message is not None and attach is None:
            params['message'] = message
        elif message is None and attach is not None:
            params['attachment'] = attach
        if not parse_links:
            params['dont_parse_links'] = 1
        self.vk.method('messages.send', params)

    def get_members(self):
        group_id = self.shell.config["group_id"]
        members = self.vk.method('groups.getMembers', {'group_id': group_id})
        self.members_ids = members['items']

    def update_members(self):
        group_id = self.shell.config["group_id"]
        admin_id = self.shell.config["admin_id"]
        members = self.vk.method('groups.getMembers', {'group_id': group_id})
        members_ids = members['items']

        lost_members = list(set(self.members_ids) - set(members_ids))
        new_members = list(set(members_ids) - set(self.members_ids))

        for lost_member in lost_members:
            user = self.user_get(lost_member)
            user_name = (user[0])['first_name'] + ' ' + (user[0])['last_name']
            message = f'&#10006; Отписался: [id{lost_member}|{user_name}]\nЧисло подписчиков: {len(members_ids)}'
            self.write_msg(admin_id, message)

        for new_member in new_members:
            user = self.user_get(new_member)
            user_name = (user[0])['first_name'] + ' ' + (user[0])['last_name']
            message = f'&#10133; Подписался: [id{new_member}|{user_name}]\nЧисло подписчиков: {len(members_ids)}'
            self.write_msg(admin_id, message)
        self.members_ids = members_ids
