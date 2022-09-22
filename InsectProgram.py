import InsectClass as i

housefly = i.Insect(2,4)       #this creates 2 seperats instances (housefly and mosquito)
mosquito = i.Insect(4,8)

housefly.calc_flight()
mosquito.calc_flight()

print('the housefly can cly up to', housefly.get_flight())
print('the mosquito can fly up to', mosquito.get_flight())
