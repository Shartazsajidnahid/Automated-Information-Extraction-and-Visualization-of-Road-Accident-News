import re


import re

dead_pattern = r"(নিহত|মারা|মৃত|মরণ|অপহত|অন্ত্য|মৃত্যু|প্রাণত্যাগ|ইন্তেকাল)"


def find_ahotonihito_and_number(paragraph, pattern):
  pattern_found = False
  number_found = False
  number = None
  pattern_match = re.search(pattern, paragraph)
  if pattern_match:
    pattern_found = True

  if pattern_found:
    nihito_sentence = paragraph

# টি/টা ছাড়া কাজ করে
    # number_pattern = r'([০-৯]+)(\s*(?:জন| জন))?'
    number_pattern = r'(?<!\()\s*([০-৯]+)\s*(\s*(?:জন| জন))?\s*(?!\))'

# কাজ করীঈঈ
    word_pattern = r"(এক|দুই|তিন|চার|পাঁচ|ছয়|সাত|আট|নয়|দশ)(\s*(?:জন| জন))?(?!\s*[টি|টা])"
    number_match = re.search(number_pattern, nihito_sentence)
    word_match = re.search(word_pattern, nihito_sentence)

    if number_match:
        print(number_match)
        number = remove_jon(number_match.group(0))
        number_found = True
    elif word_match:
          number_found = True
          number = convert_bangla_number_in_words_to_int(word_match.group(0))

  return pattern_found, number_found, number


def convert_bangla_number_in_words_to_int(number_in_words):
    number_in_words = remove_jon(number_in_words)
    bengali_numbers = {
        "এক": 1, "দুই": 2, "তিন": 3, "চার": 4, "পাঁচ": 5, "ছয়": 6, "সাত": 7, "আট": 8, "নয়": 9, "দশ": 10
    }
    return bengali_numbers.get(number_in_words, None)

def remove_jon(number_in_words):
    jon_pattern = r"(জন| জন)+\s*"
    number_in_words = re.sub(jon_pattern, "", number_in_words)
    return number_in_words


paragraph = """
একটি দুর্ঘটনায় ১০ টা দিকে নিহত হয়েছে ।
"""

nihito_found, number_found, number = find_ahotonihito_and_number(paragraph, dead_pattern)
print(find_ahotonihito_and_number(paragraph, dead_pattern))

if nihito_found and number_found:
  print("Number of people killed:", number)  # 1
elif nihito_found and not number_found:
  print("Number of people killed: unknown")
else:
  print("Not found")


def count_occurrences(text):
    keyword = "ও|এবং"
    pattern = rf'\s+(?:{keyword})\s+'
    matches = re.findall(pattern, text)
    if matches:
        return len(matches) 
    else:
        return 0
        
def count_commas(input_string):
    comma_count = input_string.count(',')
    return comma_count


def count_comma_and(string):
  count = count_commas(string) + count_occurrences(string) + 1
  return count