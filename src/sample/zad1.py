class Hamming:
    def distance(self, a, b):
        if len(a) != len(b):
            raise ValueError('err')
        result = 0
        for i in range(0, len(a)):
            if a[i] != b[i]:
                result += 1
        return result