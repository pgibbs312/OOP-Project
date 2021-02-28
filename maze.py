import random

class Maze:
    """
    Class representing the maze 

    :Param file_name: the nameof the text file that traces the maze
    :Type file_name: string
    """
    def __init__(self, file_name_):
        #self._file_name=open(file_name,'r')
        #self._lines=self._file_name.readlines()
            #Not how that works

        with open(file_name_,'r') as my_file:
            lines_=my_file.readlines()
            #print(self._lines)
            # for item in self._lines:
            #     print(item)
        self._lines = lines_
        
        #self.items = 

   
    def can_move_to(self, line_num, col_num):
        #self._line_num=line_num  
        #self._col_num=col_num    
            
             # Never declare an attribute outside of the init method
             # There wasn't a point in doing it like that anyway

        #charac = self._lines[self._line_num][self._col_num]
        charac = self._lines[line_num][col_num]
        if charac == "X":
            return False
        else:
            return True

    def display(self):
        for item in self._lines:
            print(item)

    def find_random_spot(self):
        """
        Method made to randomly select *empty spaces* in the maze
        and place objects in them.

        :Param 
        """
        dicton=[] #Why is it called this?
        for i,line in enumerate(self._lines):
            
            for j,charac in enumerate(line):
                if charac == " ":
                    dicton.append((i,j))
                
        return random.choice(dicton)

    #def is_item(self):

if __name__=="__main__":
    maze_file="maze.txt"
    my_maze = Maze(maze_file)
    my_maze.display()






    