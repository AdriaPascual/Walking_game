import sys
from walking.game import Game

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    
    print("Main module is speaking")

    game = Game()
    game.run()


if __name__ == '__main__':
    sys.exit(main())

