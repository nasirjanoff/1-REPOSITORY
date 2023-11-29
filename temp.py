#yosh = int(input("Yoshingiz nechida?"))
#if yosh<=4:
 #   narh = 0
#elif yosh<=12:
 #   narh = 5000
#elif yosh<=18:
 #   narh = 8000
#else:
  #  narh = 10000
 #   
#print(f"Sizga kirish {narh} so'm")


#kun = input("Bugun qaysi kun?>>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
 #   print("Bugun dam olish kuni.")
#else:
#   print("Bugun ish kuni.")
    
 
#kun = input("Bugun nima kun?>>>")
#harorat = float(input("Bugun harorat qanday?>>>"))
#if kun.lower()=='yakshanba' and harorat>=30:
 #   print("Chomilgani ketik!")
#elif kun.lower()=='yakshanba' and harorat<30:
 #   print("Uyda dam olamiz!")
 
 
menu = ['osh', 'lagmon', 'somsa', 'bishteks', 'norin', 'qozonkabob']
ovqat =     input('Nima ovqat yeysiz?')
if ovqat.lower() in menu:
    print('buyurtma qabul qillindi')
else:
    print('Afsuski bizda bunday ovqat yo\'q')