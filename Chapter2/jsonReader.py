import json
from pprint import pprint

with open("pokemon.json") as f:
    data = json.loads(f.read())
    pprint(data)

Edit json:
{
  "id": 25,
  "name": "Pikachu",
  "type": [
    "Electric"
  ],
  "isLegendary": false,
  "stats": {
    "hp": 35,
    "attack": 55,
    "defense": 40
  },
  "moves": [
    {
      "name": "Thunder Shock",
      "power": 40
    },
    {
      "name": "Quick Attack",
      "power": 40
    }
  ]
}
