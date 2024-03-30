import pygame;

pygame.init();

def make_pL(playList, musicname):
    playList.append(musicname);


pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(0);

sc = pygame.display.set_mode((200, 100));


pL = [];

make_pL(pL, 'music.mp3')
make_pL(pL, 'music2.mp3')


clock = pygame.time.Clock()

pause = False;
vol = 1.0;
i = 0;
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause;
                if pause:
                    pygame.mixer.music.pause();
                else:
                    pygame.mixer.music.unpause();
            elif event.key == pygame.K_1:
                vol -= 0.5;
                pygame.mixer.music.set_volume(vol);
            elif event.key == pygame.K_2:
                vol += 0.5;
                pygame.mixer.music.set_volume(vol);
            elif event.key == pygame.K_z:
                if i== 0:
                    i = len(pL) - 1;
                else:
                    i -= 1;
                pygame.mixer.music.load(pL[i]);
                pygame.mixer.music.play(0);
            elif event.key == pygame.K_x:
                if i == len(pL) - 1:
                    i = 0;
                else :
                    i += 1;

                pygame.mixer.music.load(pL[i]);
                pygame.mixer.music.play(0);



    pygame.display.update();

    clock.tick(60)