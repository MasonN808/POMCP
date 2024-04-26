import random

#TODO: Think about ways to make this smarter like configuring the random distributions away from random uniform across all potential values (e.g., skewed gaussian)

# Define suits, ranks, and generate the full deck of cards
suits = ['C', 'D', 'H', 'S']  # Clubs, Diamonds, Hearts, Spades
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [f"{suit}{rank}" for rank in ranks for suit in suits]

# Define maximum pot and rounds (as string for easy formatting)
max_pot = 99999 # TODO: probably less
max_rounds = 99999 # TODO: probably less

# Function to randomly select exactly two cards for each player
def get_two_cards():
    selected_cards = random.sample(deck, 2)
    return selected_cards

# Function to generate a random game state
def generate_random_game_state() -> str:
    # Randomly select the number of community cards between 2 and 5
    num_community_cards = random.randint(2, 5)
    community_cards = random.sample(deck, num_community_cards)
    # Fill the remaining card slots with "00" up to 5 cards
    community_cards += ['00'] * (5 - num_community_cards)
    
    remaining_deck = list(set(deck) - set(community_cards))

    # Randomly select two hole cards for each player from the remaining deck
    player1_cards = random.sample(remaining_deck, 2)
    remaining_deck = list(set(remaining_deck) - set(player1_cards))
    player2_cards = random.sample(remaining_deck, 2)

    # Randomly select pot and round numbers, and format them
    pot = random.randint(1, max_pot)
    rounds = random.randint(1, max_rounds)

    # Combine all parts into the final encoded string
    game_state = f"{''.join(community_cards)}|{str(pot).zfill(5)}|{str(rounds).zfill(5)}|{''.join(player1_cards)}|{''.join(player2_cards)}"
    return game_state


def generate_random_game_observation() -> str:
    # Randomly select the number of community cards between 2 and 5
    num_community_cards = random.randint(2, 5)
    community_cards = random.sample(deck, num_community_cards)
    # Fill the remaining card slots with "00" up to 5 cards
    community_cards += ['00'] * (5 - num_community_cards)
    
    remaining_deck = list(set(deck) - set(community_cards))

    # Randomly select two hole cards for each player from the remaining deck
    player1_cards = random.sample(remaining_deck, 2)
    remaining_deck = list(set(remaining_deck) - set(player1_cards))
    player2_cards = random.sample(remaining_deck, 2)

    # Randomly select pot and round numbers, and format them
    pot = random.randint(1, max_pot)
    rounds = random.randint(1, max_rounds)

    # Combine all parts into the final encoded string
    game_state = f"{''.join(community_cards)}|{str(pot).zfill(5)}|{str(rounds).zfill(5)}|{''.join(player1_cards)}|{''.join("0000")}"
    return game_state


if __name__ == "__main__":
    print(generate_random_game_observation())