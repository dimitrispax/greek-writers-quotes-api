import json
import random

json_file_path = './data/quotes.json'

# Load the quotes from the file containing them
with open(json_file_path, 'r') as file:
  quotes = json.load(file)

def get_randomized_quote():
  random_index = random.randint(0, len(quotes) - 1)
  
  # Suffling the quotes list to increase the entropy
  random.shuffle(quotes)

  return quotes[random_index]

def get_shuffled_quotes():
  random.shuffle(quotes)

  return quotes