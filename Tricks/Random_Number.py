import random as Rand

Rand.seed(20)

print(Rand.normalvariate(10, 100))
print(Rand.uniform(10, 100))
print(Rand.randint(10, 100))
print(Rand.randrange(10, 100))

mylist = list("python competitive programming trick")
print(Rand.sample(mylist, 3))
print(Rand.choices(mylist, k=3))
print(Rand.shuffle(mylist))
