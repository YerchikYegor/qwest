import json


with open('1.json', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())


class Qwest():
    def __init__(self, text, diff, answer):
        self.text = text
        self.diff = diff
        self.answer = answer

        self.ans_user = None
        self.score = self.get_point()

    def build_question(self):
        return f'Вопрос: {self.text}\nСложность {self.diff}/5'

    def is_corect(self):
        if self.ans_user == self.answer:
            return True
        else:
            return False

    def get_point(self):
        return self.diff + 10

    def build_positive_feedback(self):
        if self.is_corect():
            return  f'Правильно!!! получено {self.score} баллов.'
        else:
            return 'Не правильно '
qwest_list = []
for q in data:
    qwest_list.append(Qwest(q['text'],q['diff'], q['answer']))
for qwest in qwest_list:
    print(qwest.build_question())
    qwest.ans_user = input('ведите ответ')
    print(qwest.is_corect())
    print(qwest.get_point())
    print(qwest.build_positive_feedback())