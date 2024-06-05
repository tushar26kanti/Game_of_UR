import csv
import time
import os

class GameRecorder:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.filename = f"{int(time.time())}.csv"
        self.filepath = os.path.join(self.data_dir, self.filename)
        os.makedirs(self.data_dir, exist_ok=True)
        self.initialize_file()

    def initialize_file(self):
        with open(self.filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header if needed, example: game_state features + move
            header = [f"feature_{i}" for i in range(20)] + ["move"]
            writer.writerow(header)

    def record_move(self, game_state, move):
        with open(self.filepath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(game_state + [move])
