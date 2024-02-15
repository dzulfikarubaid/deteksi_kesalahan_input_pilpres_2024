import pandas as pd
from sel import scrape_data
df = pd.read_csv("villages.csv")

code = list(df['code'])
code.sort()
# print(code)
for i in code:
    i = str(i)
    scrape_data(f'https://pemilu2024.kpu.go.id/pilpres/hitung-suara/{i[0:2]}/{i[0:4]}/{i[0:6]}/{i}')