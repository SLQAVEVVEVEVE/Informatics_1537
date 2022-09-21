


def newsys(num, base):
    new_num = ''

    while num > 0:
        new_num = str(num % base) + new_num
        num //= base

    return new_num
