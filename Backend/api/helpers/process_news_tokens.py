# -*- coding: utf-8 -*-

import banglanltk as bn
from ..helpers import functions

deadfound = False
injuredfound = False
vehiclefound = False
dowfound = False
todfound = False
tod = ""
dow = ""


news = "বরগুনার পাথরঘাটা উপজেলায় থেমে থাকা একটি ট্রাকে ধাক্কা খেয়ে মোটরসাইকেল আরোহী তিন তরুণ মারা গেছেন। পাথরঘাটা উপজেলার রায়হানপুর ইউনিয়নের পূর্ব লেমুয়া গ্রামের লেমুয়া-কাকচিড়া সড়কে সোমবারে সন্ধ্যায় এ ঘটনা ঘটে।নিহত তিনজন একে অপরের বন্ধু ছিলেন। তাঁরা হলেন রায়হানপুর ইউনিয়নের জামিরতলা গ্রামের দেলোয়ার হাওলাদারের ছেলে শাকিব হাওলাদার , কাকচিড়া ইউনিয়নের খাসতবক গ্রামের বাবুল হাওলাদারের ছেলে রাকিব হাওলাদার  এবং ওই একই গ্রামের মোহাম্মদ নাসির উদ্দিনের ছেলে মোহাম্মদ তানভীর হোসেন । তাঁরা সবাই সৈয়দ ফজলুল হক ডিগ্রি কলেজের ছাত্র ছিলেন। রায়হানপুর ইউনিয়ন পরিষদের (ইউপি) ৭ নম্বর ওয়ার্ডের সদস্য মঞ্জুরুল আলম এলাকার লোকজনের বরাত দিয়ে বলেন, নিহত তিন তরুণ লেমুয়া ঘুরতে গিয়েছিলেন। সন্ধ্যার পর মোটরসাইকেলে করে তাঁরা লেমুয়া-কাকচিড়া সড়ক দিয়ে এলাকায় ফিরছিলেন। তাঁদের মোটরসাইকেলের গতি বেশি ছিল। পথে স্থানীয় আলমগীর হাওলাদারের বাড়ির সামনে একটি ট্রাক দাঁড়িয়েছিল। তাঁরা অন্ধকারে বিষয়টি বুঝতে পারেননি। ট্রাকের পেছনে সজোরে মোটরসাইকেল ধাক্কা খেলে ঘটনাস্থলেই তাঁরা মারা যান। পরে তাঁদের কাকচিড়া বাজারের মোফাজ্জেল হোসেন হাসপাতালে নিয়ে যাওয়া হলে চিকিৎসক মৃত ঘোষণা করেন।পাথরঘাটা থানার ভারপ্রাপ্ত কর্মকর্তা মো. সাইফুজ্জামান বলেন, বিষয়টি খুবই মর্মাহত। এ ব্যাপারে ঊর্ধ্বতন কর্তৃপক্ষের সঙ্গে আলোচনা করে সিদ্ধান্ত নেওয়া হবে।" # or you can pass ['সে', 'ঢাকায়', 'থাকে', '।']


def get_time(sentence):
    global dowfound, todfound, dow, tod 
    # words = bn.word_tokenize(sentence)
    # print(sentence)
    # print("")
    dresult, doww = functions.get_week_day(sentence)
    # print(dresult, " ", doww,)

    # Day of Week
    if dresult and not dowfound:
        dowfound = True
        dow = doww
    
    tresult, todd =functions.get_dayornight(sentence)
    # Time of Day
    if tresult and not todfound:
        # print(tresult, " ", todd)
        todfound = True    
        tod = todd

    
def process_news(news, time_from_model):
    global dowfound, todfound, dow, tod
    vehicle1 = ""
    vehicle2 = ""

    sentence_tokens = bn.sent_tokenize(news)

    vehicles = functions.get_vehicles(news)

    if len(vehicles) >= 2:
        vehicle1 = vehicles[0]
        vehicle2 = vehicles[1]
    elif len(vehicles) ==1: 
        vehicle1 = vehicles[0]
        
    # get time from model_time
    get_time(time_from_model)

    modelnotgood = False
    # if time not found from model_time
    if not dowfound or not todfound:
        modelnotgood = True
        for sentence in sentence_tokens:
            get_time(sentence)
            if dowfound and todfound:
                break

    if modelnotgood:
        time_from_model = dow + " " + tod
    
    
    return vehicle1, vehicle2, dow, tod, time_from_model
