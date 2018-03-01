def calculate_points (car, ride, time, bonus):
    points = 0
    car_loc = car.getLoc()
    start_loc = ride.get_start_loc()
    end_loc = ride.get_end_loc()
    time_to_start = locs_to_time(car_loc, start_loc)
    ride_time = locs_to_time(start_loc, end_loc)
    if time + time_to_start + ride_time <= ride.get_end_time():
        if time + time_to_start <= ride.get_start_time():
            points = points + bonus
        points = points + ride_time

    return points



def locs_to_time(loc1, loc2):
    y_time = abs(loc1.getY() - loc2.getY())
    x_time = abs(loc1.getX() -  loc2.getX())
    time = x_time + y_time
    return time

