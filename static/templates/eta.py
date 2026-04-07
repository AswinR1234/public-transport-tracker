def calculate_eta(distance, speed):
    if speed == 0:
        return "Bus Stopped"
    
    time = distance / speed
    return round(time * 60, 2) 
