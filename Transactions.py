
def withdraw(amount):
    """function to add elements to withdraw text file"""
    tran_list = [amount]
    f = open('withdraw_tran.txt', 'a')
    space = '\n'
    for item in tran_list:
        f.write(item + space)
    f.close()


def deposit(amount):
    """function to add elements to deposit text file"""
    tran_list = [amount]
    f = open('deposit_tran.txt', 'a')
    space = '\n'
    for item in tran_list:
        f.write(item)
    f.close()


def withdraw_net():
    """function sums up elements in withdraw text file"""
    f = open('withdraw_tran.txt', 'r')
    file = f.readlines()

    new_list = []
    for data in file:
        data = data.strip('\n')
        print(data)
        data_2 = float(data)
        new_list.append(data_2)
    return sum(new_list)


def deposit_net():
    """function sums up elements in withdraw text file"""
    f = open('deposit_tran.txt', 'r')
    file = f.readlines()

    new_list = []
    for data in file:
        data = data.strip('\n')
        data_2 = float(data)
        new_list.append(data_2)
    return sum(new_list)



