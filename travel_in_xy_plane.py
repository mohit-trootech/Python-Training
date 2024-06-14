# Find Coordinated from Origin Based on Directions
from check_number_input import is_number
from distance_between_coordinates import distance_from_origin

print("Enter the Step by Step Position\n"
      "Press N/n fpr North\n"
      "Press S/s fpr South\n"
      "Press E/e fpr East\n"
      "Press W/w for West\n"
      "ps - Press C/c for Cancel - ")

x, y = 0, 0

while True:
    direction = input("Choose Direction Press C/c to Stop- ").lower()
    if direction != 'c':
        steps = input(f"Enter Steps in {direction.upper()} - ").lower()
        if is_number(steps):
            if direction == 'n' or direction == 's':
                y += int(steps)
            elif direction == "w" or direction == "e":
                x += int(steps)
            else:
                print("Invalid Input Choose Input From N/E/W/S - ")
    else:
        break


print(f"Position in XY Plane (x, y) = ({x}, {y})")
print(f"Distance From Origin(0,0) is {distance_from_origin((x, y))}")
