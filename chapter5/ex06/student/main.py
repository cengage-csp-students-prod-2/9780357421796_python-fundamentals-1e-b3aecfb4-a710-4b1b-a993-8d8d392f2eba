cars = ('coupe','coupe', 'coupe', 'carbiolet','sedan')
fav = cars.count('coupe')
amt = len(cars)
percentage_coup = (fav/amt) * 100
if percentage_coup > 45:
    print("Too many coupes in the garage.")
else:
    print ("You are all set with cars.")