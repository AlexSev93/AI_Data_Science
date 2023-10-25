class My_str():
    def __init__(self):
        self.my_str = input('my_str')

    def separate(self, n):
        self.my_str_c = self.my_str
        answer = []
        while True:
            if len(self.my_str_c) >= n:
                part = self.my_str_c[0:n]
                answer.append(part)
                self.my_str_c = self.my_str_c[n:]
            elif len(self.my_str_c) == 0:
                break
            else:
                answer.append(self.my_str_c)
                break
        return answer

    def words(self):
        my_str_c = self.my_str
        i = 0
        words = 0
        while True:
            if my_str_c[i] == ' ' and my_str_c[i+1] == ' ':
                my_str_c[i] = my_str_c[:i]+my_str_c[i+1:]
            i = i + 1
            print(my_str_c)

    # 2. сколько слов
    # 3. сколько заглавных букв



x = My_str()
print(x.my_str)
print(x.separate(2))
print(x.words())