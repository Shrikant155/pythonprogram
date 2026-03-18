from faker import Faker
fake = Faker()
# print(fake.name())
name = fake.name()
mail = fake.email()

address = fake.address()
phon = fake.phone_number()
text = fake.text()
card = fake.credit_card_number()
print(f'name={name}\n{mail}\n{address}\n{text}\n{card}ln{phon}')