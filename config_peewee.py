import csv
from peewee import SqliteDatabase, Model, CharField, IntegerField
import pandas as pd


db = SqliteDatabase('jo_predict.db')


class AthletesData(Model):
    edition = IntegerField(null=True)
    country_noc = CharField(null=True)
    sport = CharField(null=True)
    event = CharField(null=True)
    athlete = CharField(null=True)
    athlete_id = IntegerField(null=True)
    medal = CharField(null=True)
    total_medaille = IntegerField(null=True)

    class Meta:
        database = db


data = pd.read_csv('data_athlete_prediction.csv', index_col=0)

db.connect()
db.create_tables([AthletesData])

with db.atomic():
    for _, row in data.iterrows():
        AthletesData.create(
            edition=row['edition'],
            country_noc=row['country_noc'],
            sport=row['sport'],
            event=row['event'],
            athlete=row['athlete'],
            athlete_id=row['athlete_id'],
            medal=row['medal'],
            total_medaille=row['total_medaille'])

db.close()
