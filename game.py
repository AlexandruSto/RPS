#stabileste castigatoru pe baza datelor oferite
#ofera date despre starea fiecarui jucator: daca a alses sau nu, etc

class Game:
    def __init__(self, id):
        self.p1Went = False# verifica daca player 1 a facut alegerea
        self.p2Went = False
        self.ready = False# verfica daca ambii playeri sunt conectati
        self.id = id#player id
        self.moves = [None, None]# lista cu miscari a playerilor


    def get_player_move(self, p):
        """
        parametru este playerul, fct returneza alegerea playerului
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move# atribuie miscarea fiecarui player
        if player == 0:#verifica daca player 1 sau 2 au facut alegerea
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready# returneaza starea conexiunii

    def bothWent(self):
        return self.p1Went and self.p2Went# verifica daca ambii playeri au mers

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        # fucntia de rock paper scissors

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False#reseteaza starea playerilor pt a putea juca din nou