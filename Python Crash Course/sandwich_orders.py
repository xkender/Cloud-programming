print("\nSandwich Orders: \n")

#Make a list for nSandwich Orders
sandwich_orders = ['deli_special', 'parmesan', 'mozeralla', 'chicken', 'egg']
#Make an empty list
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("Making your sandwich: " + current_order.title())
    finished_sandwiches.append(current_order)

for current_order in finished_sandwiches:
    print("Your " + current_order + "sandwich is ready!, Enjoy! :)")

sandwich_orders = ['deli_special', 'parmesan', 'mozeralla', 'chicken', 'egg']
for sandwich in range(3):
    sandwich_orders.append('pastrami')
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("Unfortunatelly no pastrami is left!: ")
print(sandwich_orders)
