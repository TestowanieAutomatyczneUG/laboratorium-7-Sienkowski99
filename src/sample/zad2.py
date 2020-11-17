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
