from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
clock = time.Clock()
FPS = 60
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
x1 = 50
y1 = 300
x2 = 250
y2 = 300
background = transform.scale(
    image.load('images (3).jfif'),
    (700, 500)
)
game_runing = True #открыто
while game_runing:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    keys_pressed = key.get_pressed()
    #первый спрайт
    if keys_pressed[K_w] and y1 > 0:
        y1 -= 10
    if keys_pressed[K_a] and x1 > 0:
        x1 -= 10
    if keys_pressed[K_s] and y1 < 400:
        y1 += 10
    if keys_pressed[K_d] and x1 < 600:
        x1 += 10
    #второй спрайт
    if keys_pressed[K_UP] and y2 > 0:
        y2 -= 10
    if keys_pressed[K_LEFT] and x2 > 0:
        x2 -= 10
    if keys_pressed[K_DOWN] and y2 < 400:
        y2 += 10
    if keys_pressed[K_RIGHT] and x2 < 600:
        x2 += 10
    for e in event.get():
        if e.type == QUIT:
            game_runing = False #закрыто
    clock.tick(FPS)
    display.update()
#создай окно игры

#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»