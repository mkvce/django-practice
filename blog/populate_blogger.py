import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'blog.settings')

import django
django.setup()
from blogger.models import Article, Author

def populate():
    fars_articles = [
    {'title': "قفل‌ها در این دولت نه تنها باز نشد بلکه بیشتر هم شد",
     'brief': "دبیرکل جامعه اسلامی مدیران گفت: درنتیجه سو مدیریت‌ها در مردم نوعی بی‌اعتمادی به دولتمردان بوجود آمده و نه تنها قفل‌ها باز نشد بلکه بر قفل‌ها افزوده شد. ",
     'text': """به گزارش خبرنگار حوزه احزاب خبرگزاری فارس، محمد ناظمی اردکانی دبیرکل جامعه اسلامی مدیران عصر امروز(دوشنبه) در آیین رونمایی از برنامه و نقشه راه دولت مردمی و تحول‌گرا که توسط این تشکل تدوین شده است، گفت: انقلاب اسلامی بزرگترین حادثه قرن بود که جهان امروز و دولت‌های مسلط بر جهان را به چالش کشید.

وی با بیان اینکه بیش از ۴ دهه از پیروزی انقلاب اسلامی می گذرد، گفت: در بیانیه گام دوم فراز و فرودهای ۴ دهه ترسیم شده است. در سال‌های گذشته از ظرفیت‌های کم نظیر این بیانیه استفاده نشد و بسیاری از مشکلات، ناشی از عدم استفاده از این ظرفیت هاست و این مسئله به بسیاری از ظرفیت های انقلاب خدشه وارد کرد.

ناظمی اردکانی افزود: دانش هسته‌ای این امروز یک رکن قدرت برای کشورهاست اما به بهانه ترمیم معیشت مردم با قدرت‌های مسلط جهان باب مذاکره گشوده شد که نتیجه آن نه‌تنها بهبود اقتصادی نبود بلکه همه دستاوردهای ما در حوزه هسته ای متوقف و مختلف شد.

دبیرکل جامعه اسلامی مدیران ضمن بیان اینکه در نتیجه سو مدیریت‌ها در مردم نوعی بی‌اعتمادی به دولتمردان بوجود آمده و نه تنها قفل‌ها باز نشد بلکه بر قفل‌ها افزوده شد، اظهار داشت: این سوال همواره برای مردم مطرح است که چرا نظامی که اینقدر قدرت و ظرفیت دارد باید مشی سازش را در پیش بگیرد و در برابر قدرت ها کرنش کند و در بازار سرمایه به سرمایه مردم لطمات سنگینی وارد شود."""},
    {'title': "«جهان آرا» امشب میزبان «حسین شریعتمداری» است",
     'brief': "برنامه «جهان آرا» امشب میزبان «حسین شریعتمداری»، روزنامه نگار و مدیر مسئول روزنامه کیهان است. ",
     'text': """به گزارش خبرگزاری فارس، برنامه تلویزیونی جهان آرا که شنبه ها و دوشنبه ها به صورت زنده از شبکه افق پخش می شود؛ در تلاش است تا در گفتگو با کارشناسان و مسئولان، مسائل سیاسی روز را برای عامه مردم تبیین کند.

این قسمت از برنامه‌ی گفتگو محور جهان آرا قرار است درباره مسائل سیاسی روز در آستانه سالگرد چهل و دو سالگی انقلاب اسلامی صحبت کند.

مهمان امشب جهان آرا، «حسین شریعتمداری»، روزنامه نگار و مدیر مسئول روزنامه کیهان است.

برنامه تلویزیونی جهان آرا امشب ساعت 22 از شبکه افق پخش خواهد شد."""},
    {'title': "تغییر مدیریت کیش ایر برای دومین بار/ انتصاب مدیرعامل جدید با مدرک «دکتری طب هوایی»",
     'brief':"امروز مجددا مدیرعامل کیش ایر تغییر کرد و مدیریت این شرکت هواپیمایی پس از حدود 2 ماه که در اختیار کاپیتان سید جواد هاشمی بود، به محمدرضا حبیبی واگذار شد. ",
     'text': """به گزارش خبرنگار اقتصادی خبرگزاری فارس 17 آذرماه امسال بود که کاپیتان سید جواد هاشمی تهرانی، سرپرستی شرکت هواپیمایی کیش را پس از فرزانه شرفبافی بر عهده گرفت.

امروز و پی از گذشت حدود 2 ماه از این انتصاب، مجددا مدیرعامل کیش ایر تغییر کرد و دبیر شورای عالی مناطق آزاد که از پنجم بهمن ماه امسال بازنشسته است اما ظاهرا دعوت به کار شده است، محمدرضا حبیبی را به سمت مدیرعاملی کیش ایر منصوب کرد.

در حکم حبیبی آمده است: پیرو ابلاغیه 34/76240 مورخ 98/05/05 وزیر محترم امور اقتصادی و دارایی و به موجب ماده ۲۲ اساسنامه شرکت هواپیمایی کیش ایر (سهامی خاص) و نظر به سوابق و تجربیات ارزشمند جنابعالی به موجب این حکم به عنوان «مدیرعامل شرکت هواپیمایی کیش» منصوب می شوید.

در بخش دیگری از این حکم آمده است: تقویت امکانات این شرکت در جهت سیاست‌های کلان دولت تدبیر و امید و توسعه خدمات با کیفیت و نیز استفاده از ظرفیت فضای حمل و نقل هوایی کشور و ایفای نقش فعال بین المللی با بهره‌مندی از سرمایه‌های مردمی و کیشوندان مورد انتظار است.

بنابراین گزارش «محمدرضا حبیبی» دارای مدرک تحصیلی دکتری طب هوایی است. 

از مهمترین سوابق کاری وی می توان به عضویت در هیات مدیره انجمن هوا فضا، عضویت در هیات مدیره شرکت هواپیمایی کیش، عضویت در هیات مدیره فرودگاه بین المللی و منطقه ویژه اقتصادی پیام و عضویت در هیات مدیره شرکت هواپیمایی آسمان و ریاست دانشکده صنعت هواپیمایی اشاره کرد.

بنابراین گزارش کیش ایر یکی از شرکت های هواپیمایی عضو IATA (یاتا) است، در حال حاضر این شرکت هواپیمایی دارای 11 فروند هواپیما شامل 7 فروند هواپیمای بوئینگ MD و 2 فروند هواپیمای فوکر 100 و 2 فروند ایر باس A321 است."""} ]
    

    mehr_articles = [
    {'title': "سرویس‌دهی رایگان متروی تهران در روز ۲۲ بهمن",
     'brief': "مدیرعامل شرکت بهره برداری متروی تهران و حومه از رایگان بودن خدمات شرکت بهره‌برداری متروی تهران و حومه به شهروندان در روز ۲۲ بهمن خبر داد.",
     'text': """به گزارش خبرگزاری مهر، فرنوش نوبخت با اشاره به برگزار نشدن مراسم راهپیمایی یوم الله ۲۲ بهمن در پایتخت افزود: مراسم ۲۲ بهمن ماه امسال به دلیل شیوع ویروس کرونا، با شرایط خاص و به صورت موتوری و خودرویی برگزار می‌شود. با توجه به تمهیدات انجام شده برای تسهیل تردد شهروندان و شرکت کنندگان در این برنامه از ابتدای صبح روز ۲۲ بهمن ماه تا پایان مراسم ایستگاه‌های خطوط هفتگانه متروی تهران و حومه رایگان خواهد بود.

مدیرعامل شرکت بهره برداری متروی تهران و حومه با بیان اینکه در این روز خدمات رسانی در خطوط هفتگانه متروی تهران و حومه افزایش می‌یابد تصریح کرد: طبق روال سنوات گذشته و به منظور حفظ نظم و امنیت در روز ۲۲ بهمن در میدان آزادی، ایستگاه متروی میدان آزادی واقع در خط چهار مترو از ابتدای صبح تا پایان مراسم تعطیل و مسافرگیری انجام نخواهد شد."""},
    {'title': "٣۴٠ شناور به نیروی دریایی سپاه الحاق شد",
     'brief': "بندرعباس - ٣۴٠ فروند شناور رزمی و پشتیبانی رزم در کلاس‌های مختلف باحضور رئیس ستاد کل نیروهای مسلح به نیروی دریایی سپاه الحاق شد.",
     'text': """به گزارش خبرنگار مهر، مراسم الحاق ۳۴۰ فروند شناور به نیروی دریایی سپاه صبح دوشنبه با حضور سرلشکر پاسدار محمد باقری رئیس ستادکل نیروهای مسلح، سرلشکر پاسدار حسین سلامی فرمانده کل سپاه، سرتیپ پاسدار علیرضا تنگسیری فرمانده نیروی دریایی سپاه، استاندار هرمزگان، نماینده ولی فقیه در استان هرمزگان و جمعی دیگر از مسئولان کشوری و لشکری در بندرعباس برگزار شد.

این شناورها در ترکیب‌های عملیاتی در خلیج فارس و دریای عمان و همچنین دریای خزر آماده مأموریت می‌شوند.

این شناورهای سبک، تندرو و هجومی در مراکز وابسته به نیروی دریایی سپاه و همکاری وزارت دفاع ساخته شده است که عملیات الحاق آنها به نیروی دریایی سپاه صبح امروز در ستاد این نیرو در بندرعباس برگزار شده است.""",} ]

    raja_articles = [
        {'title': "واگذاری باشگاه پرسپولیس در روزهای آینده از طریق فرابورس",
         'brief': "رئیس سازمان خصوصی‌سازی گفت: باشگاه پرسپولیس به زودی از طریق فرابورس واگذار می‌شود و پس از آن باشگاه استقلال هم واگذار می‌شود. ",
         'text': """

حسنعلی قنبری ممان امروز در حاشیه نشست سهام عدالت در وزارت اقتصاد در جمع خبرنگاران در مورد واگذاری دو باشگاه فوتبال پرسپولیس و استقلال موسوم به سرخابی‌ها گفت: واگذاری این دو باشگاه در جریان قرار دارد. اولین شرکتی که واگذار می‌شود پرسپولیس است چون اطلاعات باشگاه پرسپولیس منظم‌تر و دقیق‌تر بود و رسیدگی به صورت‌های مالی کامل شده است. باشگاه استقلال هم در جریان رسیدگی قرار دارد که یک هفته بعد از پرسپولیس باشگاه استقلال هم واگذار می‌شود.

 

وی گفت: قرار بود در دهه فجر این دو باشگاه از طریق فرابورس به مردم عرضه شود اما می‌خواهیم با دقت این واگذاری انجام شود و گرفتار عجله و اشتباه نشویم. صورت‌های مالی دو باشگاه باید شفاف شوند. شفاف‌سازی را سازمان خصوصی‌سازی انجام نمی‌دهد بلکه سازمان حسابرسی صورت‌های مالی دو باشگاه را تأیید می‌کند، الان در مرحله تأیید نهایی قرار دارد، البته حساب‌های قبلی دو باشگاه تأیید شده‌اند و حساب‌های 6 ماهه اخیر درخواست شده‌اند که آن هم به زودی تأیید و دو باشگاه از طریق فرابورس به مردم عرضه می‌شود.

 

رئیس سازمان خصوصی‌سازی همچنین در مورد این که آیا کشت و صنعت هفت تپه دوباره به دولت برمی‌گردد، گفت: برای واگذاری‌ها سازمان عریض و طویلی به نام خصوصی‌سازی ساخته شده است که واگذاری‌ها با منطق و اصول انجام شود، البته گاهی واگذاری‌ها به مشکل برمی‌خورد و اگر واگذاری وفق مفاد قرارداد نباشد، چون واگذاری‌ها به صورت مشروط انجام می‌شود و قطعی نیست، بنابراین واگذاری‌ها به دولت برمی‌گردد و تجدیدنظر صورت می‌گیرد.

 

وی در مورد این که هفت تپه به دولت برمی‌گردد یا نه اظهار بی‌اطلاعی کرد و گفت: من فعلا از این مسأله خبر ندارم.

 

قنبری ممان همچنین در پاسخ به سؤالی که چرا سهام عدالت برای 1.8 میلیون سهامدار عدالت که کارت پرس شده سهام عدالت هم در اختیار دارند اختصاص نیافته است، گفت: در مقطعی اعلام شد که سهامداران عدالت در سامانه ثبت نام کنند و مدارک خود را ارائه کنند. احراز هویت قانونی صورت گیرد، یک تعداد از مشمولان سهام عدالت که یک میلیون و 800 هزار نفر بودند این کارها را انجام ندادند و در سامانه ثبت نشدند و اختلاف حاضر به خاطر همین مسأله است. فعلا بر اساس سامانه سازمان خصوصی‌سازی تعداد سهامداران عدالت فقط 49 میلیون نفر است و کس دیگری نمی‌تواند سهامدار عدالت باشد.
"""},
        {'title': "بارش رحمت الهی در حرم های مقدس کربلا و نجف",
         'brief': "با بارش رحمت الهی در اعتاب مقدس عراق علی الخصوص کربلا و نجف اشرف صحنه ها و تصاویر زیبایی خلق شد. ",
         'text': """بارش رحمت الهی در اعتاب مقدسه عراق باعث خلق صحنه‌هایی بدیع و زیبا شده و زائران و مجاوران حرم های مقدس را مشعوف کرد.


زائران و مجاوران در کربلای معلی با مشاهده بارش رحمت الهی دست به دعا برداشتند.

 
همچنین در نجف اشرف بارش باران باعث تجمع زائران زیر ناودان طلای حرم علوی و خواندن دعا و نیایش شد."""},
        {'title': "عرضه ۳۰ هزار دستگاه خودرو به بازار",
         'brief': "در مراسمی با حضور رییس کل گمرک جمهوری اسلامی ایران، مدیرعامل سازمان بنادر و دریانوردی ایران و مدیرعامل گروه صنعتی ایران‌خودرو، طرح توسعه گمرک اختصاصی ایران‌خودرو به بهره‌برداری رسید. ",
         'text': """ایکوپرس- با بهره‌برداری از این طرح و تسریع در روند ترخیص و ارسال قطعات، در گام نخست، بیش از ۳۰ هزار دستگاه خودرو تکمیل، تجاری سازی و وارد بازار خواهد شد. 
رییس کل گمرک جمهوی اسلامی ایران در این مراسم با بیان این‌که اگر بخواهیم جامعه‌ای با مشکلات کمتر داشته باشیم، باید فضای کسب و کار رقابتی شود، گمرک را حامی و در خدمت تولید دانست و تصریح کرد: در این مسیر سازمان های حاکمیتی وظیفه‌ای جز تسهیل‌گری ندارند. 
مهدی میراشرفی، افزود: ایجاد انبار اختصاصی گمرک سبب خواهد شد تا امکانات و کالاها از گمرکات مستقیما به کارخانه‌ها منتقل شود و به این ترتیب گره‌های موجود در تجارت و تولید باز شود. """} ]
    authors = {'خبرگزاری فارس': {'age': 24, 'articles': fars_articles},
               'خبرگزاری مهر': {'age': 36, 'articles': mehr_articles},
                'خبرگزاری رجا': {'age': 50, 'articles': raja_articles}}

    for author, author_data in authors.items():
        a = add_author(author, author_data['age'])
        for article in author_data['articles']:
            add_article(a, article['title'], article['brief'], article['text'])

    for author in Author.objects.all():
        for article in Article.objects.filter(author=author):
            print("- {0} - {1}".format(str(author), str(article)))

def add_article(author, title, brief, text):
    p = Article.objects.get_or_create(author=author, title=title, brief=brief, text=text)[0]
    p.save()
    return p

def add_author(name, age, articles=0):
    a = Author.objects.get_or_create(name=name, age=age, num_of_articles=articles)[0]
    a.save()
    return a
if __name__ == '__main__':
    print("Starting Blogger population script...")
    populate()
