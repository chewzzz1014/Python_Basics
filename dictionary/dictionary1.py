#introductory operations of dictionary part 2
#updating position of alien
#Involves dictionary and selection statement

alien_0={"x_position": 0,"y_position": 25,"speed": "Medium"}
print("The current position of alien is ("+str(alien_0["x_position"])+","+str(alien_0["y_position"])+").")
print("Readjusting speed...")

if alien_0["speed"]=="Fast":
    x_increment=1
    y_increment=1
elif alien_0["speed"]=="Medium":
    x_increment=2
    y_increment=2
else:
    x_increment=3
    y_increment=3

alien_0["x_position"]=alien_0["x_position"]+x_increment
alien_0["y_position"]=alien_0["y_position"]+y_increment

print("The alien is now at position ("+str(alien_0["x_position"])+","+str(alien_0["y_position"])+")")


