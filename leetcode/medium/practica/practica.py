# 1.Login Tekshiruvi

# login = str(input("Loginingiz: "))
# parol = int(input("Parolingiz: "))

# if login == "admin":
#     print("Xush kelibsiz")
# elif parol == "1234":
#     print("Xush kelibsiz")
# else:
#     print("Login yoki parol xato")



# 2.Kino uchun yosh
# yosh = int(input("Yoshingiz: "))

# if yosh >= 13:
#     print("Siz kino tomosha qilishingiz mumkin")
# else:
#     print("Siz uchun ruxsat yoq")



# 3.Onlayn dokon chegirmasi

# xarid = int(input("Xarid summangiz: "))

# if xarid >= 500000:
#     chegirma = 500000 * 0.9
#     print(chegirma)
# else:
#     print(xarid)



# 4.Telefon quvvati

# batteryi = int(input("Batteryingiz: "))

# if batteryi < 20:
#     print("Telefonni zaryadlang")
# elif batteryi > 20 and batteryi < 80:
#     print("Battery holati yaxshi")
# elif batteryi > 80:
#     print("Battery deyarli tola")


# 5.Sinf Jurnali


# oquvchilar = []

# ismolish = str(input("Oquvchilar ismi: "))
# oquvchilar.append(ismolish)
# print(oquvchilar)

# for ism in oquvchilar:
#     print(ism)


# 6.Kuchli parol


# parol = input("Parolingiz: ")

# if len(parol) < 8:
#     print("Parol qisqa")
# else:
#     print("Parol qabul qilindi")


# 7.Market savati



# mahsulotSoni = int(input("Mahsulotlar soni: "))

# mahsulotlar = []

# for i in range(mahsulotSoni):
#     mahsulot = input(f"{i+1}-mahsulot nomi: ")
#     mahsulotlar.append(mahsulot)

# print("Mahsulotlar:")

# for i in range(mahsulotSoni):
#     print(f"{i+1}. {mahsulotlar[i]}")



# 8.Chatdagi emoji


# emoji = input("Emoji: ")

# uzunligi = len(emoji)
# print(uzunligi)



# 9.Ismlar orasidan qidirish

ismlar = []
ismKiritish = input("Ism: ")
ismlar.append(ismKiritish)
topish = input("Izlanayotgan ismni kiriting: ")
if topish in ismlar:
    print("Topildi", topish)
else:
    print("Topilmadi")




# 10.Mehmonlar royxati


# mehmon_soni = int(input("Mehmonlar soni: "))

# mehmonlar = []

# for i in range(mehmon_soni):
#     ismi = input(f"Mehmonni yozing {i + 1} ismi: ")
#     mehmonlar.append(ismi)

# print("\nJami mehmonlar:", len(mehmonlar))
# print("\nBirinchi mehmon:", mehmonlar[0])
# print("\nOxirgi mehmon:", mehmonlar[-1])