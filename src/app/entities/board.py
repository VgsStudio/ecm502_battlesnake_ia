
from typing import List, Optional

from ..entities.battlesnake import Battlesnake
from ..entities.coordinate import Coordinate


class Board:
  height: int
  width: int
  food: List[Coordinate]
  snakes: List[Coordinate]
  hazards: List[Battlesnake]

  def __init__(self, height: int, width: int, food: List[Coordinate], snakes: List[Coordinate], hazards: List[Battlesnake]):
      self.food = food
      self.height = height
      self.width = width
      self.snakes = snakes
      self.hazards = hazards


  def __eq__(self, other):
      return self.height == other.height and self.width == other.width and self.food == other.food and self.snakes == other.snakes and self.hazards == other.hazards

  def __repr__(self):
      return f"Board: {self.width}x{self.height}"

  @staticmethod
  def from_json(json):
      height = json["height"]
      width = json["width"]
      food = [Coordinate.from_json(food) for food in json["food"]]
      snakes = [Battlesnake.from_json(snake) for snake in json["snakes"]]
      hazards = [Coordinate.from_json(hazard) for hazard in json["hazards"]]
      return Board(height, width, food, snakes, hazards)

  @staticmethod
  def navigate_to(start: Coordinate, end: Coordinate) -> str:
      if start.x < end.x:
          return "right"
      elif start.x > end.x:
          return "left"
      elif start.y < end.y:
          return "up"
      elif start.y > end.y:
          return "down"
      else:
          return "up"
    
  def reconstruct_path(self, came_from: dict, current: Coordinate) -> List[Coordinate]:
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]
      
  def find_path(self, start: Coordinate, end: Coordinate) -> List[Coordinate]:
        
        if end is None:
            return []
        if start == end:
            return [start]
        
        open_set = [start]
        came_from = {}
        g_score = {start: 0}
        f_score = {start: Coordinate.heuristic_function(start, end)}
    
        while open_set:
            current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
    
            if current == end:
                return self.reconstruct_path(came_from, current)
    
            open_set.remove(current)
    
            for neighbor in self.get_valid_neighbors(current):
                tentative_g_score = g_score.get(current, float('inf')) + 1
    
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + Coordinate.heuristic_function(neighbor, end)
                    if neighbor not in open_set:
                        open_set.append(neighbor)
    
        return []

  def get_path_to_all_foods(self, me: Battlesnake) -> List[List[Coordinate]]:
      paths = []
      for food in self.food:
          path = self.find_path(me.head, food)
          if path:
              paths.append(path)
      return paths
  
  def get_path_to_closest_food(self, me: Battlesnake) -> List[Coordinate]:
        if len(self.food) == 0:
            return []
        paths = self.get_path_to_all_foods(me)
        paths.sort(key=lambda x: len(x))
        if len(paths) > 0:
            return paths[0]
        return []
  
  def get_all_foods(self):
        return self.food

  def get_valid_neighbors(self, head: Coordinate) -> List[Coordinate]:
      neighbors = []
      for move in ["right", "down", "left", "up"]:
          if self.can_move(move, head):
              new_coordinate = head.move_command(move)
              neighbors.append(new_coordinate)
      return neighbors

  def is_snake(self, move: str, head: Coordinate):
      coordinate = head.move_command(move)
      for snake in self.snakes:
          if snake.is_inside_snake(coordinate):
              return snake
      return False
  
  def get_closest_food(self, me: Battlesnake) -> Optional[Coordinate]:
        closest_food = None
        min_distance = float('inf')
        for food in self.food:
            distance = Coordinate.distance(me.head, food)
            if distance < min_distance:
                min_distance = distance
                closest_food = food
        return closest_food
  
  def is_hazard(self, move: str, head: Coordinate):
      coordinate = head.move_command(move)
      for hazard in self.hazards:
          if hazard == coordinate:
              return True
      return False

  def dodge_snake_body(self, me: Battlesnake, old_move: str):
      if  self.can_move(old_move, me.head):
          return old_move

      for move in ["up", "down", "left", "right"]:
          if self.can_move(move, me.head):
              return move
      return old_move
  
  def can_move(self, move: str, coordinate: Coordinate) -> bool:
        if self.is_out_of_bounds(move, coordinate) or self.is_snake(move, coordinate) or self.is_hazard(move, coordinate):
            return False
        return True

  def is_out_of_bounds(self, move: str, head: Coordinate):
      coordinate = head.move_command(move)
      if coordinate.x < 0 or coordinate.x >= self.width or coordinate.y < 0 or coordinate.y >= self.height:
          return True
      return False
  
  def safe_random_move(self, me: Battlesnake) -> str:
        for move in ["up", "down", "left", "right"]:
            if self.can_move(move, me.head) and not self.is_near_snake(me.head.move_command(move), me):
                return move
        return "up"  # Default move if no safe moves are available
  
  def is_near_snake(self, coordinate: Coordinate, me: Battlesnake) -> bool:
        for snake in self.snakes:
            if Coordinate.distance(snake.head, coordinate) <= 1 and snake.snake_id != me.snake_id:
                return True
        return False  
