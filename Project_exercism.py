

1-Say "Hello, World!" With Python

print("Hello, World!")
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
2-Convert a long phrase to its acronym

Acronym
Convert a long phrase to its acronym

def abbreviate(words):
    abbreviation = ""

    words = words.replace("-", " ").replace("_", " ")

    for word in words.split():
        abbreviation += word[0].upper()

    return(abbreviation)
print(abbreviate("The big Man"))
--------------------------------------
3-isogram
def is_isogram(string):
    characters = {}
    for char in string:
        char = char.lower()
        if char.isalpha():
            if char not in characters:
                characters[char] = 1
            else:
                return False
    return True

print(is_isogram("ali raft"))
-----------------------------------------
4 - scor
def score(word):
    alphabet = {'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1, 'L' : 1,
        'N' : 1, 'R' : 1, 'S' : 1, 'T' : 1, 'D' : 2, 'G' : 2, 'B' : 3,
        'C' : 3, 'M' : 3, 'P' : 3, 'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4,
        'Y' : 4, 'K' : 5, 'J' : 8, 'X' : 8, 'Q' : 10, 'Z' : 10}
    return sum(alphabet[char] for char in word.upper())
print(score("Raeisi"))
----------------------------------------
5- leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(is_leap_year(2020))

------------------------------------------------------------
6
#https://exercism.io/tracks/python/exercises/reverse-string

def reverse(text):
    return text[::-1]
print(reverse("mohammad"))
--------------------------------------------------------------
7
#https://exercism.io/tracks/python/exercises/pangram

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return False

    return True
print(is_pangram("The quick brown fox jumps over the lazy dog."))
---------------------------------------------------------------
8
#https://exercism.io/tracks/python/exercises/prime-factors

def prime_factors(num):
	factors = []
	for i in range(2, int(num+1)):
		if num % i == 0:
			factors.append(i)
			num /= i
			break
	if num != 1:
		factors += prime_factors(num)
	return factors

print(prime_factors(60))
------------------------------------
9
#https://exercism.io/tracks/python/exercises/nth-prime

def is_prime(num):
	for n in range(2, num):
		if num % n == 0:
			return False
	else:
		return True

def nth_prime(positive_number):
    if positive_number < 1:
    	raise ValueError("invalid")
    count = 0
    num = 2
    nth = 2
    while ( count < positive_number):
    	if is_prime(num):
    		nth = num
    		count += 1
    	num += 1
    return nth
-------------------------------------------
-------------------------------------------------

#10
#https://exercism.io/tracks/python/exercises/two-fer

def two_for(name = "you"):
    return "One for " + str(name) + ", one for me."


print(two_for())
-------------------------------------------

from datetime import timedelta

------------------------------------------
#11
#https://exercism.io/tracks/python/exercises/difference-of-squares/solutions



def square_of_sum(count):
    return sum(range(count+1))**2

def sum_of_squares(count):
    total = 0
    for i in range(count+1):
        total += i**2
    return total

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)


print(difference(10))
print(square_of_sum(10))
print(sum_of_squares(10))


def add_gigasecond(moment):
    return moment + timedelta(seconds=10 ** 9)


print(add_gigasecond(moment))
------------------------------------------------
12
#https://exercism.io/tracks/python/exercises/series/


def slices(series, length):
    if length <= 0 or length > len(series):
        raise ValueError("Series lenght not correct")

    series_list = []
    for i in range(len(series) - length + 1):
        series_list.append(series[i: i +length])

    return series_list


print(slices("56896", 6))
---------------------------------------------



def sum_of_multiples(limit, multiples):
    return sum(set([m for n in multiples for m in getMultiples(n, limit)]))

def getMultiples(n, limit):v
    if n == 0: return []
    return [n * factor for factor in range(1, limit) if n * factor < limit]
    ---------------------------------------------------------
https://exercism.io/tracks/python/exercises/space-age/
class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self._raw_earth = self.seconds/31557600

    def on_earth(self):
        return round(self._raw_earth, 2)

    def on_mercury(self):
        return round(self._raw_earth/0.2408467, 2)

    def on_venus(self):
        return round(self._raw_earth/0.61519726, 2)

    def on_mars(self):
        return round(self._raw_earth/1.8808158, 2)

    def on_jupiter(self):
        return round(self._raw_earth/11.862615, 2)

    def on_saturn(self):
        return round(self._raw_earth/29.447498, 2)

    def on_uranus(self):
        return round(self._raw_earth/84.016846, 2)

    def on_neptune(self):
        return round(self._raw_earth/164.79132, 2)