from audioop import avg


def drop_first_last(grades):
    first, *middle, last, = grades
    return avg(middle)


record = ('Dave', 'dave@example.com', '99-33-44-595-44', '2020200-3-3-')
name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

