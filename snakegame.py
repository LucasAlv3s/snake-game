import pygame
from pygame.locals import *
from sys import exit

pygame.init()


#pygame.mixer.music.set_volume(0.05)
#musica_de_fundo = pygame.mixer.music.load('musicafundo.mp3')
#pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
#barulho_colisao.set_volume(1)

largura = 640
altura = 480


x_cobra = int(largura/2)
y_cobra = int(altura/2) #meio da tela


velocidade = 10
x_controle = velocidade
y_controle = 0


from random import randint
x_maca = randint(40, 600)
y_maca  = randint(50, 430) #escolhe um valor entre os declarados

fonte = pygame.font.SysFont('arial', 40, True, True) #negrito e italico
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()


lista_cobra = []
comprimento_inicial = 5

morreu = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = lista com os valores de X e Y XeY = [X, Y]
        pygame.draw.rect(tela, (0, 255,0) , (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca  = randint(50, 430)
    morreu = False



while True:
    relogio.tick(25)
    tela.fill((216,216,191))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra, y_cobra, 20, 20)) #posicao x y largura altura
    maca = pygame.draw.rect(tela,(255,0,0), (x_maca,y_maca , 20, 20))

    if cobra.colliderect(maca):
       x_maca = randint(40, 600)
       y_maca  = randint(50, 430)
       pontos = pontos + 1
       barulho_colisao.play()
       comprimento_inicial = comprimento_inicial + 1
    

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    # lista_cobra = [] não pode ficar dentro do loop
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1: #cobra encostou nela

        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = "Game Over! Pressione R para jogar novamente"
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()

        morreu = True 
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) #duas barras transformam em inteiro
            tela.blit(texto_formatado, ret_texto) 
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0


    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    #if y >= altura:
    #    y=0 #para voltar ao começo
    #y = y+1
    
    #pygame.draw.circle(tela, (0,0, 255), (300, 260), (40)) #cor posicao raio
    #pygame.draw.line(tela, (255,255,0), (390, 0), (390, 600), 5) #posicao inicial e final, espessura

    tela.blit(texto_formatado,(450, 40))

    pygame.display.update()