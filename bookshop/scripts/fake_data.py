import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE","bookshop.settings")

import django
django.setup()
### Modellerimize ve django içeriklerine erişmek için yukarıdaki gibi ayarlamaları yapmamız lazım
### SIRALAMA ÇOK ÖNEMLİ

from django.contrib.auth.models import User

from faker import Faker
import requests


def set_user():
    fake=Faker(["en_US"])
    
    f_name=fake.first_name()
    l_name= fake.last_name()
    u_name=f'{f_name.lower()}_{l_name.lower()}'
    email= f"{u_name}@{fake.domain_name()}"

    print(f_name,l_name,email)

    user_check= User.objects.filter(username=u_name)
    while user_check.exists():
        u_name= u_name + str(random.randrange(1,99))
        user_check = User.objects.filter(username=u_name)

    user= User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=25),
    )
    user.set_password("fakeruser123")
    user.save()
    print(f"user {u_name} has been saved")

    
from pprint import pprint
from books.api.serializers import BookSerializer

def searchOfBook(query):
    url= "http://openlibrary.org/search.json"
    payload={"q":query}
    response= requests.get(url,params=payload)
    jsn= response.json()
    books= jsn.get("docs")

    fake=Faker(["en_US"])

    for book in books:
        data= dict(
            name= book.get("title"),
            author= book.get("author_name")[0],
            explanation="-".join(book.get("edition_key")) ,
            pub_date= fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None)
        )
        serializer= BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(data.get("name"),"isimli kitap hatalı")
            continue



