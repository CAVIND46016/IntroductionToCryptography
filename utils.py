
"""http://stackoverflow.com/questions/38204582/how-to-xor-two-binary-strings-in-python"""
XORLOGIC = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
def xor(x, y):
    return ''.join([XORLOGIC[a, b] for a, b in zip(x, y)])

"""http://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa"""
def ascii2Bin(_str):
    zero_padding = len(_str) * 8;
    return ((bin(int.from_bytes(_str.encode(), 'big'))).replace('b','')).zfill(zero_padding);

def bin2Ascii(_bin):
    n = int(_bin, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode();
    
def hex2Bin(_str):
    zero_padding = len(_str) * 4;    
    return (bin(int(_str, 16))[2:] ).zfill(zero_padding);

"""http://stackoverflow.com/questions/2072351/python-conversion-from-binary-string-to-hexadecimal"""
def bin2Hex(_bin):
    return hex(int(_bin, 2))[2:];
