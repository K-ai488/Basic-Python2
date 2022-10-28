class Dice:
    def set_data(self,set_top,set_front,set_right,set_left,set_back,set_bottom):
        self.top = set_top
        self.front = set_front
        self.right = set_right
        self.left = set_left
        self.back = set_back
        self.bottom = set_bottom
    
    def print_data(self):
        print(self.top,self.front,self.right,self.left,self.back,self.bottom) # サイコロの上にきた値を出力する

    def dicemove(self,direction):
        if direction == "E":
            self.top,self.right,self.left,self.bottom = self.left,self.top,self.bottom,self.right
        elif direction == "N":
            self.top,self.front,self.back,self.bottom = self.front,self.bottom,self.top,self.back
        elif direction == "S":
            self.top,self.front,self.back,self.bottom = self.back,self.top,self.bottom,self.front
        elif direction == "W":
            self.top,self.right,self.left,self.bottom = self.right,self.bottom,self.top,self.left # 入力によってサイコロを転がす

n =int(input())
dice = [[]*6]*n


for s in range(n):
    top,front,right,left,back,bottom= map(int, input().split())
    dice[s] = Dice()
    dice[s].set_data(top,front,right,left,back,bottom) 


check = 0  #　サイコロが同じであると認識した場合1にする
for k in range(n-1):
  for m in range(n-1-k):
    for l in range(3):
      if l == 1:
        dice[k].dicemove("E")
        dice[k].dicemove("S")
      if l == 2:
        dice[k].dicemove("S")
        dice[k].dicemove("S")
      for j in range(5):
        if j != 0:
          dice[k].dicemove("S")
        for i in range(5):
          if i != 0:
            dice[k].dicemove("E")
          if dice[k].top == dice[k+m+1].top and dice[k].front == dice[k+m+1].front and dice[k].right == dice[k+m+1].right and dice[k].left == dice[k+m+1].left and dice[k].back == dice[k+m+1].back and dice[k].bottom == dice[k+m+1].bottom:
            check = 1
            break

if check == 1:
    print("No")
else:
    print("Yes")
