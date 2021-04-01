from pratice_class import Question
from random import shuffle

c = 'ABCDE'


def read_item_bank(file_name):
    q = open(file_name, 'r', encoding='utf-8')
    item_bank = []
    d = Question()
    
    while True:
        new_line = q.readline()
        if not new_line:
            break

#题干
        if new_line[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            item_bank.append(d)
            d = Question(new_line, [])
            right_answer_number = 0

        if new_line[0] in c:
            d.choice.append(new_line)
            if new_line[-2] == '*':
                right_answer_number += 1

        elif new_line[0] == 'F':
            d.f = int(new_line[1:])
        if right_answer_number > 1:
            d.is_single_choice = False
            
    q.close()

    item_bank.append(d)
    item_bank.pop(0)
    return item_bank


def write_item_bank(file_name, ib):
    q = open(file_name, 'w', encoding='utf-8')
    for i in ib:
        q.write(i.index)
        for j in i.choice:
            q.write(j)
        q.write('F'+str(i.f)+'\n')
    q.close()


def input_answer(ib):
    start = input('start:')
    for i in range(int(start),len(ib)):
        ib[i].show_question()
        answer = input('Please input answer:')
        if answer:
            if answer == "X":
                break
            elif answer == 'S':
                continue
            elif answer in c:
                ib[i].choice[c.find(answer)] = ib[i].choice[c.find(
                    answer)][:-1] + '*' + '\n'
    return ib


def init_item_bank():
    a = read_item_bank('1.txt')
    ib = input_answer(a)
    write_item_bank('200.txt', ib)

def practice1(file_name):
    s = int(input('start at: '))
    a = read_item_bank(file_name)[s:]
    shuffle(a)
    for i in a:
        if i.is_single_choice:
            i.practice_random()
    return a
    
def read_all(file_name):
    a = read_item_bank(file_name)
    #shuffle(a)
    for i in a:
        if i.is_single_choice:
            i.show_question()
            input()
            i.show_answer()
            
if __name__ == "__main__":
    #init_item_bank()
    
    a = practice1('1.txt')
    write_item_bank('1.txt', a)
    #read_all('1.txt')
