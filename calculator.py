

"""TAMPILAN KALKULATOR"""
def tampilan_kalkulator():
    print("=" * 35)
    print("        KALKULATOR PYTHON")
    print("=" * 35)
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.Keluar Kalkulator")


"""INPUT ANGKA"""
def input_angka():
    try:
        angka1 = float(input("Masukkan angka: "))
        angka2 = float(input("Masukkan angka: "))
        return angka1, angka2
    except ValueError:
        return None

"""PERHITUNGAN"""
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return None
    else:
        return a / b


"""PILIHAN PERHITUNGAN"""
def pilihan_perhitungan():
    pilihan = input("Masukkan Pilihan: ").lower()
    if pilihan not in [
        "1", "penjumlahan", "1.penjumlahan",
        "2", "pengurangan", "2.pengurangan",
        "3", "perkalian", "3.perkalian",
        "4", "pembagian", "4.pembagian",
        "5", "keluar", "5.keluar kalkulator", "keluar kalkulator"
    ]:
        return None
    return pilihan


"""TEMPAT MEMPROSES SEMUANYA"""
while True:
    tampilan_kalkulator()
    pilihan = pilihan_perhitungan()
    if pilihan is None:
        print("Pilihan Tidak valid")
        continue
    if pilihan in ["5", "keluar", "5.keluar kalkulator", "keluar kalkulator"] :
        print("Terimakasih telah memakai kalkulator kami:D")
        break
    angka = input_angka()
    if angka is None:
        print("ERROR:HARUS MASUKKAN ANGKA!!")
        continue
    angka1, angka2 = angka
    if pilihan in ["1", "penjumlahan", "1.penjumlahan"] :
        hasil = penjumlahan(angka1, angka2)
    elif pilihan in ["2", "pengurangan", "2.pengurangan"] :
        hasil = pengurangan(angka1, angka2)
    elif pilihan in ["3", "perkalian", "3.perkalian"] :
        hasil = perkalian(angka1, angka2)
    elif pilihan in ["4", "pembagian", "4.pembagian"] :
        hasil = pembagian(angka1, angka2)
        if hasil is None:
            print("ERROR:TIDAK DAPAT MEMBAGI DENGAN NOL")
            continue
    print(f"Hasilnya adalah: {hasil:,.2f}")
    