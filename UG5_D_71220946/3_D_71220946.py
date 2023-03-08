import math

while True:
    jarak_awal = input("Masukkan jarak awal(dalam meter): ")
    if jarak_awal.lower() == "berhenti" or jarak_awal.lower() == "stop":
        print("program di berhentikan")
        break
    
    sudut_elevasi_pertama = input("Masukkan sudut elevasi pada menit ke-5: ")
    sudut_elevasi_kedua = input("Masukkan sudut elevasi pada menit ke-6: ")

    jarak_awal = float(jarak_awal)
    sudut_elevasi_pertama = math.radians(float(sudut_elevasi_pertama))
    sudut_elevasi_kedua = math.radians(float(sudut_elevasi_kedua))

    tinggi_drone_awal = jarak_awal * math.tan(sudut_elevasi_pertama)
    jarak_drone_akhir = jarak_awal * math.tan(sudut_elevasi_kedua) - tinggi_drone_awal
    selisih_ketinggian_drone = jarak_drone_akhir * math.tan(sudut_elevasi_kedua)

    print("Ketinggian drone pada menit ke-5: ", tinggi_drone_awal)
    print("Selisih ketinggian drone saat menit ke-5 dan ke-8 adalah: ", selisih_ketinggian_drone)
