#Creating an emtpy list and appending dictionaries to it

car_pool = []

#creating a pool of 10 cars from each car dictionary
for cars in range (10):
    car_1 = {'make': 'ferrari', 'model': '911', 'color': 'red', 'package': 'luxury'}
    car_2 = {'make': 'honda', 'model': 'accord', 'color': 'black', 'package': 'limited'}
    car_3 = {'make': 'bmw', 'model': 'x5', 'color': 'black', 'package': 'comfort'}
    car_4 = {'make': 'mercedes', 'model': 'c200', 'color': 'gray', 'package': 'basic'}
#appending each dictionary from the loop to the emtpy list
    car_pool.append(car_1)
    car_pool.append(car_2)
    car_pool.append(car_3)
    car_pool.append(car_4)
#printing the number of dictionaries within the list
print(len(car_pool))

#for cars in car_pool[:5]:
    #print(cars)
#changing the first 5 cars that have black color to gray color and ultimate package 
for cars in car_pool[:5]:
    if cars['color'] == 'black':
        cars['color'] = 'gray'
        cars['package'] = 'ultimate'

print(car_pool[:5])
