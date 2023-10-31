# 1. Buat variabel list dengan value : [nama kendaraan, jenis kendaraan, cc kendaraan, warna kendraan, roda kendaraan]
# tambahkan dari list tersebut di belakang dengan value: [harga kendaraan, tipe kendaraan]
# tambahkan dari setelah jenis kendaraan dengan value : [merk kendaraan]

kendaraan =["motor", "ninja zx motor ", "1197cc", "hitam", "roda dua"]
kendaraan.append("99 juta")
kendaraan.append("kopling")
kendaraan.insert(2,"yamaha")
print(kendaraan)


# 2. Buat program pyhton dengan match case untuk menghitung luas bangun datar: 
# jika pilih 1, maka menghitung luas persegi 
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga 
# selain pilihan di atas, maka keterangan : salah pilih angka

#luas persegi
ket = """masukkan pilihan:
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
"""
pilihan = input (ket)

match pilihan:
    case "1":
        print ("memilih 1 untuk menghitung luas persegi")
        sisi = int (input("masukan sisi?"))
        luasp = sisi * sisi
        print ("luas persegi yang sisinya",sisi,"adalah",luasp)

    case "2":
        print ("memilih 2 untuk menghitung luas lingkaran")
        jari2 = float (input("masukkan jari2?"))
        luasL = 3.14*jari2*jari2
        print("luas lingkaran yang jari2nya",jari2,"adalah",int(luasL))

    case "3":
        print ("memilih 3 untuk menghitung luas segitiga")
        alas = float (input("masukkan panjang alas segitiga:"))
        tinggi = float (input("masukkan tinggi segitiga"))
        luasS = 0.5*alas*tinggi
        print("luas segitiga yang alasnya",alas,"dan tingginya",tinggi,"adalah",luasS)
    case _:
        print("salah memilih pilihan")