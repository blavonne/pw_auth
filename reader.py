class Account:
    def __init__(self):
        pass


def acc_reader():
    f = open('passwords', 'r', encoding='utf-8')
    accounts = []
    account = Account()
    i = 0

    for line in f:
        line = line.replace("\r", "")
        line = line.replace("\n", "")

        if i % 2 == 0:
            account.login = line
        else:
            account.password = line
            accounts.append(account)
            account = Account()

        i += 1

    f.close()

    return accounts


def pin_reader():
    f = open('pins', 'r', encoding='utf-8')
    pins = []

    for line in f:
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        pins.append(line)

    f.close()

    return pins


def script_reader(filename):
    f = open(filename, 'r', encoding='utf-8')
    script = f.read()

    f.close()

    return script

