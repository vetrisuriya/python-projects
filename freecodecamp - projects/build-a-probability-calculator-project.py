import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.num_balls = {}
        for color, count in kwargs.items():
            self.num_balls[color] = count
            self.contents.extend([color] * count)

    def draw(self, num_balls_to_draw):
        if num_balls_to_draw >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []
            return drawn_balls
        else:
            drawn_balls = []
            for _ in range(num_balls_to_draw):
                chosen_ball = random.choice(self.contents)
                drawn_balls.append(chosen_ball)
                self.contents.remove(chosen_ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        
        drawn_balls = temp_hat.draw(num_balls_drawn)
        
        drawn_balls_count = {}
        for ball in drawn_balls:
            drawn_balls_count[ball] = drawn_balls_count.get(ball, 0) + 1
        
        is_successful = True
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                is_successful = False
                break
        
        if is_successful:
            successful_experiments += 1
            
    return successful_experiments / num_experiments
