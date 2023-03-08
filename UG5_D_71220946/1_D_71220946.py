def ganti_kata(kalimat, cari, ganti):
    kata = kalimat.split()

    for i in range(len(kata)):
        if kata[i] == cari:
            kata[i] = ganti

    kalimat_baru = " ".join(kata)

    return kalimat_baru

kalimat = input("Masukkan kalimat: ")
cari = input("Kata yang dicari: ")
ganti = input("Diganti menjadi: ")

kalimat_baru = ganti_kata(kalimat, cari, ganti)

print(f"Kalimat baru: {kalimat_baru}")
