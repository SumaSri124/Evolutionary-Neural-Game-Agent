import numpy as np

class FlappyEnv:
    def __init__(self):
        self.gravity = 0.25
        self.flap_impulse = -4.5
        self.pipe_speed = 2.0
        self.pipe_gap = 120

        self.screen_width = 288
        self.screen_height = 512

        self.bird_x = 50 
        self.reset()

    def reset(self):
        self.bird_y = self.screen_height // 2
        self.bird_velocity = 0.0

        self.pipe_x = self.screen_width
        self.pipe_gap_center = np.random.randint(50, self.screen_height - 50)

        self.scored = False

        return self._get_state()

    def step(self, action):
        reward = 1     
        done = False

        if action == 1:
            self.bird_velocity = self.flap_impulse

        self.bird_velocity += self.gravity
        self.bird_y += self.bird_velocity

        self.pipe_x -= self.pipe_speed
        if self.pipe_x < -50:
            self.pipe_x = self.screen_width
            self.pipe_gap_center = np.random.randint(50, self.screen_height - 50)
            self.scored = False

        if not self.scored and self.pipe_x + 50 < self.bird_x:
            reward += 10         
            self.scored = True

        if self._check_collision():
            reward = -100         
            done = True

        return self._get_state(), reward, done

    def _check_collision(self):
        if self.bird_y <= 0 or self.bird_y >= self.screen_height:
            return True

        gap_top = self.pipe_gap_center - self.pipe_gap // 2
        gap_bottom = self.pipe_gap_center + self.pipe_gap // 2

        hit_horizontal = (
            self.bird_x > self.pipe_x and
            self.bird_x < self.pipe_x + 50
        )
        hit_vertical = (
            self.bird_y < gap_top or
            self.bird_y > gap_bottom
        )

        return hit_horizontal and hit_vertical

    def _get_state(self):
        return np.array([
            self.bird_y,
            self.bird_velocity,
            self.pipe_x,
            self.pipe_gap_center
        ], dtype=np.float32)
