from database import data
from pemiluadil import pilpresadil

data_list = data()
code = [angka for angka in data_list if str(angka).startswith("73")]
pilpresadil(code)

