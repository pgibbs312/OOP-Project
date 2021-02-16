import random
class Maze:

    def __init__(self, file_name):
        self._file_name=open(file_name,'r')
        self._lines=self._file_name.readlines()




    def can_move_to(self, line_num, col_num):
        self._line_num=line_num
        self._col_num=col_num
        charac = self._lines[self._line_num][self._col_num]
        if charac == "X":
            return False
        else:
            return True


            

    def display(self):
        for item in self._lines:
            print(item)




    def find_random_spot(self):
        dicton=[]
        i=0
        for line in self._lines:
            j=0
            for charac in line:
                if charac == " ":
                    dicton.append((i,j))
                j=j+1
            i=i+1
        return random.choice(dicton)






    