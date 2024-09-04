def make_readable(seconds):
    if seconds // 3600 > 99:
        hours = 99
    elif seconds // 3600 < 10:
        hours = f'0{seconds // 3600}'
    else:
        hours = seconds // 3600
    if seconds % 3600 // 60 < 10:
        minutes = f'0{seconds % 3600 // 60}'
    else:
        minutes = seconds % 3600 // 60
    if seconds % 3600 % 60 < 10:
        seconds = f'0{seconds % 3600 % 60}'
    else:
        seconds = seconds % 3600 % 60
    return f'{hours}:{minutes}:{seconds}'


def make_readable2(n):
    return f'{n // 3600:02d}:{n % 3600 // 60:02d}:{n % 60:02d}'


def make_readable3(seconds):
    h = seconds / 60 ** 2
    m = (seconds % 60 ** 2) / 60
    s = (seconds % 60 ** 2 % 60)
    return "%02d:%02d:%02d" % (h, m, s)


def make_readable4(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


if __name__ == '__main__':
    print(make_readable2(11111))
