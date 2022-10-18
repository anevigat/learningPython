def toggle_boolean(boolean):
    if boolean:
        boolean = False
    else:
        boolean = True
    return boolean
    
def generate_doors(num_doors):
    doors = {}
    for i in range(1, num_doors + 1):
        doors["door" + str(i)] = False
    return doors

def iterate_with_steps(num_doors, steps):
    visited_doors = []
    for i in range(steps, num_doors + 1, steps):
        visited_doors.append(i)
    return visited_doors

def toggle_doors(doors, visited_doors):
    for i in visited_doors:
        doors["door" + str(i)] = toggle_boolean(doors["door" + str(i)])
    return doors

def full_run(num_doors):
    doors = generate_doors(num_doors)
    for i in range(1, num_doors + 1):
        doors = toggle_doors(doors, iterate_with_steps(num_doors, i))
    return doors