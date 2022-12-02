def unique_sort(arr):
    arr = sorted(set(arr))
    return arr
def get_students_names(dict1):
    students_list = []
    for students in dict1:
        students_list.append(dict1[students])
    return sorted(students_list)
def integer_boolean(s):
    bool_list = []
    for i in s:
        if i == '1':
            bool_list.append(True)
        if i == '0':
            bool_list.append(False)
    return bool_list
def upload_count(dates, month):
    count = 0
    for i in range(len(dates)):
        if month in dates[i]:
            count += 1
    return count
def find_bob(list1):
    i = 0
    while i < len(list1):
        if list1[i] == 'Bob':
            return i
        i += 1
    if 'Bob' not in list1:
        return -1
def count_all(s):
    counter_dict = {}
    counter_dict['LETTERS'] = 0
    counter_dict['NUMBERS'] = 0
    for i in s:
        if i.isalpha():
            counter_dict['LETTERS'] += 1
        elif i.isdigit():
            counter_dict['NUMBERS'] += 1
    return counter_dict
def color_invert(rgb):
    rgb = list(rgb)
    for i in range(len(rgb)):
        rgb[i] -= 255
        rgb[i] *= -1
    return tuple(rgb)
def matrix(x, y, z):
    list_m = []
    for i in range(x):
        list_m.append([])
        for j in range(y):
            list_m[i].append(z)
    return list_m
def find_ocurrences(sentence, letter):
    sentence_dict = {}
    sentence_list = sentence.split(' ')
    for word in sentence_list:
        sentence_dict[word] = 0
        for i in word:
            if letter == i:
                sentence_dict[word] += 1
    return sentence_dict
def oldest(peoples):
    for name in peoples:
        if peoples[name] == max(peoples.values()):
            return name












def main():
    #print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
    #print(get_students_names({
 # "Student 1" : "Steve",
 # "Student 2" : "Becky",
 # "Student 3" : "John"}))
    #print(integer_boolean('10011'))
    #print(upload_count(['Sep 13','Sep 15', 'Oct 15'], 'Sep'))
    #print(find_bob(["Jimmy", "Layla", "Bob"]))
    #print(count_all('149990'))
    #print(color_invert((165, 170, 221)))
    #print(matrix(3, 2, 0))
    #print(find_ocurrences("create a nice juicy function", "e"))
    print(oldest({"Max": 9,
  "Josh": 13,
  "Sam": 48,
  "Anne": 33}))


main()
