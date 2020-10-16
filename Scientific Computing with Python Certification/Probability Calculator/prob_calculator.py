import copy
import random
from collections import Counter


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        ball = ""
        for hat in kwargs.items():
            ball += ((hat[0] + " ") * hat[1])
        self.contents = ball.rstrip().split(" ")

    def draw(self, num_balls_drawn):
        if num_balls_drawn == 0:
            self.contents = []
        elif num_balls_drawn < len(self.contents):
            reduce_contents = random.sample(self.contents, k=num_balls_drawn)
            for ball in reduce_contents:
                self.contents.remove(ball)
            return reduce_contents
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    item_expected_balls = expected_balls.items()
    if num_balls_drawn > len(hat.contents):
        num_balls_drawn = len(hat.contents)

    for i in range(0, num_experiments):
        balls_drawn = random.sample(hat.contents, num_balls_drawn)
        dict_balls_drawn = dict(Counter(balls_drawn))
        count = 0

        for ball in item_expected_balls:
            key, value = ball[0], ball[1]
            if key in dict_balls_drawn and dict_balls_drawn[key] >= value:
                count += 1

        if len(dict_balls_drawn) == len(item_expected_balls) == count:
            probability += 1
        elif len(dict_balls_drawn) > len(item_expected_balls) == count:
            probability += 1

    return probability / num_experiments
