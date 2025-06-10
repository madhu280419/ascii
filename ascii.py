def main():
     s = 'PythonIsCool'
     T = ''
     for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
             if i != 0:
                 T += " "
             T += chr(ord(s[i]))
        else:
             T += s[i]
     print(T)
main()