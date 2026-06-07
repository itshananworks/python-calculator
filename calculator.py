
"""TAMPILAN KALKULATOR"""
print("=" * 35)
print("        KALKULATOR PYTHON")
print("=" * 35)
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
print("5.Keluar Kalkulator")

while True:
    pilihan = input("Masukkan pilihan Anda: ").lower()
    if pilihan not in [
        "1", "penjumlahan", "1.penjumlahan",
        "2", "pengurangan", "2.pengurangan",
        "3", "perkalian", "3.perkalian",
        "4", "pembagian", "4.pembagian",
        "5", "keluar", "5.keluar kalkulator", "keluar kalkulator"
    ]:
        print("ERROR:PILIHAN TIDAK VALID")
        continue
    try:
        if pilihan in ["5", "keluar", "5.keluar kalkulator", "keluar kalkulator"] :
            print("Terimakasih telah menggunakan kalkulator kami:D")
            break
        angka1 = float(input("Masukkan angka: "))
        angka2 = float(input("Masukkan angka: "))
    except ValueError:
        print("ERROR:HARUS MASUKKAN ANGKA!!")
        continue
    if pilihan in ["1", "penjumlahan", "1.penjumlahan"] :
        hasil = angka1 + angka2
    elif pilihan in ["2", "pengurangan", "2.pengurangan"] :
        hasil = angka1 - angka2
    elif pilihan in ["3", "perkalian", "3.perkalian"] :
        hasil = angka1 * angka2
    elif pilihan in ["4", "pembagian", "4.pembagian"] :
        if angka2 == 0:
            print("ERROR:TIDAK DAPAT MEMBAGI DENGAN 0!!")
            continue
        else:
            hasil = angka1 / angka2
    print(f"Hasilnya adalah:{hasil:,.2f}")