import random
from playing_card import PlayingCard

card_suits = ('SPADES', 'CLUBS', 'HEARTS', 'DIAMONDS') # A tuple storing the different card suits.
card_face_values = ('ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING') # A tuple storing the different card ranks
deck = [] # a list to store the deck of cards
cards_in_play = [] # a list to store the cards in play

def set_up_deck():
 '''Set up the card deck - put 52 cards in the deck'''
 card_id = 1  # Every card will be given a unique id from 1 to 52 inclusive. The first card will have an id of 1.

 #Spades Suit
 for i in range(1,14):   # there are 13 cards in a card suit (Ace is 1, King is 13) 
  card = PlayingCard(card_id,card_suits[0],card_face_values[i-1],i)  # create a Card object
  deck.append(card) # append the Card object to the list
  card_id = card_id + 1  # add one to the card_id
 
 #Clubs Suit
 for i in range(1,14):   
  card = PlayingCard(card_id,card_suits[1],card_face_values[i-1],i)  
  deck.append(card) 
  card_id = card_id + 1 
 
 #Hearts Suit
 for i in range(1,14):   
  card = PlayingCard(card_id,card_suits[2],card_face_values[i-1],i)  
  deck.append(card) 
  card_id = card_id + 1 
 
 #Diamonds Suit
 for i in range(1,14):   
  card = PlayingCard(card_id,card_suits[3],card_face_values[i-1],i)  
  deck.append(card) 
  card_id = card_id + 1
  
  
def check_for_duplicate_card(random_card_no):
  '''Check to make sure that a dulicate card won't be generated'''
  found_card = False  # a flag

  # Check to see if the 'random' card is already in the cards_in_play list
  for x in range(0,len(cards_in_play)):
   if random_card_no == cards_in_play[x].get_card_id():
     found_card = True  # update the flag value
     break  # exit the loop
   
  if found_card == True:   # check the value of the flag
   return True
  else:
   return False
   
   
def play():
  '''Starts the game by dealing the first card to the player'''

  # Create a 'random' card. Generate a random number from 1-52 inclusive.
  random_card_no = random.randint(1,52)
  
  # Put the first card into the cards_in_play list.
  cards_in_play.append(deck[random_card_no-1])
  
  # Populate the remaining cards_in_play list - watch out for duplicate cards.
  while len(cards_in_play) != 3:
    # Create a 'random' card. Generate a random number from 1-52 inclusive.
    random_card_no = random.randint(1,52)
    
    if check_for_duplicate_card(random_card_no) == False:
     cards_in_play.append(deck[random_card_no-1]) # append to the list of cards_in_play
   
   
def compute_game_winner():
  '''Determines who wins the game, the house or the player'''
  # variable to count the score of the player
  player_score = 0
    
  # variable to store the game boundary score (21)
  boundary_score = 21
  
  #Iterate over the cards_in_play list
  for i in range(0,len(cards_in_play)): # 3 cards in play
    print(cards_in_play[i])
    player_score = player_score + cards_in_play[i].get_card_face_value() # tot up the player's score
      
  #Finally, determine who won the game
  if player_score <= boundary_score:
   print('\nPatron wins!', player_score, 'is less than', boundary_score)
  else:    
   print('\nHouse wins!', player_score, 'is greater than', boundary_score)
   print('\nBetter luck next time! We value your custom. Thanks for playing.')
  

print('\n*************Welome to BlackJack - the game of 21!*************'.center(30))
print('\nThe computer will deal three random cards.')
print('To win, the total value of the three cards dealt must be less than or equal to 21. Otherwise, house wins!')
print('Start Game...\n')

set_up_deck()

play()
 
compute_game_winner()







