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
    
    def get_sport(self):
        return self.__sport
    
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

def main():
    wayne = TeamSport('Wayne Gretzky', 'Canada', 'Hockey', 'Center', 4)
    tom = TeamSport('Tom Brady', 'United States', 'Football', 'Quarterback', 7)
    lionel = TeamSport('Lionel Messi', 'Argentina', 'Soccer', 'Forward', 14)
    roger = IndividualSport('Roger Federer', 'Switzerland', 'Tennis', 130594339, 20)
    rory = IndividualSport('Rory Mcllroy', 'Northern Ireland', 'Golf', '125147336', 4)

    team = [wayne, tom, lionel]
    indy = [roger, rory]

    for player in team:
        print(f"{player.get_name()} is from {player.get_country()} and plays {player.get_sport()}.")
        print(f"He played {player.get_position()} and won {player.get_leagueGamesWon()} league championships.")
        print()
    
    for person in indy:
        print(f"{person.get_name()} is from {person.get_country()} and plays {person.get_sport()}.")
        print(f"He earned ${person.get_totalWinnings()} and won {person.get_playerChampionshipsWon()} major championships.")
        print()

               

main()

    

    
