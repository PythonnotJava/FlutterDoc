
def batsh_like(path : str):
    file = open(path, 'r', encoding='U8')
    for line in file.readlines():
        cur = line.split('\n')[0]
        if '：' in cur:
            cur = cur.split('：')
        elif ': ' in cur:
            cur = cur.split(': ')
        a = cur[0]
        b = cur[1].split('。')[0]
        print('|{} |         |{} |'.format(a, b))

batsh_like('Animation/animationswitcher-default.txt')