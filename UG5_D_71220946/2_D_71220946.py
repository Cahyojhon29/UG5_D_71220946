def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0

    while True:
        asal = input("Masukkan asal mobil (ketik 'done' untuk keluar): ")

        if asal.lower() == 'done':
            break

        if asal.capitalize() == 'Solo':
            jumlahSol += 1
        elif asal.capitalize() == 'Surabaya':
            jumlahSur += 1
        elif asal.capitalize() == 'Jogja':
            jumlahJog += 1
        elif asal.capitalize() == 'Magelang':
            jumlahMag += 1
        else:
            print("Kota asal tidak valid.")

    print(f"Jumlah mobil dari Solo: {jumlahSol}")
    print(f"Jumlah mobil dari Surabaya: {jumlahSur}")
    print(f"Jumlah mobil dari Jogja: {jumlahJog}")
    print(f"Jumlah mobil dari Magelang: {jumlahMag}")

hitung_mobil()
