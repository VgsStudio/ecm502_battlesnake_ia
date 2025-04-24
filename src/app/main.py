import random
from fastapi import FastAPI
from mangum import Mangum
from .entities.battlesnake import Battlesnake
from .entities.board import Board

app = FastAPI()

# GET / - info about the snake (https://docs.battlesnake.com/api/requests/info)
# POST /start - start the game (https://docs.battlesnake.com/api/requests/start)
# POST /move - move the snake (https://docs.battlesnake.com/api/requests/move)
# POST /end - end the game (https://docs.battlesnake.com/api/requests/end)

@app.get("/")
def read_root():
    return {
        "apiversion": "1",
        "author": "SoBrRuMaSA",
        "color": "#FFDE21",
        "head": "ski",
        "tail": "weight",
        "version": "1.0.0"
    }

@app.post("/start") 
def start():
    return "ok"

@app.post("/move")
def move(request: dict):
    print(request)

    board = Board.from_json(request["board"])
    me = Battlesnake.from_json(request["you"])

    path = board.get_path_to_closest_food(me)
    if len(path) > 0:
        
        next_move = board.navigate_to(me.head, path[1])
    else:
        next_move = board.safe_random_move(me)

    response = {
        "move": next_move,
        "shout": f"I'm moving {next_move}!"
    }
    return response

@app.post("/end")
def end():
    return "ok"

handler = Mangum(app, lifespan="off")