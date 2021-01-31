CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class TileDisplay():
    #giving num_rows and num_cols will make a rectangular display
    #giving grid will make a display that only shows values in the grid
    #coordinate list
    def __init__(self, num_rows=None, num_cols=None, grid=None, default_char="0"):
        if grid and not num_rows and not num_cols:

            #find enclosing dimensions of grid
            max_x = 0
            max_y = 0
            for x,y in grid:
                max_x = max(x,max_x)
                max_y = max(y,max_y)

            #use standard constructor
            self.__init__(num_rows=max_x+1, num_cols=max_y+1, default_char=" ")

            #color in valid areas with zeroes
            for x,y in grid:
                self.display[x][y] = "0"
        elif num_rows and num_cols:
            self.current_index = 0
            self.num_rows = num_rows
            self.num_cols = num_cols
            #final information to display
            self.display = [[default_char for c in range(num_cols)] for r in range(num_rows)]
            #keeping track of errors
            self.out_of_bounds_chars = []
            self.overlap_chars = []
        else:
            #enforce construction rules since python doesn't let you overload constructors
            raise ValueError("only give both num_rows and num_cols or just a grid")

    #adds a tile at the given location
    #will do nothing if given tile=None
    def add_tile(self, location, tile):
        if tile == None:
            return

        character = CHARACTERS[self.current_index]
        self.current_index += 1
        #loop around if use too many tiles
        self.current_index = self.current_index % len(CHARACTERS)
        x,y = location
        for square in tile:
            x_offset, y_offset = square
            xp = x+x_offset
            yp = y+y_offset
            #only display valid squares
            if(0 <= xp < self.num_rows and 0 <= yp < self.num_cols and self.display[xp][yp] == "0"):
                self.display[xp][yp] = character
            elif self.display[xp][yp] != "0" and self.display[xp][yp] != " ":
                #report overlap error
                self.overlap_chars.append((character,self.display[xp][yp]))
            else:
                #report out of bounds error
                self.out_of_bounds_chars.append(character)
    def __str__(self):
        result = ""

        #display overlap error info
        if len(self.overlap_chars) > 0:
            result += "Overlap error: "
            result += ", ".join([top+" on "+bottom for top, bottom in self.overlap_chars])
            result += "\n"

        #display out of bounds error info
        if len(self.out_of_bounds_chars) > 0:
            result += "Out of bounds error at tiles: "
            result += ", ".join(self.out_of_bounds_chars)
            result += "\n"

        #pretty margin
        for i in range(self.num_cols):
            result += "*"
        
        result += "\n"

        #print body
        for i in range(len(self.display)):
            line = self.display[i]
            for character in line:
                result += character
            
            result += "\n"

        #pretty margin
        for i in range(self.num_cols):
            result += "*"
        
        return result

if __name__ == "__main__":
    disp = TileDisplay(5,5)
    print(disp)
    print()
    disp.add_tile((1,1),[(0,0),(0,1),(1,1)])
    print(disp)
    print()
    disp.add_tile((3,3),[(0,0),(0,1),(1,1)])
    print(disp)
    print()

    disp = TileDisplay(grid=[(0,0),(1,0),(0,1)])
    print(disp)
    disp.add_tile((0,0),[(0,0),(0,1)])
    print(disp)
    disp.add_tile((1,0),[(0,0),(0,1)])
    print(disp)
    disp.add_tile((1,0),[(0,0),(0,1)])
    print(disp)