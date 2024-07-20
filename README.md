## Greek Writers Quotes API

Is a simple application designed to show quotes from renowned Greek writers and poets. Utilizing Flask, a minimal web server grants users access to a curated collection of quotes sourced from various books and poems.

### Writers & Poets available:

- C. P. Cavafy
- Kiki Dimoula
- Odysseas Elytis
- Katerina Gogou
- Nikos Kazantzakis
- Giannis Ritsos
- Giorgos Seferis

# Using the API

#### Get a random quote

```
GET {URL}/api/quote
```

##### Example JSON response

```json
{
  "author": "Nikos Kazantzakis",
  "quote": "I hope for nothing. I fear nothing. I am free."
}
```

#### Get the list with all quotes

```
GET {URL}/api/quotes
```

##### Example JSON response

```json
[
  {
    "author": "C.P. Cavafy",
    "quote": "And if you find her poor, Ithaca has not deceived you. Wise as you have become, with so much experience, you must already have understood what these Ithacas mean."
  },
  {
    "author": "Kiki Dimoula",
    "quote": "Love grows by not giving to us. And if our passion for poetry lives on and persists, it is because poetry offers us only its bits of lint."
  },
  {
    "author": "Giorgos Seferis",
    "quote": "Every man of action has a strong dose of egoism, pride, hardness, and cunning. But all those things will be regarded as high qualities if he can make them the means to achieve great ends."
  }
]
```

# Running the app locally
1. Ensure that you have ```python3``` installed with ```python3 -V``` command.
2. ```pip3 install -U flask```
3. ```pip3 install -U flask-cors```
4.  ```flask --app app run```