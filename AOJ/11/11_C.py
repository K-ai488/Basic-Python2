class Dice:
    def set_data(self,set_top,set_front,set_right,set_left,set_back,set_bottom):
        self.top = set_top
        self.front = set_front
        self.right = set_right
        self.left = set_left
        self.back = set_back
        self.bottom = set_bottom

    def dicemove(self,direction):
        if direction == "E":
            self.top,self.right,self.left,self.bottom = self.left,self.top,self.bottom,self.right
        elif direction == "N":
            self.top,self.front,self.back,self.bottom = self.front,self.bottom,self.top,self.back
        elif direction == "S":
            self.top,self.front,self.back,self.bottom = self.back,self.top,self.bottom,self.front
        elif direction == "W":
            self.top,self.right,self.left,self.bottom = self.right,self.bottom,self.top,self.left # 入力によってサイコロを転がす

top1,front1,right1,left1,back1,bottom1= map(int, input().split())
top2,front2,right2,left2,back2,bottom2= map(int, input().split())

dice1 = Dice()
dice1.set_data(top1,front1,right1,left1,back1,bottom1)

dice2 = Dice()
dice2.set_data(top2,front2,right2,left2,back2,bottom2)

check = 0  #　サイコロが同じであると認識した場合1にする

for l in range(3):
    if l == 1:
        dice1.dicemove("E")
        dice1.dicemove("S")
    if l == 2:
        dice1.dicemove("S")
        dice1.dicemove("S")
    for j in range(5):
        if j != 0:
            dice1.dicemove("S")
        for i in range(5):
            if i != 0:
                dice1.dicemove("E")
            if dice1.top == dice2.top and dice1.front == dice2.front and dice1.right == dice2.right and dice1.left == dice2.left and dice1.back == dice2.back and dice1.bottom == dice2.bottom:
                check = 1
                break

if check == 1:
    print("Yes")
else:
    print("No")
