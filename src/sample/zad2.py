class Checker:
    def ValidPassword(self, given_string):
        specialCharacters = "!@#$%^&*()_+-="
        numbers = "0123456789"
        alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
        if not isinstance(given_string, str):
            raise ValueError('Your password must be a string')
        if len(given_string) < 8:
            return False
        requirements = 3
        for char in specialCharacters:
            if char in given_string:
                requirements -= 1
                break
        for char in numbers:
            if char in given_string:
                requirements -= 1
                break
        for char in alphabet.upper():
            if char in given_string:
                requirements -= 1
                break
        if requirements == 0:
            return True
        else:
            return False

"""
Checks if given_string (password) has meets the requirements.
>>> c = Checker()
>>> c.ValidPassword("halibutZZiemniakamimmmmmmPycha!!!111oneone")
True
>>> c.ValidPassword("HumanistaBeletrysta2137()")
True
>>> c.ValidPassword("HassaN0)")
True
>>> c.ValidPassword("HASLo!23")
True
>>> c.ValidPassword("Haslo123@")
True
>>> c.ValidPassword("haaaaaaaaaaaaaaaa)")
False
>>> c.ValidPassword("!!!!!!!!!!!!!!!!")
False
>>> c.ValidPassword("237942789374892738")
False
>>> c.ValidPassword("haslomalarskie128e")
False
>>> c.ValidPassword("haslo")
False
>>> c.ValidPassword("ARBITER")
False
>>> c.ValidPassword(23)
Traceback (most recent call last):
  File "C:\Python\lib\doctest.py", line 1337, in __run
    compileflags, 1), test.globs)
  File "<doctest __main__.Checker.ValidPassword[11]>", line 1, in <module>
    c.ValidPassword(23)
  File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad2.py", line 33, in ValidPassword
    raise ValueError('Your password must be a string')
ValueError: Your password must be a string
>>> c.ValidPassword(None)
Traceback (most recent call last):
  File "C:\Python\lib\doctest.py", line 1337, in __run
    compileflags, 1), test.globs)
  File "<doctest __main__.Checker.ValidPassword[11]>", line 1, in <module>
    c.ValidPassword(23)
  File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad2.py", line 33, in ValidPassword
    raise ValueError('Your password must be a string')
ValueError: Your password must be a string
>>> c.ValidPassword(False)
Traceback (most recent call last):
  File "C:\Python\lib\doctest.py", line 1337, in __run
    compileflags, 1), test.globs)
  File "<doctest __main__.Checker.ValidPassword[11]>", line 1, in <module>
    c.ValidPassword(23)
  File "C:/Users/Sieniu/studia/testowanie_automatyczne/laboratorium-6-Sienkowski99/src/zad2.py", line 33, in ValidPassword
    raise ValueError('Your password must be a string')
ValueError: Your password must be a string
"""