'''
helper Create by wangxiaoming on 2019/12/26.
'''


def is_isbn_or_key(word):
    '''
    判断查询关键字是否ISBN
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
