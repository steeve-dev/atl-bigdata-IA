import csv
from tortoise import Tortoise, fields
from tortoise.models import Model

class Person(Model):
    id = fields.IntField(pk=True)
    edit = fields.CharField(max_length=50)
    age = fields.IntField()

async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['your_module_name']},
    )
    await Tortoise.generate_schemas()

async def insert_data_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = await Person.create(
                name=row['Name'],
                age=int(row['Age'])
            )
            print(f"Inserted person: {person.name}")

async def main():
    await init()
    await insert_data_from_csv('your_csv_file.csv')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
