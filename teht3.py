import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")

hyvis = pygame.image.load("hahmo.png").convert()
örkki = pygame.image.load("hahmo2.png").convert()
viholliset = [["vihollinen.png", 200, 200]]
def piirraKuva(hyvis, x, y):
    naytto.blit("hahmo.png", (x, y))
    naytto.blit("hahmo2.png", (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    for pahis in viholliset:
        if pahis[3] == True:
            kuva = pygame.image.load(pahis[0]).convert()
            naytto.blit(kuva, (pahis[1], pahis[2]))
    pygame.display.flip()

def kontrolli(hahmot, viholliset, tapahtuma):
    hyvis = hahmot[0]
    for vihollinen in viholliset:
        if (hahmot[0][1] <= viholliset[0][1] +50 and hahmot[0][1] >= viholliset[0][1] -50) and (hahmot[0][2] <= viholliset[0][2] +50 and hahmot[0][2] >= viholliset[0][2]-50):
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            hahmot[0][3] = True
            viholliset [0] [3] = True
        elif tapahtuma.key == pygame.K_RIGHT and hyvis[1] < 540:
             
                hyvis[1] += 10
        elif tapahtuma.key == pygame.K_LEFT and hyvis[1] > 0:
            
                hyvis[1] -= 10
        elif tapahtuma.key == pygame.K_UP and hyvis[2] > 0:
                
                hyvis[2] -= 10
        elif tapahtuma.key == pygame.K_DOWN and hyvis[2] < 300:
               
                hyvis[2] += 10

def sulje()

def main():
    hyvis = ["hahmo.png", 100, 100, False]
    örkki = ["hahmo2.png", 250, 250, False]
    hahmot = [hyvis]
    viholliset = [örkki]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, viholliset, tapahtuma)
        piirtaminen(naytto, hahmot, viholliset)


main()