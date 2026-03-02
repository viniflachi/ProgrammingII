
def is_valid_url(url):
    """
    checks if url is valid
    :param url: string to check
    :return: True if valid URL, False otherwise
    """
    # Rule 1: must start with http:// or https://
    if url[:7] != "http://" and url[:8] != "https://":
        return False

    # Rule 2: must have something after the scheme
    if url[:8] == "https://":
        rest = url[8:]
    else:
        rest = url[7:]

    if len(rest) == 0:
        return False

    # Rule 3: must contain a dot
    if "." not in rest:
        return False

    # Rule 4: must not contain spaces
    if " " in url:
        return False

    # Rule 5: dot cannot be last character
    if url[-1] == ".":
        return False

    return True
print(is_valid_url("https://gemini.google.com/app/f8162ba084302f6b"))
def longest_c_word(book_file):
    """
    Searches for the longest word starting with 'c' in a text file
    :param book_file: The filename of the text file
    :return: the longest word starting with 'c'
    """
    longest = ""                        # tracks longest word found so far
    special_chars = ",?.!;'\""          # characters to strip from words

    with open(book_file, encoding="utf-8") as f:
        for line in f:
            # clean punctuation from each line
            for c in special_chars:
                line = line.replace(c, "")

            words = line.split()        # split line into words

            for word in words:
                word = word.lower()     # case insensitive check
                if word[0] == "c":      # starts with c?
                    if len(word) > len(longest):   # longer than current longest?
                        longest = word  # update longest

    return longest


print(longest_c_word("text.txt"))
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

def days_since_birthday(birthday):
    """
    :param birthday: string in format DD-MM-YYYY
    :return: number of days since birthday (whole years only)
    """
    # Step 1: extract year using slicing
    year = int(birthday[6:10])  # where is YYYY in "DD-MM-YYYY"?

    # Step 2: current year — hint: this must be hardcoded since no imports!
    current_year = 2026

    # Step 3: calculate whole years passed
    years = current_year - year

    # Step 4: multiply by 365
    return years * 365


print(days_since_birthday("25-04-2006"))
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# continue here
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)  # replace with 20-30
    elif random_numbers[i] < 50:
        random_numbers[i] = "XX"                     # replace with XX

print(random_numbers)
word="1414884937242655719669145562427394884141"
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome(word))

a = 16

a = a // 2

print(a**2)

a = a + 11

print(a+1)

a = a - 3
print(a)

print(8 // 3 + 2 * 4)