from fastapi import FastAPI
from ..models.NewsArticle import NewsArticle, Parameter
from ..helpers.hugface import find_params

# prev_news_articles = [
#     NewsArticle(id=1, title="বরগুনার পাথরঘাটা উপজেলায় মোটরসাইকেল দুর্ঘটনা", content="বরগুনার পাথরঘাটা উপজেলায় থেমে থাকা একটি ট্রাকে ধাক্কা খেয়ে মোটরসাইকেল আরোহী তিন তরুণ মারা গেছেন। পাথরঘাটা উপজেলার রায়হানপুর ইউনিয়নের পূর্ব লেমুয়া গ্রামের লেমুয়া-কাকচিড়া সড়কে সোমবার সন্ধ্যায় এ ঘটনা ঘটে।নিহত তিনজন একে অপরের বন্ধু ছিলেন। তাঁরা হলেন রায়হানপুর ইউনিয়নের জামিরতলা গ্রামের দেলোয়ার হাওলাদারের ছেলে শাকিব হাওলাদার , কাকচিড়া ইউনিয়নের খাসতবক গ্রামের বাবুল হাওলাদারের ছেলে রাকিব হাওলাদার  এবং ওই একই গ্রামের মোহাম্মদ নাসির উদ্দিনের ছেলে মোহাম্মদ তানভীর হোসেন । তাঁরা সবাই সৈয়দ ফজলুল হক ডিগ্রি কলেজের ছাত্র ছিলেন। রায়হানপুর ইউনিয়ন পরিষদের (ইউপি) ৭ নম্বর ওয়ার্ডের সদস্য মঞ্জুরুল আলম এলাকার লোকজনের বরাত দিয়ে বলেন, নিহত তিন তরুণ লেমুয়া ঘুরতে গিয়েছিলেন। সন্ধ্যার পর মোটরসাইকেলে করে তাঁরা লেমুয়া-কাকচিড়া সড়ক দিয়ে এলাকায় ফিরছিলেন। তাঁদের মোটরসাইকেলের গতি বেশি ছিল। পথে স্থানীয় আলমগীর হাওলাদারের বাড়ির সামনে একটি ট্রাক দাঁড়িয়েছিল। তাঁরা অন্ধকারে বিষয়টি বুঝতে পারেননি। ট্রাকের পেছনে সজোরে মোটরসাইকেল ধাক্কা খেলে ঘটনাস্থলেই তাঁরা মারা যান। পরে তাঁদের কাকচিড়া বাজারের মোফাজ্জেল হোসেন হাসপাতালে নিয়ে যাওয়া হলে চিকিৎসক মৃত ঘোষণা করেন।পাথরঘাটা থানার ভারপ্রাপ্ত কর্মকর্তা মো. সাইফুজ্জামান বলেন, বিষয়টি খুবই মর্মাহত। এ ব্যাপারে ঊর্ধ্বতন কর্তৃপক্ষের সঙ্গে আলোচনা করে সিদ্ধান্ত নেওয়া হবে"),
#     NewsArticle(id=2, title="চাঁদপুরের মতলব উত্তর উপজেলায় মোটরসাইকেল দুর্ঘটনা", content="চাঁদপুরের মতলব উত্তর উপজেলায় মোটরসাইকেল নিয়ে ঘুরতে বের হয়ে সড়ক দুর্ঘটনায় এক বন্ধু নিহত হয়েছে। এতে গুরুতর আহত অপর বন্ধু হাসপাতালে চিকিৎসাধীন। গতকাল শনিবার রাতে উপজেলার চরমাছুয়ার বেড়িবাঁধ এলাকায় এ ঘটনা ঘটে। নিহত কিশোরের নাম আশিক মিয়াজী (১৭)। সে চাঁদপুরের মতলব দক্ষিণ উপজেলার পইলপাড়া গ্রামের জাহাঙ্গীর হোসেন মিয়াজীর ছেলে। এ ঘটনায় আহত হয়েছে তার বন্ধু মো. নেছার (১৬)। আশিক ও নেছার একই গ্রামের বাসিন্দা। তারা স্থানীয় একটি কলেজের একাদশ শ্রেণির শিক্ষার্থী। স্বজন ও পুলিশ সূত্রে জানা যায়, কয়েক দিন আগে মোটরসাইকেলটি কিনেছে মো. নেছার। এর আগেও মোটরসাইকেলে করে দুই বন্ধু ঘুরেছে। গতকাল শনিবার রাত ৯টার দিকে দুই বন্ধু মোটরসাইকেলে একসঙ্গে ঘুরতে বের হয়। মোটরসাইকেলটি চালাচ্ছিল নেছার, আর পেছনে বসা ছিল আশিক। তারা মতলব উত্তর উপজেলার চরমাছুয়া এলাকায় বেড়িবাঁধের ওপর পৌঁছালে হঠাৎ নেছার মোটরসাইকেলের নিয়ন্ত্রণ হারায়। মুহূর্তের মধ্যে মোটরসাইকেলটি উল্টে যায়। এতে দুই বন্ধু মোটরসাইকেল থেকে ছিটকে পড়ে। দুজনকে উদ্ধার করে স্থানীয় লোকজন চাঁদপুর জেনারেল হাসপাতালে নিয়ে গেলে কর্তব্যরত চিকিৎসক আশিককে মৃত ঘোষণা করেন। পরে রাতেই নেছারকে উন্নত চিকিৎসার জন্য ঢাকা মেডিকেল কলেজ হাসপাতালে পাঠানো হয়েছে। চিকিৎসকের বরাত দিয়ে নেছারের মা আসমা আক্তার বলেন, তাঁর ছেলের অবস্থা আশঙ্কাজনক। মতলব উত্তর থানার পরিদর্শক (তদন্ত) সানোয়ার হোসেন বলেন, এ ঘটনায় থানায় কোনো অভিযোগ করা হয়নি। পরিবারের অনুরোধে ময়নাতদন্ত ছাড়াই কিশোর আশিকের লাশ দাফনের অনুমতি দেওয়া হয়েছে।"),
#     NewsArticle(id=3, title="সিলেটে ট্রাক-মোটরসাইকেল দুর্ঘটনা", content="সিলেটের গোয়াইনঘাট উপজেলায় দাঁড়িয়ে থাকা একটি ট্রাকের পেছনে মোটরসাইকেলের ধাক্কায় ইউনিয়ন পরিষদের (ইউপি) একজন চেয়ারম্যান ও একজন ব্যবসায়ীর মৃত্যু হয়েছে।গতকাল শনিবার দিবাগত রাত একটার দিকে সিলেট-কোম্পানীগঞ্জ আঞ্চলিক মহাসড়কের গোয়াইনঘাট উপজেলার মিত্রিমহল এলাকায় এই দুর্ঘটনা ঘটে। নিহত ব্যক্তিরা হলেন সিলেট সদর উপজেলার জালালাবাদ ইউপির চেয়ারম্যান ওবায়দুল্লাহ ইসহাক (৩৬) এবং নগরের দরগাহ মহল্লার বাসিন্দা ও ব্যবসায়ী হাফিজুর রশিদ (৩৪)। পুলিশ ও স্থানীয় লোকজনের সঙ্গে কথা বলে জানা গেছে, গতকাল রাতে সিলেট-কোম্পানীগঞ্জ আঞ্চলিক মহাসড়কের সালুটিকর মিত্রিমহল এলাকায় একটি ট্রাক সড়কের পাশে দাঁড়িয়ে ছিল। রাত একটার দিকে সিলেট থেকে কোম্পানীগঞ্জগামী একটি মোটরসাইকেল নিয়ন্ত্রণ হারিয়ে দাঁড়িয়ে থাকা ওই ট্রাকের পেছনে ধাক্কা দেয়। এতে ঘটনাস্থলেই দুই আরোহীর মৃত্যু হয়। গোয়াইনঘাট থানার ভারপ্রাপ্ত কর্মকর্তা (ওসি) কে এম নজরুল ইসলাম বলেন, খবর পেয়ে পুলিশ ঘটনাস্থলে গিয়ে নিহত ব্যক্তিদের লাশ উদ্ধার করে। এরপর লাশ দুটি সিলেট এম এ জি ওসমানী মেডিকেল কলেজ হাসপাতালে পাঠানো হয়। ঘটনাস্থল থেকে ট্রাকটি জব্দ করে পুলিশি হেফাজতে রাখা হয়েছে। নিহত ব্যক্তিদের মরদেহ আইনি প্রক্রিয়া শেষে পরিবারের কাছে হস্তান্তর করা হবে।"),
#     NewsArticle(id=4, title="দেশে পাওয়া হয়েছে নতুন ডাইনোসর", content="দেশে নতুন ডাইনোসরের অববর্ণনা করা হয়েছে, এটি প্রাচীন কালের জীবন্ত কোষগুলির সম্মানিত অংশ।"),
#     NewsArticle(id=5, title="বিশ্বকাপে বাংলাদেশের জয়", content="বাংলাদেশ ক্রিকেট দলের উপর বিশ্বকাপে জয়ের প্রত্যাশা বাড়ছে, প্রস্তুতি চলছে উত্সবের জন্য।"),
#     NewsArticle(id=6, title="বৃষ্টির সময় সাবান প্রয়োজন", content="বৃষ্টির সময় হাত ধোতে সাবানের প্রয়োজন৷ বিশেষজ্ঞরা জনগণের জন্য সাবান ব্যবহার প্রস্তাবনা দিচ্ছে।"),
#     NewsArticle(id=7, title="বাংলাদেশে নতুন প্রধানমন্ত্রী", content="বাংলাদেশে নতুন প্রধানমন্ত্রী নির্বাচিত হয়েছে, দেশের নেতা প্রধানমন্ত্রী হিসেবে প্রশাসন করবেন।"),
#     NewsArticle(id=8, title="বাংলাদেশে সামরিক অবস্থা", content="বাংলাদেশে সামরিক অবস্থার স্থিতি বর্ণনা করা হয়েছে, সেনাবাহিনী প্রস্তুতি নেওয়া হয়েছে সীমান্তে।"),
#     NewsArticle(id=9, title="পর্বত শৃঙ্গে পাওয়া হয়েছে নতুন জীবন", content="পর্বত শৃঙ্গে নতুন জীবনের সংকেত প্রাপ্ত হয়েছে, এই সংবাদের বিষয়টি নিয়ে বিস্তারিত আলোচনা হচ্ছে।"),
# ]

news_articles = [
    NewsArticle(
        title="বরগুনার পাথরঘাটা উপজেলায় মোটরসাইকেল দুর্ঘটনা",
        content="বরগুনার পাথরঘাটা উপজেলায় থেমে থাকা একটি ট্রাকে ধাক্কা খেয়ে মোটরসাইকেল আরোহী তিন তরুণ মারা গেছেন। পাথরঘাটা উপজেলার রায়হানপুর ইউনিয়নের পূর্ব লেমুয়া গ্রামের লেমুয়া-কাকচিড়া সড়কে সোমবার সন্ধ্যায় এ ঘটনা ঘটে।নিহত তিনজন একে অপরের বন্ধু ছিলেন। তাঁরা হলেন রায়হানপুর ইউনিয়নের জামিরতলা গ্রামের দেলোয়ার হাওলাদারের ছেলে শাকিব হাওলাদার , কাকচিড়া ইউনিয়নের খাসতবক গ্রামের বাবুল হাওলাদারের ছেলে রাকিব হাওলাদার  এবং ওই একই গ্রামের মোহাম্মদ নাসির উদ্দিনের ছেলে মোহাম্মদ তানভীর হোসেন । তাঁরা সবাই সৈয়দ ফজলুল হক ডিগ্রি কলেজের ছাত্র ছিলেন। রায়হানপুর ইউনিয়ন পরিষদের (ইউপি) ৭ নম্বর ওয়ার্ডের সদস্য মঞ্জুরুল আলম এলাকার লোকজনের বরাত দিয়ে বলেন, নিহত তিন তরুণ লেমুয়া ঘুরতে গিয়েছিলেন। সন্ধ্যার পর মোটরসাইকেলে করে তাঁরা লেমুয়া-কাকচিড়া সড়ক দিয়ে এলাকায় ফিরছিলেন। তাঁদের মোটরসাইকেলের গতি বেশি ছিল। পথে স্থানীয় আলমগীর হাওলাদারের বাড়ির সামনে একটি ট্রাক দাঁড়িয়েছিল। তাঁরা অন্ধকারে বিষয়টি বুঝতে পারেননি। ট্রাকের পেছনে সজোরে মোটরসাইকেল ধাক্কা খেলে ঘটনাস্থলেই তাঁরা মারা যান। পরে তাঁদের কাকচিড়া বাজারের মোফাজ্জেল হোসেন হাসপাতালে নিয়ে যাওয়া হলে চিকিৎসক মৃত ঘোষণা করেন।পাথরঘাটা থানার ভারপ্রাপ্ত কর্মকর্তা মো. সাইফুজ্জামান বলেন, বিষয়টি খুবই মর্মাহত। এ ব্যাপারে ঊর্ধ্বতন কর্তৃপক্ষের সঙ্গে আলোচনা করে সিদ্ধান্ত নেওয়া হবে",
        source="Example Source",
        link="example.com"
    ),
    NewsArticle(
        title="চাঁদপুরের মতলব উত্তর উপজেলায় মোটরসাইকেল দুর্ঘটনা",
        content="চাঁদপুরের মতলব উত্তর উপজেলায় মোটরসাইকেল নিয়ে ঘুরতে বের হয়ে সড়ক দুর্ঘটনায় এক বন্ধু নিহত হয়েছে। এতে গুরুতর আহত অপর বন্ধু হাসপাতালে চিকিৎসাধীন। গতকাল শনিবার রাতে উপজেলার চরমাছুয়ার বেড়িবাঁধ এলাকায় এ ঘটনা ঘটে। নিহত কিশোরের নাম আশিক মিয়াজী (১৭)। সে চাঁদপুরের মতলব দক্ষিণ উপজেলার পইলপাড়া গ্রামের জাহাঙ্গীর হোসেন মিয়াজীর ছেলে। এ ঘটনায় আহত হয়েছে তার বন্ধু মো. নেছার (১৬)। আশিক ও নেছার একই গ্রামের বাসিন্দা। তারা স্থানীয় একটি কলেজের একাদশ শ্রেণির শিক্ষার্থী। স্বজন ও পুলিশ সূত্রে জানা যায়, কয়েক দিন আগে মোটরসাইকেলটি কিনেছে মো. নেছার। এর আগেও মোটরসাইকেলে করে দুই বন্ধু ঘুরেছে। গতকাল শনিবার রাত ৯টার দিকে দুই বন্ধু মোটরসাইকেলে একসঙ্গে ঘুরতে বের হয়। মোটরসাইকেলটি চালাচ্ছিল নেছার, আর পেছনে বসা ছিল আশিক। তারা মতলব উত্তর উপজেলার চরমাছুয়া এলাকায় বেড়িবাঁধের ওপর পৌঁছালে হঠাৎ নেছার মোটরসাইকেলের নিয়ন্ত্রণ হারায়। মুহূর্তের মধ্যে মোটরসাইকেলটি উল্টে যায়। এতে দুই বন্ধু মোটরসাইকেল থেকে ছিটকে পড়ে। দুজনকে উদ্ধার করে স্থানীয় লোকজন চাঁদপুর জেনারেল হাসপাতালে নিয়ে গেলে কর্তব্যরত চিকিৎসক আশিককে মৃত ঘোষণা করেন। পরে রাতেই নেছারকে উন্নত চিকিৎসার জন্য ঢাকা মেডিকেল কলেজ হাসপাতালে পাঠানো হয়েছে। চিকিৎসকের বরাত দিয়ে নেছারের মা আসমা আক্তার বলেন, তাঁর ছেলের অবস্থা আশঙ্কাজনক। মতলব উত্তর থানার পরিদর্শক (তদন্ত) সানোয়ার হোসেন বলেন, এ ঘটনায় থানায় কোনো অভিযোগ করা হয়নি। পরিবারের অনুরোধে ময়নাতদন্ত ছাড়াই কিশোর আশিকের লাশ দাফনের অনুমতি দেওয়া হয়েছে",
        source="Example Source",
        link="example.com"
    ),
    NewsArticle(
        title="সিলেটে ট্রাক-মোটরসাইকেল দুর্ঘটনা",
        content="সিলেটের গোয়াইনঘাট উপজেলায় দাঁড়িয়ে থাকা একটি ট্রাকের পেছনে মোটরসাইকেলের ধাক্কায় ইউনিয়ন পরিষদের (ইউপি) একজন চেয়ারম্যান ও একজন ব্যবসায়ীর মৃত্যু হয়েছে।গতকাল শনিবার দিবাগত রাত একটার দিকে সিলেট-কোম্পানীগঞ্জ আঞ্চলিক মহাসড়কের গোয়াইনঘাট উপজেলার মিত্রিমহল এলাকায় এই দুর্ঘটনা ঘটে। নিহত ব্যক্তিরা হলেন সিলেট সদর উপজেলার জালালাবাদ ইউপির চেয়ারম্যান ওবায়দুল্লাহ ইসহাক (৩৬) এবং নগরের দরগাহ মহল্লার বাসিন্দা ও ব্যবসায়ী হাফিজুর রশিদ (৩৪)। পুলিশ ও স্থানীয় লোকজনের সঙ্গে কথা বলে জানা গেছে, গতকাল রাতে সিলেট-কোম্পানীগঞ্জ আঞ্চলিক মহাসড়কের সালুটিকর মিত্রিমহল এলাকায় একটি ট্রাক সড়কের পাশে দাঁড়িয়ে ছিল। রাত একটার দিকে সিলেট থেকে কোম্পানীগঞ্জগামী একটি মোটরসাইকেল নিয়ন্ত্রণ হারিয়ে দাঁড়িয়ে থাকা ওই ট্রাকের পেছনে ধাক্কা দেয়। এতে ঘটনাস্থলেই দুই আরোহীর মৃত্যু হয়। গোয়াইনঘাট থানার ভারপ্রাপ্ত কর্মকর্তা (ওসি) কে এম নজরুল ইসলাম বলেন, খবর পেয়ে পুলিশ ঘটনাস্থলে গিয়ে নিহত ব্যক্তিদের লাশ উদ্ধার করে। এরপর লাশ দুটি সিলেট এম এ জি ওসমানী মেডিকেল কলেজ হাসপাতালে পাঠানো হয়। ঘটনাস্থল থেকে ট্রাকটি জব্দ করে পুলিশি হেফাজতে রাখা হয়েছে। নিহত ব্যক্তিদের মরদেহ আইনি প্রক্রিয়া শেষে পরিবারের কাছে হস্তান্তর করা হবে।",
        source="Example Source",
        link="example.com"
    ),
    # Add three more NewsArticle instances with parameters...
    NewsArticle(
        title="টেস্ট ন্যাচুরেলাইজেশন ট্রায়াল",
        content="এটি একটি টেস্ট ন্যাচুরেলাইজেশন ট্রায়াল সম্পর্কে সংক্ষিপ্ত বর্ণনা করে।",
        source="Example Source",
        link="example.com"
    ),
    NewsArticle(
        title="পর্বত শৃঙ্গে পাওয়া হয়েছে নতুন জীবন",
        content="পর্বত শৃঙ্গে নতুন জীবনের সংকেত প্রাপ্ত হয়েছে।",
        source="Example Source",
        link="example.com"
    ),
]

def dummy_news():
    return news_articles 

def get_news_article(article_id: int):
    for news_item in news_articles:
        if news_item.id == article_id:
            # parameters = find_params(news_item.content)
            # processed_news = {
            #     "news": news_item, 
            #     "location": parameters["location"], 
            #     "time": parameters["time"],
            #     "vehicle": parameters["vehicle"],
            #     "dead": parameters["dead"],
            #     "injured": parameters["injured"]
            #     }
            return news_item

    return {"error": f"News item with ID {article_id} not found."}

