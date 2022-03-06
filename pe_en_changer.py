# coding=utf-8
eng_alph = (
'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x',
'c', 'v', 'b', 'n', 'm', ',', ' ')
persian = (
'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'ظ', 'ط',
'ز', 'ر', 'ذ', 'د', 'پ', 'و' ,' ')

zipped=dict(zip(eng_alph,persian))
reversed_zip=dict(zip(persian,eng_alph))

print(reversed_zip)

def cahnger(inp,zipped, reversed_zip):
    my_str=""
    if lan_finder(inp) == 'eng':
        for let in inp:
            my_str+= zipped[let]
    else:
        for let in inp:
            my_str+= reversed_zip[let]
    return my_str


def lan_finder(inp):
    if inp[0] in eng_alph:
        return 'eng'
    return 'per'


if __name__ == '__main__':
    print(cahnger(input("your word: "), zipped, reversed_zip))

