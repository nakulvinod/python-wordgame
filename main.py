#imports#
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from libs.game import Game
from time import sleep
import curses

#main init#

game =  Game()
game.init()
main_screen = curses.initscr()
main_screen.keypad(True)
screen_two=curses.newwin(15,80,int(curses.LINES/4),int(curses.COLS / 6))
screen_two.keypad(True)
screen_one=curses.newwin(17,93,int(curses.LINES/4),int(curses.COLS / 6-7))
screen_three=curses.newwin(17,93,int(curses.LINES/4),int(curses.COLS / 6-7))
curses.noecho()
curses.curs_set(0)
screen_two.nodelay(True)



#colour init#

curses.start_color()
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLUE)
curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_YELLOW)

#functions#
def how_to_play():
   screen_one.clear()
   screen_three.clear()
   screen_three.bkgd(" ",curses.color_pair(10))
   screen_three.addstr(1,1,"""
   ▄▀█ █▄▄ █▀█ █░█ ▀█▀  ▀█▀ █░█ █▀▀  █▀▀ ▄▀█ █▀▄▀█ █▀▀
   █▀█ █▄█ █▄█ █▄█ ░█░  ░█░ █▀█ ██▄  █▄█ █▀█ █░▀░█ ██▄
   
         Words will come down from the top of the screen and you need to press 
         the corresponding letters for each word to score points.If any letters 
         reach the bottom of the screen you will lose life.
         Correctly typed letters will become a"*".

         Each correct letter will give you 10 points,
         Each time a letter reach the bottom will reduce your
         life by 5.

         Press ESC to go back.""",curses.color_pair(10))
   screen_three.border()
   screen_three.refresh()

def welcome():
   screen_three.clear()
   screen_one.refresh()
   screen_one.bkgd(" ",curses.color_pair(10))
   screen_one.addstr(3,1,"""
   
  ██     ██  ██████  ██████  ██████      ██████   █████  ████████ ████████ ██      ███████ 
  ██     ██ ██    ██ ██   ██ ██   ██     ██   ██ ██   ██    ██       ██    ██      ██      
  ██  █  ██ ██    ██ ██████  ██   ██     ██████  ███████    ██       ██    ██      █████   
  ██ ███ ██ ██    ██ ██   ██ ██   ██     ██   ██ ██   ██    ██       ██    ██      ██      
   ███ ███   ██████  ██   ██ ██████      ██████  ██   ██    ██       ██    ███████ ███████ 
                                                                                                                               
      [Press Esc to exit]           [Press ENTER to start]          [Press h for help]"""                   ,
curses.color_pair(10)
)
   screen_one.border()
   screen_one.refresh()
 





#menu#

welcome()
while True:
   key=main_screen.getch()   
   if key==27:
     curses.endwin()
     exit()
   elif key==10:
      # if enter key is pressed start the game#
      break
   elif key==104:
      screen_three.clear()
      screen_one.clear()
      how_to_play()
      # key handler for help screen#
      while True:
         key=main_screen.getch()
         if key==27:
            screen_three.clear()
            welcome()
            break

#27=ESC,10=enter key,104=H key#
      

     
            

  
      


#game#
while True:
   
   try:      
      event = screen_two.getch()
      if (event) == 27:
         #to quit the game and show the gameover screen#
         break
         
      else:
         keyPressed = ""
         #checks if event has characters in it and passes keypressed to game.py#
         if event != -1:
            keyPressed = chr(event)
         value=game.update(keyPressed)

         #checks if value == 1 and ends the game if so#
         if value==1:
            game.clear()
            break
         sleep(0.19)
   #line to except the keyboard interrupt and show game over instead#
   except KeyboardInterrupt:
      break


#game over screen#
game.main.clear()
screen_two.nodelay(False)
curses.echo()
screen_two.bkgd(' ',curses.color_pair(10))

screen_two.addstr(1,1,"""

     ██████  █████  ███    ███ ███████    ██████  ██    ██ ███████ ██████  
   ██       ██   ██ ████  ████ ██        ██    ██ ██    ██ ██      ██   ██ 
   ██   ███ ███████ ██ ████ ██ █████     ██    ██ ██    ██ █████   ██████  
   ██    ██ ██   ██ ██  ██  ██ ██        ██    ██  ██  ██  ██      ██   ██ 
    ██████  ██   ██ ██      ██ ███████    ██████    ████   ███████ ██   ██ 
                                                                            
                                                                           

                              Press any key to exit""",
curses.color_pair(10)
)
screen_two.border()
screen_two.refresh()
   
screen_two.getch()

#command to end game#
curses.endwin()