data_panen = {
    'lokasi1':{
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'keledai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 1000,
            'keledai' : 500
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1800,
            'jagung' : 1200,
            'keledai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 2000,
            'jagung' : 1500,
            'keledai' : 700
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 2200,
            'jagung' : 1800,
            'keledai' : 800
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun F',
        'hasil_panen' : {
            'padi' : 2400,
            'jagung' : 2000,
            'keledai' : 900
        }
    }
}

# 1. Tampilkan seluruh data dari data_panen
print("Seluruh data panen:")
for lokasi, data in data_panen.items():
    print(f"{data['nama_lokasi']}: {data['hasil_panen']}")

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung dari {data_panen['lokasi2']['nama_lokasi']}: {jumlah_jagung_lokasi2}")

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")

# 4. Masukkan hasil panen padi dan kedelai ke dalam variabel yang berbeda
hasil_padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
hasil_kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']

hasil_padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
hasil_kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']

hasil_padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
hasil_kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']

# 5. Buat percabangan untuk memeriksa kondisi lokasi
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")

