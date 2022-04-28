from faker import Faker
fake = Faker()

# Utworzyłem klasę pierwszą (BaseContact)
# Wprowadziłem metodę contact(), zwracającą predefiniwany string na każdym z wywoływanych obiektów; Metoda contact() sprecyzowana zostałaa dla 
# klasy BaseContnact
# dodałem metodę __repr__ w celu sformatowania widoku obiektów, tj określenia sposóbu w jaki będą  wyświatlane obiekty klasy BaseContact
# podczas iteracji  listy obiektów 
# dodałem @property

class BaseContact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def label_lenght(self): 
        return len(self.name)
    
    def contact(self):
        return f"Wybieram {self.phone} i dzwonię do {self.name} \n"

    def __repr__(self):
        return f'{self.name}, {self.phone}, {self.email}'


card_one = BaseContact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_two = BaseContact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_three = BaseContact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_four = BaseContact(name = fake.name(),phone = fake.phone_number(),email=fake.email())
card_five = BaseContact(name =fake.name(),phone = fake.phone_number(),email=fake.email())


# Utworzyłem , za pomoca dziedziczenia druga klasę (BusinessContact), rozszerzyłem klasę bazową o przechowywanie informacji związanych z pracą danej osoby – 
# stanowisko, nazwa firmy, telefon służbowy
# Wprowadziłem metodę contact(), zwracającą predefiniwany string na każdym z wywoływanych obiektów; Metoda contact() sprecyzowana zostałaa dla 
# klasy BusinessContnact
# dodałem metodę __repr__ w celu sformatowania widoku obiektów, tj określenia sposóbu w jaki będą  wyświatlane obiekty klasy BusinessContact
# podczas iteracji  listy obiektów

class BusinessContact(BaseContact):
    def __init__(self, occupation, company,businessphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company = company
        self.businessphone = businessphone


    def contact(self):
        return f"Wybieram {self.businessphone} i dzwonię do {self.name} \n"
    
    def __repr__(self):
        return f'{self.name}, {self.phone}, {self.email}, {self.occupation}, {self.company}, {self.businessphone}'


card_six = BusinessContact(name = card_one.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_seven = BusinessContact(name = card_two.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_eight = BusinessContact(name = card_three.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_nine = BusinessContact(name = card_four.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(), businessphone = fake.phone_number())
card_ten = BusinessContact(name = card_five.name,phone = fake.phone_number(),email=fake.email(),company = fake.company(),occupation=fake.job(),businessphone = fake.phone_number())



# utworzyłem petlę w celu przeprowadzenia iteracji listy obiektów, z uwzględnieniem @property
for i in [card_one, card_two, card_three, card_four, card_five, card_six,card_seven,card_eight, card_nine,card_ten]:
    print(f"{i.name},{i.phone},{i.email},{i.label_lenght}")

# utworzyłem petlę w celu wykonania metody contact() na każdym obiekcie z listy 
for i in [card_one, card_two, card_three, card_four, card_five, card_six,card_seven,card_eight, card_nine,card_ten]:
    print(i.contact())


# Utworzylem funkcję create_contacts(), która ma generowac losowe wizytówki, zawierające określone atrybuty, 
# w ilości zdefiniowanej przez użytkownika. 
# pierwszy sposób   - create instances
def create_contacts(type, amount):
    if type == "base":
        for i in range (1,amount+1):
            print(BaseContact(name = fake.name(),phone = fake.phone_number(),email=fake.email()))
    elif type == "business":
        for i in range (1,amount+1):
            print(BusinessContact(name = fake.name(),phone = fake.phone_number(),email=fake.email(), occupation=fake.job(), company = fake.company(), businessphone = fake.phone_number()))
create_contacts("base",5)

# drugi sposób  - create list, print list 
def create_contacts(type, amount):
    my_list = []
    if type == "base":
        for i in range (1,amount+1):
            my_list.append(BaseContact(name = fake.name(),phone = fake.phone_number(),email=fake.email()))
    elif type == "business":
        for i in range (1,amount+1):
            my_list.append(BusinessContact(name = fake.name(),phone = fake.phone_number(),email=fake.email(),occupation=fake.job(),company = fake.company(), businessphone = fake.phone_number()))
    print(my_list)
create_contacts("business",5)