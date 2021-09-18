#imports#
import keyboard
from sys import platform
from libs.game import Game
from time import sleep
import curses


#functions#

def print(text,screen):
   
   screen.clear()
   screen.bkgd(" ",curses.color_pair(10))
   screen.addstr(1,1,str(text),curses.color_pair(10))
   screen.border()
   screen.refresh()

def full_screen():
   
   if platform=="win32" or "win64":
      keyboard.press('f11')
   elif platform == "linux" or platform == "linux2":
      keyboard.press('alt+f10')
   elif platform=="darwin":
      keyboard.press('Control+Command+F')


#main init#

game =  Game()
full_screen()
game.init()
main = curses.initscr()
screen_two=curses.newwin(17,93,int(curses.LINES/4),int(curses.COLS / 6))
screen_one=curses.newwin(17,93,int(curses.LINES/4),int(curses.COLS / 6-7))
screen_three=curses.newwin(17,93,int(curses.LINES/4),int(curses.COLS / 6-7))
curses.noecho()
curses.curs_set(0)
screen_two.nodelay(True)
word_battle="""
   ██     ██  ██████  ██████  ██████      ██████   █████  ████████ ████████ ██      ███████ 
   ██     ██ ██    ██ ██   ██ ██   ██     ██   ██ ██   ██    ██       ██    ██      ██      
   ██  █  ██ ██    ██ ██████  ██   ██     ██████  ███████    ██       ██    ██      █████   
   ██ ███ ██ ██    ██ ██   ██ ██   ██     ██   ██ ██   ██    ██       ██    ██      ██      
    ███ ███   ██████  ██   ██ ██████      ██████  ██   ██    ██       ██    ███████ ███████ 
                                                                                                     
      [Press Esc to exit]           [Press ENTER to start]          [Press h for help]"""





#colour init#

curses.start_color()
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLUE)
curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_YELLOW)

 
 
#menu#






print(str(word_battle),screen_one)
while True:
   key=main.getch()
   if key==27:
      full_screen()
      curses.endwin()
      exit()
   if key==10:
      # if enter key is pressed start the game#
      break
   elif key==104:
      screen_three.clear()
      screen_one.clear()

      print("""
   ▄▀█ █▄▄ █▀█ █░█ ▀█▀  ▀█▀ █░█ █▀▀  █▀▀ ▄▀█ █▀▄▀█ █▀▀
   █▀█ █▄█ █▄█ █▄█ ░█░  ░█░ █▀█ ██▄  █▄█ █▀█ █░▀░█ ██▄
   
         Words will come down from the top of the screen and you need to press 
         the corresponding letters for each word to score points.If any letters 
         reach the bottom of the screen you will lose life.
         Correctly typed letters will become a"*".

         Each correct letter will give you 10 points,
         Each time a letter reach the bottom will reduce your
         life by 5.

         Press ESC to go back.""",screen_three)      
      # key handler for help screen#
      while True:
         key=main.getch()
         if key==27:
            screen_three.clear()
            
            print(str(word_battle),screen_one)
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
   except ConnectionRefusedError:
      print("Please check ypur network connection.")


#game over screen#
game.main.clear()

screen_two.nodelay(False)
curses.echo()
main.bkgd(curses.COLOR_BLACK)
print("""

            ██████  █████  ███    ███ ███████    ██████  ██    ██ ███████ ██████  
          ██       ██   ██ ████  ████ ██        ██    ██ ██    ██ ██      ██   ██ 
          ██   ███ ███████ ██ ████ ██ █████     ██    ██ ██    ██ █████   ██████  
          ██    ██ ██   ██ ██  ██  ██ ██        ██    ██  ██  ██  ██      ██   ██ 
           ██████  ██   ██ ██      ██ ███████    ██████    ████   ███████ ██   ██ 
                                                                                                                         

                                 [Press any key to exit]""",screen_two)
screen_two.getch()
keyboard.press('f11')

#command to end game#
curses.endwin()