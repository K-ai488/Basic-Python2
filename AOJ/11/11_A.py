class Dice:
    def set_data(self,set_top,set_front,set_right,set_left,set_back,set_bottom):
        self.top = set_top
        self.front = set_front
        self.right = set_right
        self.left = set_left
        self.back = set_back
        self.bottom = set_bottom

    def print_data(self):
        print(self.top) # サイコロの上にきた値を出力する

    def dicemove(self,direction):
        if direction == "E":
            self.top,self.right,self.left,self.bottom = self.left,self.top,self.bottom,self.right
        elif direction == "N":
            self.top,self.front,self.back,self.bottom = self.front,self.bottom,self.top,self.back
        elif direction == "S":
            self.top,self.front,self.back,self.bottom = self.back,self.top,self.bottom,self.front
        elif direction == "W":
            self.top,self.right,self.left,self.bottom = self.right,self.bottom,self.top,self.left # 入力によってサイコロを転がす

top,front,right,left,back,bottom= map(int, input().split())

dice = Dice()
dice.set_data(top,front,right,left,back,bottom)

move = input()
for i in move:
  dice.dicemove(i)

dice.print_data()
