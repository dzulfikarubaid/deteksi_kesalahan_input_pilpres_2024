import pandas as pd
def data():
    df = pd.read_csv("villages.csv")
    code = list(df['code'])
    code.sort()
    return code