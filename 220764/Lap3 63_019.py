#63011212019
score = []
for i in range(5):
    score.append(float(input("นิสิตคนที่ "+str(i+1)+" คะแนน : ")))
    sum = 0.0
    Count = 0
for i in range(5):
    if score[i] < 0 or score[i] > 100:
        print("Error")
        score[i] = 0
        Count +=1
    elif score[i] >= 80:
        print('นิสิตคนที่', i+1,'คะแนน = %.2f, เกรด = A'% score[i])
    elif score[i] >= 70:
        print('นิสิตคนที่', i+1,'คะแนน = %.2f, เกรด = B'% score[i])
    elif score[i] >= 60:
        print('นิสิตคนที่', i+1,'คะแนน = %.2f, เกรด = C'% score[i])
    elif score[i] >= 50:
        print('นิสิตคนที่', i+1,'คะแนน = %.2f, เกรด = D'% score[i])
    else:
        print('นิสิตคนที่', i+1,'คะแนน = %.2f, เกรด = F'% score[i])
    sum += score[i]
print('คะแนนรวมนิสิต = %.2f' %(sum/(5-Count)))
