import discord
from game import Game


class GameState():
    """
    The GameState class represents a finite state machine that determines the state of the poker game
    """
    def __init__(self):
        self.game = None
        self.game_state = State.NO_GAME

    def process_command(self, message: discord.Message, command: str) -> None:
        if command == "?poker":
            self.process_new_game(message, command)
        elif command == "?join":
            self.process_new_player()
        elif command == "?deal":
            self.process_dealing()
        elif command == "?check":
            self.process_player_check()
        elif command == "?call":
            self.process_player_call()
        elif command == "?raise":
            self.process_player_raise()
        elif command == "?fold":
            self.process_player_fold()
        elif command == "?allin":
            self.process_player_all_in()
        elif command == "?help":
            await message.channel.send("help command")
        elif command == "?exit":
            self.game = None
            self.game_state = State.NO_GAME
            await message.channel.send("The game has ended, thanks for playing!")
        else:
            await message.channel.send("Command not recognized, please type `?help` to see the list of commands.")

    def process_new_game(self, message: discord.Message, commands: str):
        if self.game_state == State.NO_GAME:
            self.game = Game(commands)
            self.game_state = State.WAIT_FOR_PLAYERS
            await message.channel.send("The poker game is currently looking for players\n" +
                                       "Type `?join` to join the game\n" +
                                       "Type '?deal` to start the game")
        elif self.game_state == State.WAIT_FOR_PLAYERS:
            await message.channel.send("The poker game is currently looking for players\n" +
                                       "Type `?join` to join the game\n" +
                                       "Type '?deal` to start the game")
        else:
            await message.channel.send("The Poker game has already started.")

    def process_new_player(self, message: discord.Message):
        if self.game_state == State.NO_GAME:
            await message.channel.send("The poker game has not started yet\n" +
                                       "Type `?poker` to start looking for players")
        elif self.game_state == State.WAIT_FOR_PLAYERS:
            self.game.add_player(message.author)
            await message.channel.send('{} has joined the poker game.'.format(message.author.name))
        else:
            # add the player, but wait for next round

    def process_deal_hands(self, message: discord.Message):
        if self.game_state == State.NO_GAME:
            await message.channel.send("The poker game has not started yet\n" +
                                       "Type `?poker` to start looking for players")
        elif self.game_state == State.WAIT_FOR_PLAYERS:
            self.game_state = State.DEALING
            self.game.deal_hands()
            # print out the first three cards
        elif self.game_state == State.BETTING_FLOP:
        elif self.game_state == State.BETTING_TURN:
        elif self.game_state == State.BETTING_RIVER:



    def process_

    def process_player_check(self):

    def process_player_call(self):
        if self.game_state == State.BETTING_FLOP:
        elif self.game_state == State.BETTI

    def process_player_raise(self):


    def process_player_fold(self):

    def process_player_all_in(self):
        # check if the player is still in


