bangla_days = ["শনিবার", "রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার"]

day_indicator = ["ভোর", "সকাল", "দুপুর", "বেলা", "বিকাল", "বিকেল"]
night_indicator = ["রাত", "সন্ধ্যা"]

vehicle_types = ["মোটরসাইকেল", "সাইকেল", "বাইক", "বাস", "ট্রাক", "কার", "প্রাইভেট কার", "অটোরিকশা", "রিকশা", "রিক্সা", "মিনি বাস", "ট্রেন", "স্কুটার", "গাড়ি", "মাইক্রোবাস", "স্কুটি", "স্কুটার", "মোটর বাইক", "হোণ্ডা"]

def get_week_day(sentence):
    for day in bangla_days:
        if day in sentence:
            return {"result": True, "dow": day}
    return {"result": False, "dow": ""}
    
def get_dayornight(sentence):
    words = sentence.split()

    for pattern in day_indicator:
        if any(word.startswith(pattern) for word in words):
        # if pattern in sentence:
            return {"result": True, "tod": "দিন"}

    for pattern in night_indicator:
        if any(word.startswith(pattern) for word in words):
        # if pattern in sentence:
            # print(pattern )
            # print(sentence)
            return {"result": True, "tod": "রাত"}

    return {"result": False, "tod": ""}

def get_vehicles(news_article):
    vehicles_involved = []
    words = news_article.split()

    for vehicle_type in vehicle_types:
        if any(word.startswith(vehicle_type) for word in words):
            vehicles_involved.append(vehicle_type)
    
    return vehicles_involved

# def get_dayornight(sentence):
    # if sentence.endswith("য়"):  # সন্ধ্যায়
    #     sentence = sentence[:-1]

    # if re.search(day_pattern, sentence):
    #     return {"result": True, "tod": "দিন"}

    # if re.search(night_pattern, sentence):
    #     return {"result": True, "tod": "রাত"}

    # return {"result": False, "tod": ""}