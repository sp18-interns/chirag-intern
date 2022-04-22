
from Point import Point

if __name__ == '__main__':
    yash = Point(3.0, 4.0, "Yash")
    parag = Point(-2.0, 4.0, "Parag")
    chirag = Point(3.0, -4.0, "Chirag")
    sumit = Point(-3.0, -4.0, "Sumit")
    bachha = Point(0.0, 0.0, "Bachha")
    print(yash)
    print('*' * 100)
    print(f"The x coordinate of point {yash.label} is {yash.get_x()}")
    print('*' * 100)
    print(f"The y coordinate of point {yash.label} is {yash.get_y()}")
    print('*' * 100)
    print("Increment x by 5 coordinate & y by 2 coordinate")
    yash.move_coordinate_by(5.0, 2.0)
    print('*' * 100)
    yash.check_quadrant()
    parag.check_quadrant()
    chirag.check_quadrant()
    sumit.check_quadrant()
    bachha.check_quadrant()
    print('*' * 100)
    chirag.distance_from_coordinate_of_point(2.5,4.0)
    print('*' * 100)

    chirag.distance_from_point_object(yash)
    print('*' * 100)

    chirag.distance_from_origin()
    print('*' * 100)