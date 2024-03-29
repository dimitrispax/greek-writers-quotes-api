import json
import random

# Path to the JSON file
json_file_path = './data/quotes.json'

# Load JSON data from the file
with open(json_file_path, 'r') as file:
  quotes = json.load(file)

##########################################
# They get the quotes from the JSON file.#
##########################################

def get_randomized_quote():
  # Generate a random integer that will become the index of the shuffled list.
  random_index = random.randint(1, len(quotes))

  # Shuffle the quote list 
  random.shuffle(quotes)

  return quotes[random_index]

def get_shuffled_quotes():
  # Shuffle the quote list 
  random.shuffle(quotes)

  return quotes