num_steps = 5

class Vertex:
    def __init__(self, x_axis: int, y_axis: int):
        self.x = x_axis
        self.y = y_axis


class Leaf:
    def __init__(self, x_axis: int, y_axis: int, path: list):
        self.x = x_axis
        self.y = y_axis
        self.path = path


leaves = list()
start = Leaf(0, 0, [])
leaves.append(start)

for i in range(num_steps):
    for l in leaves:



