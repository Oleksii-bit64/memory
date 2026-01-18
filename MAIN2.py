from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QRadioButton, QWidget,
    QGroupBox, QVBoxLayout, QLabel, QHBoxLayout, QButtonGroup
)
class Question():

    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


Question_list = []
q1 = Question("Чому дорівнюе чісло п?", "3,1415", "3,90", "5,44", "6,14")
q2 = Question("скіки буде 34 * 98", "3332", "3232","6555", "893" )
q3 = Question("яка скорость света в км","299 792", "22222", "5433",  "444444444")
q4 = Question("Как называется самая большая планета", "Юпитер", "земля",'марс','сонце')
q5 = Question("Сколько континентов на Земле", '6', '5', '7', '8')
q6 = Question("Какой океан самый глубокий",'тихий', "атлантический", "южный", "индийский")
q7 = Question('Кто написал роман «Война и мир»?', "Лев Толстой", "Лев не Толстой", "лев", "лев толстых")
q8 = Question("Сколько градусов в прямом угле?", "90", "100", "360", "80")
q9 = Question("Какой газ необходим человеку для дыхания?", "Кислород", '', '',"")
q10 = Question("Столица Японии?", "Токио", "", "", "")
q11 = Question('Как называется самая длинная река в мире?', "Нил", "нал", "нул", "нел")
q12 = Question("Сколько хромосом у здорового человека?", "46", "45", "32", "79")
q13 = Question("Какой металл обозначается символом Fe?", "Железо", "", "", "")
q14 = Question("В каком году человек впервые высадился на Луну?", "1969", "196", "1956", "1945")
q15 = Question("Как называется наука о прошлом человечества?", "История", "", "", "")






Question_list.append(q1)
Question_list.append(q2)
Question_list.append(q3)
Question_list.append(q4)
Question_list.append(q5)
Question_list.append(q6)
Question_list.append(q7)
Question_list.append(q8)
Question_list.append(q9)
Question_list.append(q10)
Question_list.append(q11)
Question_list.append(q12)
Question_list.append(q13)
Question_list.append(q14)
Question_list.append(q15)





app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")

btn_ok = QPushButton("Відповідь")
lb_question = QLabel("Дуже складне запитаня")
radioGroupBox = QGroupBox("Варианти відповидей")


rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")

layot_ans1 = QHBoxLayout()

layot_ans2 = QVBoxLayout()
layot_ans3 = QVBoxLayout()

layot_ans2.addWidget(rbtn_1)
layot_ans2.addWidget(rbtn_2)
layot_ans3.addWidget(rbtn_3)
layot_ans3.addWidget(rbtn_4)


layot_ans1.addLayout(layot_ans2)
layot_ans1.addLayout(layot_ans3)

radioGroupBox.setLayout(layot_ans1)


ansGroupBox = QGroupBox("Результат")
lb_result = QLabel("Correct")
lb_correct = QLabel("Correct answer")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, 0, (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, 2, Qt. AlignHCenter)
ansGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_question, 0, Qt.AlignCenter)
layout_line2.addWidget(radioGroupBox)
layout_line2.addWidget(ansGroupBox)
ansGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, 2)
layout_card.addLayout(layout_line2, 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, 1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

window.setLayout(layout_card)
window.show()
window.resize(700, 500)

radioGroup = QButtonGroup()
radioGroup.addButton (rbtn_1)
radioGroup.addButton (rbtn_2)
radioGroup.addButton (rbtn_3)
radioGroup.addButton(rbtn_4)

def show_result():

    radioGroupBox.hide()
    ansGroupBox.show()
    btn_ok.setText("Powered Up")
def show_question():
    ansGroupBox.hide()
    radioGroupBox.show()
    btn_ok.setText("Video")
    radioGroup.setExclusive (False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked (False)
    rbtn_4.setChecked (False)
    radioGroup.setExclusive (True)






answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]



def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers [2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()
def show_correct(result):
    lb_result.setText(result)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Correct")
        window.score += 1
    else:
        if answers[1].isChecked() or answers [2].isChecked() or answers [3].isChecked():
            show_correct("Not correct")





def next_question():
    window.total += 1
    cur_question = randint(0, len(Question_list) -1)

    q = Question_list[cur_question]
    ask(q)



def click_ok():
    if btn_ok.text() == "Video":
        check_answer()
        print("ваша статистика:")
        print("всього відповідей:", window.total)
        print("правельних відповідей:", window.score)
        print("ваш рейдінг:", (window.score / window.total * 100), "%")
    else:
        next_question()

window.total = 0
window.score = 0


btn_ok.clicked.connect(click_ok)
next_question()


     



app.exec_()




