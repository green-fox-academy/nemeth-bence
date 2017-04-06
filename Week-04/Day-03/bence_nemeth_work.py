class Apple():

    def get_apple(self):
        return "apple"

    def __init__(self, list = []):
        self.list = list

    def get_sum(self):
        number = 0
        for num in self.list:
            number += num
        return number


    def anagram(self, A,B):
        self.A = A
        self.B = B
        for x in A:
            if x in A:
                A[x] += 1
            else:
                A[x] = 1
        return A

        for x in B:
            if x in B:
                B[x] += 1
            else:
                B[x] = 1
        return B
check = Apple()
check.anagram("tok", "fent")

'''def str_to_dict(self, count):
        self.count = count
            count_dic = dic()
            for letter in count:
                if letter not in count_dic:
                    count_dic[letter] = 1
                else:
                    count_dic[letter] += 1
            return count_dic'''
