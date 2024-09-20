import json

with open('1.txt', 'r', encoding='utf-8') as file:
    a = file.read()
list_qwest = json.loads(a)
print(list_qwest)


class Qwest():
    def __init__(self, text, diff, answer):
        self.text = text
        self.diff = diff
        self.answer = answer

        self.ans_user = None
        self.score = self.get_point()

    def get_point(self):
        return self.diff + 10

    def is_corect(self):
        if self.ans_user == self.answer:
            return True
        else:
            return False

    def build_question(self):
        print(self.text)
        print(self.diff)

    def build_positive_feedback(self):
        if self.is_corect():
            print('Правильно!!! получено ', self.score,'баллов.')
        else:
            print('Не правильно ')