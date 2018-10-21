from random import randint

name = raw_input('请输入你的名字：') #输入玩家名字

f = open('e:\py\game.txt')
lines = f.readlines()
f.close()

scores = () #初始化一个空字典
for l in lines:
    s = l.split() #把每一行的数据分成list
    scores[s[0]] = s[1:] #第一项作为key，剩下的作为value
score = scores.get(name) #查找当前玩家的数据
if score is None: #如果没找到
    score =[0, 0, 0] #初始化数据

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times =0
#加上显示玩家的名字
print '%s,你已经玩了第%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name,game_times,min_times,avg_times)

num = randint(1,100)
times = 0
bingo =False
while bingo == False:
    times +=1
    answer = input()
    if answer < num:
        print 'too small'
    if answer > num:
        print 'too big'
    if answer == num:
        print 'BINGO!'
        bingo=True

if game_times ==0 or times <min_times:
    min_times = times
total_times +=times
game_times +=1

#把成绩更新到对应得玩家数据中
#加str转成字符串，为后面的格式化作准备
scores[name] = [str(game_times),str(min_times),str(total_times)]
result ='' #初始化一个空字符串，用来存储数据
for n in scores:
    #把成绩按照先 名字 游戏次数 最小次数 总次数 格式化
    #结尾要加上\n换行
    line = n + ' ' + ' '.join(score[n]) + '\n'
    result += line #添加到result中

f= open('e:\py\game.txt', 'w')
f.write(result)
f.close()
