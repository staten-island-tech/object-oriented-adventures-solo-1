player_data = None
player_class = None

def update(data):
  global player_data, player_class
  player_data = data.__dict__
  player_class = data