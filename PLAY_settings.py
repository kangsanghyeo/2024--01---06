TITLE = "Going up"
WIDTH = 800
HEIGHT = 700
FPS = 60

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.17 # 중력을 바꿔 점프 속도, 점프 거리 조절 가능


PLATFORM_LIST = [(0, HEIGHT - 50, WIDTH + 50, 50),
                 (WIDTH/2 - 50, HEIGHT*3/5, 100, 20),
                 (19, HEIGHT - 350, 100, 20),
                 (350, 110, 100, 20),
                 (135, 250, 100, 20), (100, 100, 100, 20)]

BLOCKFORM_LIST = [(600, 350, 100, 20),
                  (700, 130, 100, 20)]

FLOORFORM_LIST = [(500, 200, 80, 20)]

SQUAREFORM_LIST = [(300, 200, 90, 20)]


