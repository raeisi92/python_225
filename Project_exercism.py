

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