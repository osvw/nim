class Nim(object):
    """Das Nim-Spiel, siehe https://de.wikipedia.org/wiki/Nim-Spiel"""

    def __init__(self, sticks):
        """Initialisiert, wie wie viele Streichhölzer verwenden werden"""
        self.sticks = sticks

    def player_move(self, user_input):
        """Handhabt den Spielzug des Spielers"""
        try:
            player_sticks = int(user_input)
        except ValueError:
            print("\nDu musst eine Zahl eingeben!")
            return False

        if( player_sticks > self.sticks ):
            print("\nEs sind keine " + str(player_sticks) + " Hölzer mehr übrig, bitte nimm weniger!")
            return False

        if( player_sticks > 3 or player_sticks < 1 ):
            print("\nDu musst zwischen 1 und 3 Hölzer nehmen!")
            return False

        return player_sticks

    def computer_move(self, player_sticks):
        """Handhabt den Spielzug des Computer.
           Dieser zieht immer so, dass die Zahl der Streichhölzer
           ungerade bleibt und somit der menglische Spieler verliert.
        """
        computer_choices = { 1: 3, 2: 2, 3: 1 }
        computer_sticks = computer_choices[player_sticks];
        print("\nDer Computer nimmt " + str(computer_sticks) + " Hölzer.")
        return computer_sticks

    def execute(self):
        """Die Spielroutine, nimmt die Eingeben entgegen und leitet
           diese an die jeweiligen move-Methoden weiter
        """
        print("\nEs sind noch " + str(self.sticks) + " Hölzer übrig.");
        while True:
            player_sticks = False
            while(player_sticks == False):
                player_sticks = self.player_move(input("\nWie viele Hölzer möchtest du nehmen (Zahl ziwschen 1 und 3)? "));

            self.sticks += -player_sticks;

            if(self.sticks == 0):
                break

            print("\nEs sind noch " + str(self.sticks) + " Hölzer übrig.");
            computer_sticks = self.computer_move( player_sticks );
            self.sticks += -computer_sticks;

            if(self.sticks == 0):
                break

            print("\nEs sind noch " + str(self.sticks) + " Hölzer übrig.");

        print("\nDu hast leider verloren.\n");
