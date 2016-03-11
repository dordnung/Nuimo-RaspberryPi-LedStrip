import math

# From https://github.com/jacksongabbard/Python-Color-Gamut-Generator


class Wheel:
    color_wheel = [
        [0xff, 0x00, 0xff],
        [0xff, 0x00, 0x00],
        [0xff, 0xff, 0x00],
        [0x00, 0xff, 0x00],
        [0x00, 0xff, 0xff],
        [0x00, 0x00, 0xff],
        [0xff, 0x00, 0xff]]  # one extra so less wrap-around logic is required

    def __init__(self, radius=25):
        self.radius = radius
        self.colors = []
        self.createWheel()

    def make_color(self, base, adj, ratio):
        output = []

        """
        Go through each bit of the colors adjusting blue with blue, red with red,
        green with green, etc.
        """
        for pos in xrange(3):
            base_chan = self.color_wheel[base][pos]
            adj_chan = self.color_wheel[adj][pos]
            new_chan = int(round(base_chan * (1 - ratio) + adj_chan * ratio))

            output.append(int(new_chan))
        return output

    def createWheel(self):
        for x in xrange(self.radius * 4):
            self.colors.append([])

            for y in xrange(self.radius * 4):
                self.colors[x].append([])
                # probably an error in my logic, but the center line is getting
                # inverted. so, manually set it if it's not right
                if x - self.radius * 2 == 0:
                    angle = angle = -90
                    if y > self.radius * 2:
                        angle = 90
                else:
                    angle = math.atan2((y - self.radius * 2),
                                       (x - self.radius * 2)) * 180 / math.pi

                angle = (angle + 30) % 360

                idx = angle / 60
                if idx < 0:
                    idx = 6 + idx
                base = int(round(idx))

                adj = (6 + base + (-1 if base > idx else 1)) % 6

                ratio = max(idx, base) - min(idx, base)

                color = self.make_color(base, adj, ratio)

                self.colors[x][y] = color

    def getColorAtAngle(self, angle):
        x = int(self.radius * math.cos(angle) + self.radius * 2)
        y = int(self.radius * math.sin(angle) + self.radius * 2)

        return self.colors[x][y]

if __name__ == "__main__":
    wheel = Wheel(100)
    for x in xrange(360):
        print(wheel.getColorAtAngle(x))
