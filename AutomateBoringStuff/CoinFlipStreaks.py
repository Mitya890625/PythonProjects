from random import randint
def main():
    numberOfStreaks = 0
    for i in range (10000):
        cont = list_of_HT()
        numberOfStreaks += streak_check(cont)
    percents = numberOfStreaks/10000
    print(str(percents)+'%')
def list_of_HT():
    cont = [randint(0,1) for x in range(100)]   #генерирование списка со 100 элементами
    return cont
def streak_check(cont):
    numberOfStreaks = 0
    streak = 0
    for i in range(len(cont)):
        if cont[i] == cont[i-1]: #проверка на совпадение следующего подбрасывания с предыдущим
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks +=1 # подсчет серий одинаковых результатов подбрасываний
    return numberOfStreaks


main()

