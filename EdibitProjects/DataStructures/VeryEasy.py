def print_list(n):
    result, i = [], 1
    while i<=n:
        result += [i]
        i += 1
    return result
def nothing_is_nothing(*args):
    if False or None in args:
        return False
    else:
        return True
def last_ind(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[-1]
def fifty_thirty_twenty(ati):
    dict1 = {'Needs': ati * 0.5, 'Wants': ati * 0.3, 'Savings': ati * 0.2}
    return dict1
def assign_person_to_job(names, jobs):
    table1 = {}
    for i in range(len(names)):
        table1[names[i]] = jobs[i]
    return table1
def rotate_by_one(list1):
    for i in range (1, len(list1)):
        list1[0], list1[i] = list1[i], list1[0]
    """
    list1[0], list1[1] = list1[1], list1[0]
    list1[0], list1[2] = list1[2], list1[0]
    list1[0], list1[3] = list1[3], list1[0]
    list1[0], list1[4] = list1[4], list1[0]
    """
    print(list1)
def convert(data1, data2):
    if type(data1) == tuple:
        data2 = tuple(data2)
        return data2
    elif type(data1) == list:
        data2 = list(data2)
        return data2
    elif type(data1) == set:
        data2 = set(data2)
        return data2
def count_unique(word1, word2, count = 0):
    word3 = word1 + word2
    word3 = set(word3)
    for i in word3:
        count +=1
    print(count)
def calculate_losses(dic):
    if sum(dic.values()) == 0:
        return "You're lucky!"
    return sum(dic.values())
def odd_sum_list(list1, list2 = []):
    for i in range(len(list1)-1):
        if (list1[i]+list1[i+1]) % 2 == 0:
            list2.append(True)
        elif (list1[i]+list1[i+1]) % 2 != 0:
            list2.append(False)
    print(list2)



def main():
    #lambda_func = lambda var: var
    #print(lambda_func('4'))
    #print(print_list(6))
    #print(nothing_is_nothing(True, False))
    #print(last_ind([1,2,3]))
    #print(fifty_thirty_twenty(10))
    #names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
    #jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]
    #print(assign_person_to_job(names, jobs))
    rotate_by_one([20, 15, 26, 8, 4, 16,18,95])
    #print(convert((1, 2, 4, 8), [7, 8, 9]))
    #count_unique("apple", "play")
    #print(calculate_losses({}))
    #odd_sum_list([1, 2, 3, 4, 5, 6])

main()
