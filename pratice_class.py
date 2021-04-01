from random import shuffle
# from speech import say, recognize

c = 'ABCDE'


class Question():
    def __init__(
            self,
            index="",
            choice=[],
            is_single_choice=True,
            f=30):
        self.index = index
        self.choice = choice
        self.is_single_choice = is_single_choice
        self.f = f

    def show_question(self):
        print('#' * self.f + '-' * (60 - self.f))
        print(self.index)
        for i in range(len(self.choice)):
            if self.choice[i][-2] == '*':
                print(c[i] + '.' + self.choice[i][2:-2])
            else:
                print(c[i] + '.' + self.choice[i][2:-1])
#        say(self.index,'zh-CN')
#        for i in range(len(self.choice)):
#            if self.choice[i][-2] == '*':
#                say(c[i] + '.' + self.choice[i][2:-2], 'zh-CN')
#            else:
#                say(c[i] + '.' + self.choice[i][2:-1], 'zh-CN')

    def show_answer(self):
        print('#' * self.f + '-' * (60 - self.f))
        for i in range(len(self.choice)):
            if self.choice[i][-2] == '*':
                print(c[i] + '.' + self.choice[i][2:-2])
                # say('答案是' + c[i] + '.' + self.choice[i][2:-2], 'zh-CN')

    def shuffle_answer(self):
        shuffle(self.choice)

    def practice_sequence(self):
        if self.f == 0:
            return 1
        self.show_question()
        chosen = input(
            "\n 'ABCDE' to chose answer, 'Q' to Quit, 'R' to Remove Qusition, 'S' to show answer:\t"
        )
        if chosen in c:
            if self.check_answer(chosen):
                pass
            else:
                print('X' * 60 + '\n')
                self.practice_sequence()
        elif chosen == 'Q':
            return 0
        elif chosen == 'R':
            self.f = 0
        elif chosen == 'S':
            self.show_answer()
        else:
            print('Please try again')
            self.practice_sequence()
        return 1

    def check_answer(self, chosen):
        if self.choice[c.find(chosen)][-2] == '*':
            return 1
        else:
            return 0

    def practice_random(self):
        self.shuffle_answer()
        self.practice_sequence()


if __name__ == "__main__":
    q = Question("问题", ['A.正确答案*\n',
                        'B.错的\n', 'C.错的\n', 'D.还是错的\n', 'E.都是错的\n'])
    #	q.show_question()
    #	q.show_answer()
    q.practice_random()
