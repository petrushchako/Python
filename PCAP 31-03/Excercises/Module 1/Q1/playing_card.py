#Define a class to model a PlayingCard
class PlayingCard:
  
  def __init__(self, card_id, card_suit, card_rank, card_face_value):
    # A Card has a unique id (ex.1), is of a certain card suit (ex.Spades), has a rank (ex. Jack) and has a face value (ex.11).
    self.__card_id = card_id         # ex. 1
    self.__card_suit = card_suit     # ex. Spades
    self.__card_rank = card_rank     # ex. Jack
    self.__card_face_value = card_face_value  # ex. 11
    
  def get_card_id(self):
    return self.__card_id
    
  def get_card_suit(self):
    return self.__card_suit;
  
  def get_card_rank(self):
    return self.__card_rank
    
  def get_card_face_value(self):
    return self.__card_face_value
  
  def __str__(self):
    return str(self.__card_rank).upper() + ' of ' + self.__card_suit.upper() + ' Card Value: (' + str(self.__card_face_value) + ')'
    
    

    
 