def schedule_lift(current_floor,requests):
    upward = [req for req in requests if req > current_floor]
    downward = [req for req in requests if req < current_floor ]

    upward.sort()
    downward.sort(reverse=True)

    upward_distance = 0
    prev_floor = current_floor
    for floor in upward:
        upward_distance += abs(floor - prev_floor)
        prev_floor = floor
    for floor in downward:
        upward_distance += abs(floor - prev_floor)
        prev_floor = floor


    downward_distance = 0
    prev_floor = current_floor
    for floor in downward:
        downward_distance += abs(floor - prev_floor)
        prev_floor = floor
    for floor in upward:
        downward_distance += abs(floor - prev_floor)
        prev_floor = floor


    if upward_distance <= downward_distance:
        direction = "up"
        path = upward + downward
    else:
        direction = "down"
        path = downward + upward
    
    return direction,path


current_floor = 2
requests = [1,3,4]

direction, path = schedule_lift(current_floor,requests)
print(f"Lift should go {direction}. path : {path}")