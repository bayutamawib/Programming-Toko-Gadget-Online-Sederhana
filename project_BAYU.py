def fungsihandphone():
   global total
   global jumlah
   global jenis
   jumlah = 0
   total = 0
   jenis = ""
   print ("\n~~~~Catalog Handphone~~~~")
   print("1. Samsung - Rp2000000")
   print("2. Iphone - Rp8000000")
   print("3. Oppo - Rp1500000")
   nomor=int(input("Masukan Pilihan: "))
   jumlah= int(input("Berapa Buah: "))
   
   if nomor==1:
       total=jumlah*2000000
       print (jumlah," buah Samsung = Rp", total)
       jenis="Samsung"
   elif nomor==2:
       total=jumlah*8000000
       print (jumlah, "buah Iphone = Rp", total)
       jenis="Iphone"
   elif nomor==3:
       total=jumlah*1500000
       print (jumlah, " buah Oppo = Rp", total)
       jenis="Oppo"
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
   return jenis,jumlah,total

    
def fungsitablet():
   global total
   global jenis
   global jumlah
   jumlah = 0
   total = 0
   jenis = ""
   print("\n~~~~Menu Tablet~~~~")
   print("1. Samsung Galaxy Tab - Rp10000000")
   print("2. Ipad - Rp15000000")
   print("3. Xiaomi - Rp5000000")
   nomor=int(input("Masukan Pilihan: "))
   jumlah= int(input("Berapa Buah : "))

   if nomor==1:
       total=jumlah*10000000
       print (jumlah, " Samsung Galaxy Tab = Rp", total)
       jenis="Samsung Galaxy Tab"
   elif nomor==2:
       total=jumlah*15000000
       print (jumlah, " Ipad = Rp", total)
       jenis="Ipad"
   elif nomor==3:
       total=jumlah*5000000
       print (jumlah, " Xiaomi = Rp ", total)
       jenis="Xiaomi"
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
   return jenis,jumlah,total

def hapus_barang(list_barang,nama_barang) :
    list_barang_temp = []
    for barang in list_barang :
        if barang[0] != nama_barang :
            list_barang_temp.append(barang)
    return list_barang_temp
while True :
    print("~~~~Program Sederhana IndoCell~~~~")
    pembeli = input("Masukkan nama Pembeli: ")
    print ("Nama Pembeli :", pembeli) 
    
    masih_beli = True
    while masih_beli :
        
        list_barang = []
        masih_beli_2 = True
        while masih_beli_2:
            mau_beli_apa = input("Anda mau beli apa (tablet/handphone) : ")
            if mau_beli_apa == 'tablet' :
                belanjaan = fungsitablet()
                list_barang.append(belanjaan)
            elif mau_beli_apa == 'handphone' :
                belanjaan = fungsihandphone()
                list_barang.append(belanjaan)
            else :
                print('Inputan tidak valid')
                break
            cek_masih_beli_2 = input("Apakah anda masih ingin beli : (yes/no)")
            if cek_masih_beli_2 == 'no' :
                masih_beli_2 = False
            print("Selesai Berbelanja!!")
            
        # for barang in list_barang :
        #     print(barang)
        
        print("List barang anda :")
        for barang in list_barang :
            print(barang)
    
        cek_belanjaan = input("Apakah belanjaan anda sudah sesuai : (yes/no)")
        if (cek_belanjaan == 'no') :
            hapus = input("Barang apa yang anda ingin hapus : ")
            list_barang = hapus_barang(list_barang,hapus)
        
        totalsemua = 0
        for barang in list_barang :
            totalsemua += barang[2]
        print("\nTotal harus Dibayar: Rp",totalsemua)
        uang=int(input("Uang Tunai Pembeli: Rp."))
        kembalian=int(uang-totalsemua)
        print("Kembalian :",kembalian)
        
        print("\n===========================")
        print("======= S T R U K   B E L I =====")
        print("===========================")
        print (" Nama         :",pembeli)
        for barang in list_barang :
            print (" Beli            :",barang[1],barang[0],"-",barang[2])
        print (" Tagihan      : Rp.",totalsemua)
        print (" Uang          : Rp.",uang)
        print (" Kembalian  : Rp.",kembalian)
        print ("Terima kasih telah berbelanja di toko kami, selamat datang kembali :)")
        print("===========================")
        print("===========================")
        cek_masih_beli = input("Apakah anda masih ingin belanja : (yes/no)")
        if cek_masih_beli == 'no' :
            masih_beli = False
            print("Pembelian Selesai!!")