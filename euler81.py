from Queue import PriorityQueue


def solve():
    with open("matrix.txt", "r") as f:
        matrix = [[int(x) for x in line.split(",")] for line in f.readlines()]
    pq = PriorityQueue()
    min_path = (0,0)
    start_value = matrix[0][0]
    print start_value
    pq.put((start_value, min_path))
    side_length = len(matrix) - 1
    i = 0
    scores = {min_path:start_value}
    min_path = (start_value, min_path)
    while min_path[1] != (side_length, side_length):
        min_path = pq.get()
        x_val = min_path[1][0]
        y_val = min_path[1][1]
        total = min_path[0]
        print min_path[1]
        next_points = []
        if x_val < side_length : next_points.append((x_val+1,y_val))
        if y_val < side_length : next_points.append((x_val,y_val+1))
        if not next_points:
            return total
        for next_point in next_points:
            next_value = matrix[next_point[0]][next_point[1]]
            next_total = total + next_value
            potential_best_path = next_total
            previous_best_path = scores.get(next_point, 0)
            if (not previous_best_path) or potential_best_path < previous_best_path:
                scores[next_point] = next_total
                pq.put((potential_best_path,next_point))
    
print solve()
    