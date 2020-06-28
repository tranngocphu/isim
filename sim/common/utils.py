from time import time


def uniqid(prefix=''):
    """Function to generate unique id"""
    return prefix + hex(int(time()))[2:10] + hex(int(time()*1000000) % 0x100000)[2:7]