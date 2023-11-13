from ..helpers import little_stem
# import little_stem

bangla_days = ["শনিবার", "রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার"]

day_indicator = ["ভোর", "সকাল", "দুপুর", "বেলা", "বিকাল", "বিকেল"]
night_indicator = ["রাত", "সন্ধ্যা"]

vehicle_types = ["মোটরসাইকেল", "সাইকেল", "বাইক", "বাস", "ট্রাক", "কার", "প্রাইভেট কার", "অটোরিকশা", "রিকশা", "রিক্সা", "ট্রেন", "স্কুটার", "গাড়ি", "মাইক্রোবাস", "স্কুটি", "স্কুটার", "মোটর বাইক", "হোণ্ডা"]

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
    matching_words = []
    # for vehicle_type in vehicle_types:
    #     if any(word.startswith(vehicle_type) for word in words):
    #         stemmed_w = little_stem.bengali_stem_ta(little_stem.bengali_stem_ra(word))
    #         vehicles_involved.append(vehicle_type)
            
    for vehicle_type in vehicle_types:
        matching_words.extend([word for word in words if word.startswith(vehicle_type)])

    for word in matching_words: 
        stemmed_w = little_stem.bengali_stem_ta(little_stem.bengali_stem_er(word))
        stemmed_w = stemmed_w.replace("চাপায়", "")
        stemmed_w = little_stem.bengali_stem_ra(stemmed_w)
        
        if stemmed_w in vehicle_types and stemmed_w not in vehicles_involved:
            vehicles_involved.append(stemmed_w)

    return vehicles_involved


# print(get_vehicles("ময়মনসিংহের তারাকান্দা কারের উপজেলার কাশিগঞ্জ বাজারে ট্রাকচাপায় সিএনজিচালিত অটোরিকশার তিনজন যাত্রী মারা গেছেন। ট্রেনটির"))