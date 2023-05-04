import pandas as pd

train_cvs_path = "./train.csv"
train_csv = pd.read_csv(train_cvs_path)
train_csv.describe()
print(train_csv)
print("ok")
