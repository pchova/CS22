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
        self.__leagueGamesWon = won
    
    #Setter Methods for TeamSport class
    def set_position(self, pos):
        self.__position = pos

    def set_leagueGamesWon(self, won):
        self.__leagueGamesWon = won

    #Getter Methods for TeamSport class
    def get_position(self):
        return self.__position
    
    def get_leagueGamesWon(self):
        return self.__leagueGamesWon
    
class IndividualSport(Athlete):
    #IndividualSport constructor accepts 5 parameters
    def __init__(self, name, country, sport, winnings, mc):
        super().__init__(name, country, sport)

        self.__totalWinnings = winnings
        self.__playerChampionshipsWon = mc
    
    #Setter Methods for IndividualSport class
    def set_totalWinnings(self, win):
        self.__totalWinnings = win

    def set_playerChampionshipsWon(self, mc):
        self.__playerChampionshipsWon = mc

    #Getter Methods for IndividualSport class
    def get_totalWinnings(self):
        return self.__totalWinnings
    
    def get_playerChampionshipsWon(self):
        return self.__playerChampionshipsWon



    

    
