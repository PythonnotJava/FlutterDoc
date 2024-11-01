
def batsh_like(path : str):
    file = open(path, 'r', encoding='U8')
    for line in file.readlines():
        cur = line.split('\n')[0]
        if '：' in cur:
            cur = cur.split('：')
        if ': ' in cur:
            cur = cur.split(': ')
        a = ''
        if '.' in cur[0]:
            a = cur[0].split('.')[1]
        if '? ' in cur[0]:
            a = cur[0].split('? ')[1]
        b = cur[1].split('。')[0]
        print('|{} |         |{} |'.format(a, b))

batsh_like('Source/icondata-default.txt')