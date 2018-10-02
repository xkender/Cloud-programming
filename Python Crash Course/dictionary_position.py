alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print("Original x-position: " + str(alien_0['x_position']))

#Movie alien to the right
#Determine how far to move the alien based on its current speed.

def speed():
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        #This must be a fast alien :)
        x_increment = 3

#The new position of the alien will be original plus the x_increment.

    alien_0['x_position'] += x_increment  # Used += to shortcut adding itself to the x_increment.
    print("New x-position: " +  str(alien_0['x_position']))

speed()

print(alien_0)
del alien_0['speed'] #removing a value from dictionary >> deleted key value is removed permanently.
print(alien_0)

alien_0['speed'] = "fast" #adding a value to the dictionary
print(alien_0)

speed()
