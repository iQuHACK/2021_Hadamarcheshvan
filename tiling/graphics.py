CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class TileDisplay():
    def __init__(self, num_rows, num_cols):
        self.current_index = 0
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.display = [["0" for c in range(num_cols)] for r in range(num_rows)]
    def add_tile(self, location, tile):
        character = CHARACTERS[self.current_index]
        self.current_index += 1
        #loop around if use too many tiles
        self.current_index = self.current_index % len(CHARACTERS)
        x,y = location
        for square in tile:
            x_offset, y_offset = square
            xp = x+x_offset
            yp = y+y_offset
            self.display[xp][yp] = character
    def __str__(self):
        result = ""
        for i in range(len(self.display)):
            line = self.display[i]
            for character in line:
                result += character
            #no new line for the last one
            if i != len(self.display)-1:
                result += "\n"
        return result
