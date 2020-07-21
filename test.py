arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for i in arr:
    if i % 3 == 0:
        print(i)


#Each number includes a tuple of two numbers. The first number is its "Scalar"
#This allows us to differentiate in our function between seventy two and seventy two thousand
#The second number is the increment, which will be simply added to the number later.
#All "incremental" numbers should have a scalar of 1.
#All "scalar" numbers should have an appropraite scalar and an increment of 0.
#Scalar words must have another word preceding them or they will not be scaled.

#Will error out with numbers that should have combined scalars but do not, like "three hundred fifty two thousand" gets parsed as 52300.
#Or "two hundred and thirty three million" will be parsed as 33,000,200
#but "five hundred thousand" will be correctly parsed as "500,000"
nums = {
    'and': 0,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90}

scalar_words = {
    'dozen': 12,
    'score': 20,
    'hundred': 100,
    'gross': 144,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 1000000000000
}


print("\n\n\n-=-=-\n\n\n")

def parse_num_string(numstr):
    current = 0
    result = 0
    scalar = 1
    for index, word in enumerate(numstr.split()[::-1]):
        if word in scalar_words.keys():
            result += current
            current = 0
            scalar *= scalar_words[word]
        elif (word in nums.keys()) and (scalar > 1):
            try:
                if (numstr.split()[::-1])[index+1] in nums.keys():
                    current += nums[word]
                else: #Scalar or nothing
                    current = (nums[word]+current) * scalar
                    result += current
                    current = 0
                    scalar = 1
            except: #List out of range error above. I know this isn't ideal.
                current = (nums[word] + current) * scalar
                result += current
                current = 0
                scalar = 1
        elif word in nums.keys(): #Should only hit if scalar == 1
            current = current + nums[word]

    return result+current

number_words = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]

for item in number_words:
    if parse_num_string(item) % 3 == 0:
        print(item)




