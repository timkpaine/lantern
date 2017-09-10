
try:
    import mimesis
except:
    from faker import Faker
    fake = Faker()


def _mname():
    person = mimesis.Personal(locale='en')
    return person.full_name()


def _fname():
    return fake.name()
