####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Project 1
# Due Date: October 20 2025
####################################################

class Athlete:
    #Athlete constructor accepts 3 parameters
    def __init__(self, name, country, sport):
        self.__name = name
        self.__country = country
        self.__sport = sport

    #Setter Methods for Athlete class
    def set_name(self, n):
        self.__name = n
    
    def set_country(self, c):
        self.__country = c
    
    def set_sport(self, s):
        self.__sport = s

    #Getter Methods for Athlete class
    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country
    
    def set_sport(self):
        return self.___sport
    
class TeamSport(Athlete):
    #TeamSport constructor accepts 5 parameters
    def __init__(self, name, country, sport, pos, won):
        super().__init__(name, country, sport)

        self.__position = pos
        self.__gamesWon = won
    
    #Setter Methods for TeamSport class
    def set_position(self, pos):
        self.__position = pos

    def set_gamesWon(self, won):
        self.__gamesWon = won

    #Getter Methods for TeamSport class
    def get_position(self):
        return self.__position
    
    def get_gamesWon(self):
        return self.__gamesWon
    
