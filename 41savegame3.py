from random import randint

name = raw_input('������������֣�') #�����������

f = open('e:\py\game.txt')
lines = f.readlines()
f.close()

scores = () #��ʼ��һ�����ֵ�
for l in lines:
    s = l.split() #��ÿһ�е����ݷֳ�list
    scores[s[0]] = s[1:] #��һ����Ϊkey��ʣ�µ���Ϊvalue
score = scores.get(name) #���ҵ�ǰ��ҵ�����
if score is None: #���û�ҵ�
    score =[0, 0, 0] #��ʼ������

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times =0
#������ʾ��ҵ�����
print '%s,���Ѿ����˵�%d�Σ�����%d�ֲ³��𰸣�ƽ��%.2f�ֲ³���' % (name,game_times,min_times,avg_times)

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

#�ѳɼ����µ���Ӧ�����������
#��strת���ַ�����Ϊ����ĸ�ʽ����׼��
scores[name] = [str(game_times),str(min_times),str(total_times)]
result ='' #��ʼ��һ�����ַ����������洢����
for n in scores:
    #�ѳɼ������� ���� ��Ϸ���� ��С���� �ܴ��� ��ʽ��
    #��βҪ����\n����
    line = n + ' ' + ' '.join(score[n]) + '\n'
    result += line #��ӵ�result��

f= open('e:\py\game.txt', 'w')
f.write(result)
f.close()
