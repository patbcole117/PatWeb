import random

class Funlink:
    def __init__(self, url, alias, min=0, max=255, d_color='rgb(200, 200, 200)'):
        self.url = url
        self.alias = alias
        self.min = min
        self.max = max
        self.d_color = d_color
        self.color = self.pick_color()


    def pick_color(self):
        r = random.choice(range(self.min, self.max))
        g = random.choice(range(self.min, self.max))
        b = random.choice(range(self.min, self.max))

        return f"rgb({r}, {g}, {b})"

    def to_dict(self):
        return {
            'url': self.url,
            'alias': self.alias,
            'color': self.color
        }