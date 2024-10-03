x = input("nazwa pliku: ").strip()
plik = x.split(".")[-1].lower()  # dzieli plik: random.txt na ["random","txt"]
# nastepnie porownuje z koncowkami istniejacych formatow plikow

if plik == "gif":
    print("image/gif")

elif plik == "jpg" or plik == "jpeg":
    print("image/jpeg")

elif plik == "pdf":
    print("application/pdf")

elif plik == "png":
    print("image/png")

elif plik == "txt":
    print("text/plain")

elif plik == "zip":
    print("application/zip")

else:
    print("application/octet-stream ")
