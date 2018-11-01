##凯撒密码
def code(plain):
                for i in range(len(plain)) :
                        if ord('a') <= ord(chr(plain[i])) <= ord('z'):
                                plain[i]= chr(ord('a') + (ord(plain[i]) + 3 - ord('a')) % 26)
                return plain
