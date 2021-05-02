import pygame

pygame.init()
back = (200,255,255)
mw = pygame.display.set_mode((500,500))
game = True
clock = pygame.time.Clock()
class Area():
    def __init__(self, x=0,y=0,width =0, height=0,color=None):
        self.rect = pygame.Rect(x,y,height,width)
        self.fill_color = back
        if color:
            self.fill_color = color
    
    def color(self,new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x,y):
        return self.collidepoint(x,y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):

    def __init__(self,filename, x=0,y=0,width =10, height=10):
        Area.__init__(self,x=x,y=y,width=width, height=height, color= None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))

ball = Picture('ball.png', 160,200,50,50)
platform = Picture('ball.png', 200, 330, 100, 30)
bricks = []
count = 9
for j in range(3):
    y = 5 +(55*j)
    x = 5 + (27.5*j)
    for i in range(count):
        br = Picture('ball.png', x,y,50, 50)
        bricks.append(br)
        x += 55
    count -= 1


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    ball.fill()
    platform.fill()
    mw.fill(back)
    for br in bricks:
        br.draw()
    ball.draw()
    platform.draw()

    
    pygame.display.update()
    clock.tick(40)
