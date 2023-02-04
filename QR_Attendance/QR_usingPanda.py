import pyqrcode
import pandas as pd


def createQRCode():
    df = pd.read_csv("students.csv")
    for index, values in df.iterrows():
        # print(values["Name"])
        Ennum = values["Enrollment No"]
        # name = values["Name"]

        # Name:{name}
        data = f'''{Ennum}'''
        print(data)
        image = pyqrcode.create(data)
        image.svg(f"{Ennum}.svg", scale="5")


createQRCode()
