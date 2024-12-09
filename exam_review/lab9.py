import math

def total_distance(directions: list) -> int:
    """
    compute total distance travelled
    params:
        directions - a list of directions (str) of the form "N 200"
    returns:
        total distance travelled
    """

    # variable to hold the sum of distances
    total = 0

    for direction in directions:
        parts = direction.split(' ') # this will be a list of strings, like ['N', '300']
        total += int(parts[1])

    return total


def net_distance(directions: list) -> float:
    """
    compute NET distance travelled
    params:
        directions - a list of directions (str) of the form "N 200"
    returns:
        net distance travelled
    """
    n_s_distance = 0
    e_w_distance = 0

    for direction in directions:
        parts = direction.split(' ')
        
        heading = parts[0]
        distance = int(parts[1])
        
        if heading == 'N':
            n_s_distance += distance
        elif heading == 'S':
            n_s_distance -= distance
        elif heading == 'E':
            e_w_distance += distance
        elif heading == 'W':
            e_w_distance -= distance
    
    return math.sqrt(n_s_distance **2 + e_w_distance ** 2)


def main() -> None:
    file = open('./exam_review/directions.txt', 'r')
    directions = []
    
    # here we'll use a sentinel loop to read all the file's lines
    # this is the "long" way to read a file,
    # but convenient if you have to stop partway
    line = file.readline()
    while line != '':
        directions.append(line.strip())
        line = file.readline()

    # another way to read lines from the file
    # contents = file.read()
    # directions = contents.split('\n')
    
    # and another way
    # directions = file.readlines()

    file.close()
    
    print(f'total distance = {total_distance(directions)}')
    print(f'net distance = {net_distance(directions)}')

main()