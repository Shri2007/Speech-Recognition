import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk! ")
    audio_text = r.listen(source)
    print("Time over, thank you! ")
    try:
        print("Text: " + r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that!")

#Lorem ipsum dolor sit ame
# t consectetur adipiscing elit, urna consequat feli
# s vehicula class ultricies mollis dictumst, aenean non a in donec n
# ulla. Phasellus ante pellentesque erat cum risus consequat imperdiet aliquam,
# integer placerat et turpis mi eros nec lobortis taciti, vehicula nisl litora tellus ligu
# la porttitor metus.


#Vivamus integer non suscipit
# taciti mus etiam at primis tempor s
# agittis sit, euismod libero facilisi aptent elementum feli
#
# s blandit cursus gravida sociis erat ante, eleifend lectus nullam
# dapibus netus feugiat curae curabitur est ad. Massa curae fringil
# la porttitor quam sollicitudin iaculis aptent leo ligula euismod dictumst,
# orci penatibus mauris er
# os etiam praesent erat volutpat
# posuere hac. Metus fringilla nec ullamcorper
# odio aliquam lacinia conubia mauris tempor, etiam ultricies pro
# in quisque lectus sociis id tristique, integer
# phasellus taciti pretium adipiscing tortor sagittis ligula.

#Mollis pretium lorem primis senectus habita
# sse lectus scelerisque donec, ultricies tortor suspendisse adipis
# cing fusce morbi volutpat pellentesque, consectetur mi risus molestie cura
# e malesuada cum. Dignissim lacus conval
# lis massa mauris enim ad mattis magnis senec
# tus montes, mollis taciti phasellus accumsan bibendum semp
# er blandit suspendisse faucibus nibh est, metus lobortis morbi cras magna vivamus per risus fe
# rmentum. Dapibus imperdiet praesent magnis ridiculus congue gravida curab
# itur dictum sagittis, enim et magna sit inceptos sodales parturient pharetra mo
# llis, aenean vel nostra tellus commodo pretium sapien sociosqu.