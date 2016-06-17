import pygame
import pprint
import sqlite3
import time
import datetime

unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
conn = sqlite3.connect("C:\\Users\\tom\Documents\python\New folder\\quant_1.db")
conn2 = sqlite3.connect("C:\\Users\\tom\Documents\python\New folder\\quant_2.db")


c = conn.cursor()
c2 = conn2.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(indx REAL, name TEXT, datestamp TEXT, keyword TEXT, tax REAL, balance REAL, allies TEXT)")

#c.execute('SELECT * FROM stuffToPlot')
data = c.fetchall()
for row in data:
    print(row)

#print (row[2])
aa = 7
bb= 11500
#c.execute('SELECT * FROM stuffToPlot WHERE int = 2 ')
#c.execute('UPDATE stuffToPlot SET balance = 9876 WHERE indx(?)',[aa])
conn.execute("UPDATE stuffToPlot SET balance = ? WHERE indx = ?", ([bb,aa]))
conn.commit()
c.close()
conn.close()

WHITE = (0,99,99)
BLACK = (244,44,44)

player_one_balance = 10000
weekly_allow = 15000


width = 800
height = 800

players = {'q1':10000,'q2':10000,'q3':10000,'q4':10000,'q5':10000}
class splashscreen():


    pygame.init()

    font2 = pygame.font.Font(None,54)
    font3 = pygame.font.Font(None,34)
    screen_width = 700
    screen_height =600
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill(WHITE)
    scoreprint = "MARKET CRASH 1977   ver 00.01: "
    text = font2.render(scoreprint, 1, BLACK)
    textpos = (10,100)
    screen.blit(text,textpos)
    scoreprint = "you are allowed ,to begin,, to buy a maximum of five stocks,"
    sp2 = "a beginning balance of 10000 dollars "
    sp2a = "weekly bank payments are 1500 dollars"
    sp3 = "trading balances posted at the end of each week..."
    text2 = font3.render(sp2, 1, BLACK)
    text2a = font3.render(sp2a,1,BLACK)
    text = font3.render(scoreprint, 1, BLACK)
    text3 = font3.render(sp3,1,BLACK)
    textpos = (10,200)
    screen.blit(text, textpos)
    
    textpos = (10,250)
    screen.blit(text2,textpos)
    textpos = (10,300)
    screen.blit(text2a,textpos)
    textpos = (10,350)
    screen.blit(text3,textpos)
#event = pygame.event.wait()
    pygame.display.flip()
done = False        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True
# Initialize Pygame

class stockscreen():

    gameDisplay = pygame.display.set_mode((width,height))
    image = pygame.image.load("C:\\Users\\tom\Documents\python\New folder\\figure_2.png")
    gameDisplay.blit(image,(10,10))
    pygame.display.flip()
pygame.mixer.pre_init(44100, -16, 2, 4048)
pygame.init()
splashscreen()
for key in players.items():
    print key
start = raw_input("are you the bank ???")
if start == 'y':
    player_one_balance = 1000000
print ("Start Week 1 with   ")+str(player_one_balance),
print ("do you want to buy ??? or sell???   ")
start1 = int(raw_input("in dollars or marks"))
print player_one_balance- start1
print start1
print players['q3']/2

stockscreen()