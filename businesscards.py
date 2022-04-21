from faker import Faker
fake = Faker()


class BaseContnact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    def contact(self):
        print(f"Wybieram {self.phone} i dzwonię do {self.name} \n")



card_one = BaseContnact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_two = BaseContnact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_three = BaseContnact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_four = BaseContnact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_five = BaseContnact(name =fake.name(),phone = fake.phone_number(),email=fake.email())
personal_list = [card_one, card_two, card_three, card_four, card_five]


class BusinessContact(BaseContnact):
    def __init__(self, occupation, company,businessphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company = company
        self.businessphone = businessphone
    def contact(self):
        print(f"Wybieram {self.businessphone} i dzwonię do {self.name} \n")



card_six = BusinessContact(name = card_one.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_seven = BusinessContact(name = card_two.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_eight = BusinessContact(name = card_three.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_nine = BusinessContact(name = card_four.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_ten = BusinessContact(name = card_five.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(),businessphone = fake.phone_number())
personal_list = [card_six, card_seven, card_eight, card_nine, card_ten]


for i in [card_one, card_two, card_three, card_four, card_five, card_six,card_seven,card_eight, card_nine,card_ten]:
    print(f"{i.name},{i.phone},{i.email}")

for i in [card_one, card_two, card_three, card_four, card_five]:
    print(i.contact())

for i in [card_six,card_seven,card_eight, card_nine,card_ten]:
    print(i.contact())