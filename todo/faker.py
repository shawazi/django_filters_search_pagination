from .models import Todo
from faker import Faker

def gen_data():
    fake = Faker()
    for item in range(200):
        Todo.objects.create(task=fake.sentence(), description=fake.text(), priority=fake.random_int(min=1, max=2), done=fake.boolean())
        # Todo.objects.create(task=fake.sentence()[:35], description=fake.text(), priority=fake.random_int(min=1, max=3), done=fake.boolean())
        # above is for postgresql fake data generation
    print("Completed fake data generation.")
    
