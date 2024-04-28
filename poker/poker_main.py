from auxilliary import BuildTree, UCB
import numpy as np
from numpy.random import binomial, choice
from POMCP.poker.poker_generator import Generator
from pomcp import POMCP
from timeit import default_timer as timer
from time import sleep
from joblib import Parallel, delayed, parallel_backend
from utils import generate_random_game_state, generate_random_game_observation

import sys
sys.path.insert(0, './pypokerengine/api/')
import game
setup_config = game.setup_config
start_poker = game.start_poker

# A = ['fold', 'call', 'raise']
# S = generate_random_game_state # The actual generator function
# O = generate_random_game_observation # The actual generator function

# # setup start
# ab = POMCP(Generator,gamma = 0.5)
# ab.initialize(S,A,O)

# # Calculate policy in a loop
# time = 0
# while time <= 10:
#     time += 1
#     action = ab.Search()
#     print(ab.tree.nodes[-1][:4])
#     print(action)
#     observation = choice(O)
#     ab.tree.prune_after_action(action,observation)
#     ab.UpdateBelief(action, observation)




import numpy as np
from fow_chess.board import Board
from fow_chess.chesscolor import ChessColor
from fow_chess_generator import (
    FogChessGenerator as Generator,
    get_action_mask,
    action_index_to_move,
)
from pomcp import POMCP

if __name__ == "__main__":
    A = ['fold', 'call', 'raise']
    S = generate_random_game_state # The actual generator function
    O = generate_random_game_observation # The actual generator function
    # action_mask = get_action_mask(board)

    # setup start
    ab = POMCP(Generator, gamma=0.9, timeout=1000, no_particles=300)
    ab.initialize(S, A, O)

    # Calculate policy in a loop
    time = 0
    history = []

    max_round = 1000
    initial_stack = 10000
    smallblind_amount = 20
    # Init pot of players
    agent1_pot = 0
    agent2_pot = 0
    # Setting configuration
    config = setup_config(max_round=max_round, initial_stack=initial_stack, small_blind_amount=smallblind_amount)
    
    # Register players
    config.register_player(name=agent_name1, algorithm=POMCPPlayer())
    config.register_player(name=agent_name2, algorithm=RandomPlayer())
    while time <= 100:
        game_result = start_poker(config, verbose=0)

        action = ab.Search()
        # print(ab.tree.nodes[-1][:4])
        move_str = str(action_index_to_move(board, action))
        print(move_str)
        history.append(move_str)
        winner = board.apply_move(action_index_to_move(board, action))
        if winner is not None:
            print("Winner is", winner)
            break
        observation = board.to_fow_fen(board.side_to_move)  # choice(O)
        print(observation)
        print(board)
        ab.tree.prune_after_action(action, observation)
        ab.UpdateBelief(action, observation)

		# agent1_pot = agent1_pot + game_result['players'][0]['stack']
		# agent2_pot = agent2_pot + game_result['players'][1]['stack']
        time += 1
    print(history)