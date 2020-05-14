"""
Main
Entry point into program

Arguments:
  1. command type
  2. music / spotify id
"""
import sys
from jukeflop import JukeFlop

def run(cmd, music_id):
    """
    Runs the whole program
    """
    j = JukeFlop(cmd, music_id)
    j.command()


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
