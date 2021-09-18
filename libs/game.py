#imports#
import curses

import os
from random import randint,choice
import pygame
import requests

#sound player#
def playSound(file):
   dir=os.path.dirname(os.path.abspath(__file__))
   path=os.path.join(dir,"..","sounds",file)
   pygame.mixer.init()
   pygame.mixer.music.load(path)
   pygame.mixer.music.play()

#game class#
class Game:  

   #data#
   words = None
   game_screen=None
   life_screen=None
   main=None
   life_screen_bg=None
   score_screen=None
   life=100
   max_y,max_x = 0,0
   selected_word = None
   current_x,current_y=1,2
   score =00
   SCORE_MAX_WIDTH=6
   life_print_screen=None
   random_colour=None
   LIFE_DEGRADE_FACTOR=5
   before_selected_word=""
   a=""
   pair_cur_index=20

   def init(self):


      response = requests.get("https://random-word-api.herokuapp.com/word?number=1000&swear=0")
      self.words=response.json()
      #screen init#
      self.main = curses.initscr()
      
      # Life Screen init #
      self.life_screen = curses.newwin(2, 50,2,10)
      self.life_screen_bg = curses.newwin(2, 50,2,10)
      self.life_print_screen=curses.newwin(4,10,1,0)
      
      # game screen init #
      self.game_screen = curses.newwin(curses.LINES-6, curses.COLS-2,5,1)
      self.game_screen.nodelay(True)
      self.max_y,self.max_x = self.game_screen.getmaxyx()
      self.newWord()
      # score screen init #
      self.score_screen=curses.newwin(3,15,2,curses.COLS-20)

      #colour init#
      curses.start_color()
      curses.init_pair(self.pair_cur_index,curses.COLOR_BLACK,curses.COLOR_BLACK)
      curses.init_pair(self.pair_cur_index, self.random_colour, curses.COLOR_BLACK)
      
   #screen update function#
   def update(self,keypressed):
      #random colour#
      curses.init_pair(self.pair_cur_index, self.random_colour, curses.COLOR_BLACK)

      #checks if the key pressed is in selected word if key is correctly pressed then the word will stop going down#
      if str(keypressed) in list(self.selected_word):
         playSound("key_pressed.wav")
         replace_word="*"

         self.selected_word = self.selected_word.replace(keypressed, replace_word,1)
         self.score+=10

      #checks if wrong key is pressed and plays sound#
      else:
         self.game_screen.addstr(self.current_y,self.current_x,self.selected_word,curses.color_pair(2))
         self.current_y +=1
         if keypressed != "":
            playSound("key_not_pressed.wav")
      
     
         



      #checks how much life needs to be reduced and generates another random#
      if self.current_y==self.max_y-1:
         remaining_letters = len(self.selected_word) -self.selected_word.count("*")
         self.life-=remaining_letters*self.LIFE_DEGRADE_FACTOR
         if self.life <= 0:
            self.life = 0
         playSound("explosion.wav")
         self.newWord()

         
      




      life_width=int(self.life/2)
      self.game_screen.addstr(self.current_y-1,self.current_x,self.selected_word,curses.color_pair(2))  
      self.game_screen.addstr(self.current_y,self.current_x,self.selected_word,curses.color_pair(self.pair_cur_index))

     
      #main#
      self.game_screen.border('|', '|', '-', '-', '+', '+', '+', '+')
      self.game_screen.bkgd(' ', curses.color_pair(2) | curses.A_BOLD)
      self.game_screen.refresh()

      #main#
      self.main.border()

      #score#
      self.score_screen.addstr(1,1,"Score : "+ str(self.score).rjust(5,"0"))
      self.score_screen.refresh()

      #life
      self.life_screen_bg.bkgd(' ', curses.color_pair(2))
      self.life_screen_bg.redrawwin()
      self.life_screen_bg.refresh()

      #life text
      self.life_print_screen.addstr(1,2,"LIFE:")
      self.life_print_screen.addstr(2,2,str(self.life).rjust(3,"0"))
      self.life_screen.addstr(0,0," T ")
      self.life_print_screen.refresh()
      curses.curs_set(0)
      
      #checks if life is zero and returns 1 to end the game#
      if self.life<=0:  
         return 1
      
      #resize's the life bar 
      else:
      
         self.life_screen.erase()
         self.life_screen.bkgd(' ', curses.color_pair(4))
         self.life_screen.resize(2,life_width)
         self.life_screen.refresh()

      #checks if the word is completed and call's the newWord function and generates a random word
      if len(self.selected_word)== self.selected_word.count("*"):
         self.newWord()
      
      


   
      #function to clear screen#
   def clear(self):
      self.game_screen.clear()
      curses.endwin()

   #function to generate new word#
   def newWord(self):
      self.random_colour=randint(1, 7)
      self.pair_cur_index += 1
      self.selected_word = choice(self.words)
      self.current_x = randint(0,self.max_x-len(self.selected_word)-1)
      self.current_y = 2


      

