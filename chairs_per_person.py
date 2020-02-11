f = open("reservations")

for reservation in f:
    name, number = reservation.split(",")
    chairs_per_person = 50 / int(number)
    chairs_per_person = int(chairs_per_person) 
    print("{} will get {} chairs per person".format(name, chairs_per_person))
