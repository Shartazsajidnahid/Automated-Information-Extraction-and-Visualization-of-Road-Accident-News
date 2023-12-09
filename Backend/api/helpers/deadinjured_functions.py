# -*- coding: utf-8 -*-
import banglanltk as bn
import re

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

def identify_number(hotahoto_sentence):
  number = None

  number_pattern = r'(?<!\()\s*([০-৯]+)\s*(\s*(?:জন| জন))?\s*(?!\))'
  word_pattern = r"(এক|দুই|দুজন|তিন|চার|পাঁচ|ছয়|সাত|আট|নয়|দশ)(\s*(?:জন| জন))?(?!\s*[টি|টা|ই])"

  number_match = re.search(number_pattern, hotahoto_sentence)
  word_match = re.search(word_pattern, hotahoto_sentence)

  if number_match:
      number = remove_jon(number_match.group())
  elif word_match:
      number = convert_bangla_number_in_words_to_int(remove_jon(word_match.group()))

  if number:
      return int(number)
  return number

def convert_bangla_number_in_words_to_int(number_in_words):
    number_in_words = remove_jon(number_in_words)
    bengali_numbers = {
        "এক": 1, "দুই": 2, "দু": 2, "তিন": 3, "চার": 4, "পাঁচ": 5, "ছয়": 6, "সাত": 7, "আট": 8, "নয়": 9, "দশ": 10
    }
    return bengali_numbers.get(number_in_words, None)

def remove_jon(number_in_words):
    jon_pattern = r"(জন| জন)+\s*"
    number_in_words = re.sub(jon_pattern, "", number_in_words)
    return number_in_words

def find_from_model(hotahoto_sentence):
  number = identify_number(hotahoto_sentence)
  if number:
      return number
  else:
      count_number = count_comma_and(hotahoto_sentence)
      if count_number:
          return count_number
      else:
          return 0

def find_sentences_with_keyword(content, keyword_set):
    pattern = r'[।?]'
    sentences = re.split(pattern, content)
    sentences = [s.strip() for s in sentences if s.strip()]

    sentences_with_keyword = []
    for string in sentences:
        # print(string)
        if any(keyword in string for keyword in keyword_set):
            sentences_with_keyword.append(string)
    return sentences_with_keyword

def arow_present(sentence):
    arow_words = ["আরও", "আরো", "অপর", "অন্য"]
    return any(string in sentence for string in arow_words)

def find_from_content(content, keyword_set):
    sentences_with_keyword = find_sentences_with_keyword(content, keyword_set)
    count = 0
    for sen in sentences_with_keyword:
        print(sen)
        if "আরেকজন" in sen:
            count +=1
        else:
          number = identify_number(sen)
          if number and (number!=count or arow_present(sen)):
              count += number
        
        print("count: ", count)
    return count

def set_keyword(deadorinjured):
  dead_terms = ["নিহত", "মারা", "মৃত", "মরণ", "অপহত", "অন্ত্য", "মৃত্যু", "প্রাণত্যাগ", "ইন্তেকাল", "প্রাণ হার"]
  injured_terms = ["আহত"]

  if deadorinjured == "নিহত":
      keyword_set = set(dead_terms)
  elif deadorinjured == "আহত":
      keyword_set = set(injured_terms)
  return keyword_set

def check_presence(content, keyword_set):
  for keyword in keyword_set:
      if keyword in content:
          return True
  return False

def find_dead_injured(content, deadorinjured, model_answer, other_answer):
    keyword_set = set_keyword(deadorinjured)

    if not check_presence(content,keyword_set):
        return 0

    if model_answer == other_answer:
        return find_from_content(content, keyword_set)
    else:
        return find_from_model(model_answer)

# str = "ঢাকার ধামরাইয়ে সেলফি পরিবহনের দুটি বাসের রেষারেষির সময় বাসচাপায় ৬জন নিহত হয়েছেন। পরে  জন নিহত। একই সময় আহত হয়েছেন আরও ছয়জন। আজ বৃহস্পতিবার সকাল সাড়ে ৮টার দিকে ঢাকা-আরিচা মহাসড়কের ধামরাই থানা বাসস্ট্যান্ডে এ দুর্ঘটনা ঘটে।"
# find_dead_injured(str, "নিহত", "আরও একজন", "আরও একজন")