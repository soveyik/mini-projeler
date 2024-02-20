cities = ("Türkiye","Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
                   "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır",
                   "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay",
                   "Isparta", "İçel", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli",
                   "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu",
                   "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa",
                   "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın",
                   "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce")
print("Yardım için ? veya help yazınız...")
while (1):
    giris = input("Giriş :")
    if giris == 'exit':
        break
    if giris == '?' or giris == 'help':
        print("Çıkmak için exit yazınız.")
        print("Plaka öğrenmek için ' p Şehir' girin.")
        print("Şehir plakası öğrenmek için ' c Plaka' girin. ")

    arr = giris.split()
    if (arr[0] == 'p'):
        ind = cities.index(arr[1])
        print(arr[1], " : ", ind)
        if ind < 10:
            print(arr[1]," : ", " 0" + str(ind))
        else:
            print(arr[1] +" : ", ind)
    if (arr[0] == 'c'):
        ind = int(arr[1])
        print(ind, " : ", cities[ind])

