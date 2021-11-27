## USER IMPORT

import csv
from django.contrib.auth import get_user_model

with open("lampoon_users.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        new_user = get_user_model().objects.create_user(
            email = row[1],
            password = "temp12345",
            url_username = row[0],
            first_name = row[10],
            last_name = row[11],
            graduation_year = "2021",
            display_name = row[7],
            board = "lit"
        )

## POST IMPORT

import csv
from django.contrib.auth import get_user_model

with open("lampoon_posts.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        new_user = get_user_model().objects.create_user(
            email = row[1],
            password = "temp12345",
            url_username = row[0],
            first_name = row[10],
            last_name = row[11],
            graduation_year = "2021",
            display_name = row[7],
            board = "lit"
        )