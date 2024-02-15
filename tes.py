import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    # Mengambil konten HTML dari URL
    response = requests.get(url)
    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    span = soup.find_all('span', class_='vs__selected')
    try:
        provinsi = span[2].text
        kota = span[3].text
        kecamatan = span[4].text
        kelurahan = span[5].text
    except IndexError:
        return
    # Membuat DataFrame kosong untuk menyimpan data tabel
    df = pd.DataFrame()
    print("=====================================")
    print(f"{provinsi}_{kota}_{kecamatan}_{kelurahan}")
    
    # Cari semua elemen tabel
    tables = soup.find_all('table')

    # Jika ditemukan tabel, ambil data di dalamnya
    if tables:
        for table in tables:
            # Temukan semua baris dalam tabel
            rows = table.find_all('tr')
            for row in rows:
                # Temukan semua sel dalam baris
                cells = row.find_all('td')
                # Inisialisasi list untuk menyimpan data sel dalam satu baris
                row_data = []
                # Periksa setiap sel dalam baris
                for cell in cells:
                    # Ambil teks dari sel dan tambahkan ke dalam list row_data
                    cell_text = cell.get_text(strip=True)
                    row_data.append(cell_text)
                # Tambahkan satu baris data ke dalam DataFrame
                df = pd.concat([df, pd.DataFrame([row_data])], ignore_index=True)
    else:
        print("Tidak ada tabel ditemukan pada halaman web.")

    # Simpan DataFrame ke dalam file CSV
    df.replace('Data sedang dalam proses', '0', inplace=True)
    df.fillna(0, inplace=True)
    df.replace('', '0', inplace=True)
    df['Total'] = df.iloc[:, 1:].astype(float).sum(axis=1)
    
    for i in df['Total']:
        if i > 300:
            df.to_csv(f"{provinsi}_{kota}_{kecamatan}_{kelurahan}.csv", index=False)
            print("Ada kesalahan input data")
            print("Data tabel telah disimpan ke dalam file CSV.")
            return
    print("Tidak ada kesalahan input data")

# Gunakan fungsi scrape_data dengan URL yang sesuai
url = "https://pemilu2024.kpu.go.id/pilpres/hitung-suara/18/1871/187115/1871151005"
scrape_data(url)
