import csv
from peewee import SqliteDatabase, Model, CharField, IntegerField
import pandas as pd


db = SqliteDatabase('country_predict.db')


class CountryData(Model):
    year= CharField(null=True)
    country = CharField(null=True)
    competitions = CharField(null=True)
    total_medaille = IntegerField(null=True)

    class Meta:
        database = db


data = pd.read_csv('data_country_prediction.csv', index_col=0)

db.connect()
db.create_tables([CountryData])

with db.atomic():
    for _, row in data.iterrows():
        CountryData.create(
            year=row['year'],
            country=row['country'],
            competitions=row['competitions'],
            total_medaille=row['total_medaille'])

db.close()