def string2binary(string):
    return string.encode(encoding='utf-8', errors='strict')


def binary2string(binary):
    return binary.decode(encoding='utf-8', errors='strict')
