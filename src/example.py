from shell.shell import timestamp


def my_function(shell):
    print(f"{timestamp()} Congratulations, it's working!\n")

    print("This is example target function or payload of your project.")
    print("An argument is passed to the my_function is class instance of Shell")
    print("It consist vk class object: ")
    print(shell.vk)
    print("for use vk methods like this:\n")

    print("shell.vk.method('users.get', {'user_ids': user_ids, 'fields':'counters'})\n")

    print("@annndruha 2021")
