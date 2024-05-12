'''
ml = [1, 2, 3]

iterator = iter(ml)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

for elem in iterator:
    print(elem)
//////////////////////////////////////////////////////////////////////////////
class Counter:
    def __init__(self, max_num):
        self.i = 0
        self.max_num = max_num

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_num:
            raise StopIteration
        return self.i


count = Counter(5)
print(count.__next__())
print(count.__iter__())
print(next(count))
print(iter(count))
print(next(count))
///////////////////////////////////////////////////////////////////////////////////
def count_up(num, max_degree):
    i = 0
    for _ in range(max_degree):
        yield num**i
        i += 1


res = count_up(2, 10)
print(res)
for _ in res:
    print(_)
////////////////////////////////////////////////////////
class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"I like my {work}"

helper = Helper('teacher')
print(helper("cleaning")
////////////////////////////////////////////////////////

#zd 1
# Реалізувати ітератор для обходу списку слів та виведення їх довжин
class Word:
    def __init__(self, words):
        self.index = 0
        self.words = words

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word, len(word)
        else:
            raise StopIteration

word_list = ["apple", "banana", "orange", "strawberry"]
iterator = Word(word_list)

for word, length in iterator:
    print(f"{word}: {length}")
////////////////////////////////////////////////////////////////////////////////////////////////

#zd2
#Створити ітератор, який генерує послідовність ступенів числа 2 (2^0, 2^1, 2^2...).

class NumDegrees:
    def __init__(self, max_degrees):
        self.max_degrees = max_degrees
        self.degrees = 0

    def __iter__(self):
        self.degrees = 0
        return self

    def __next__(self):
        if self.degrees <= self.max_degrees:
            result = 2 ** self.degrees
            self.degrees += 1
            return result
        else:
            raise StopIteration


iterator = NumDegrees(10)

for num in iterator:
    print(num)

'''

#zd3
#Написати генератор для послідовності ступенів числа 3 (3^0, 3^1, 3^2...).
def count_up(num, max_degree):
    i = 0
    for _ in range(max_degree):
        yield num**i
        i += 1


res = count_up(3, 10)
print(res)
for _ in res:
    print(_)






