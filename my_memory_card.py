#создай приложение для запоминания информации
from PyQt5.QtCore import Qt #подключаем библеотеки
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QGroupBox,QButtonGroup#подключаем библиотеки и классы
from random import shuffle #поключаем модули

programma= QApplication([])#создаем оконое приложение
glavnoe_okno=QWidget()#создаем главное окно
glavnoe_okno.setWindowTitle('Тест')
glavnoe_okno.move(900,70)
glavnoe_okno.resize(400,200)#устанавливаем высоту и ширину
glavnoe_okno.cur_question=-1
question_list=[]
class Question():#создаем класс которая будет опредилять правильный ответ дал пользователь или нет
    def __init__(self,vopros,variant1,variant2,variant3,variant4):
        self.question=vopros
        self.right_answer=variant1
        self.wrong1=variant2
        self.wrong2=variant3
        self.wrong3=variant4

def ask(q:Question):#создаем функцию
    vopros.setText(q.question)
    shuffle(answer)#здесь смешиваются ответы
   
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    pravil.setText(q.right_answer)
 
    show_question()#вызываем функцию

def next_question():
    glavnoe_okno.cur_question+=1
    if glavnoe_okno.cur_question > len(question_list):
        glavnoe_okno.cur_question=0
    q=question_list[glavnoe_okno.cur_question]
    ask(q)

def check_answer():#создаем функцию 
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    # если выбран кнопка answers[0], то установить в виджет resltat текст 'Правильно!'
    if answer[0].isChecked():
        resltat.setText('Правильно')
    # иначе, установить 'Неверно!'
    else:
        resltat.setText('Не правильно')
    show_answer()
    # вызываем функцию show_answer

def show_question():#создаем функцию
    buttonGroup.setExclusive(False)
    variant1.setChecked(False)
    variant2.setChecked(False)
    variant3.setChecked(False)
    variant4.setChecked(False)
    buttonGroup.setExclusive(True)

    gruppavopros.show()#показываем вопрос
    gruppaotvet.hide()#скрываем ответ
    knopka.setText('Ответить')
def show_answer():#создаем функцию для того что бы показать правильный ответ 
    gruppavopros.hide()#спрятать вопрос
    gruppaotvet.show()#показать ответ
    knopka.setText('Следующий вопрос')
def start():#создаем функцию обработка клика по кнопке
    if knopka.text()=='Ответить':
        check_answer()
        # вызывать функцию проверки ответа
    else:
        next_question()

vopros=QLabel('Какой национальности не существует')#создаем виджет вопрос
 
gruppavopros=QGroupBox('Вариант ответа')#создаем виджет группу

variant1=QRadioButton('Энцы')
variant2=QRadioButton('Смурфы')
variant3=QRadioButton('Чулымцы')
variant4=QRadioButton('Алеуты')
answer = [variant1,variant2,variant3,variant4]

naprav_gruppa=QVBoxLayout()
naprav_gruppa.addWidget(variant1)
naprav_gruppa.addWidget(variant2)
naprav_gruppa.addWidget(variant3)
naprav_gruppa.addWidget(variant4)
gruppavopros.setLayout(naprav_gruppa)
buttonGroup=QButtonGroup()
buttonGroup.addButton(variant1)
buttonGroup.addButton(variant2)
buttonGroup.addButton(variant3)
buttonGroup.addButton(variant4)

knopka=QPushButton('Ответить')

gruppaotvet=QGroupBox('Результат')#
resltat=QLabel('Правильно')
pravil=QLabel('тут будет правильный ответ')
gruppanapravotvet=QVBoxLayout()
gruppanapravotvet.addWidget(resltat)
gruppanapravotvet.addWidget(pravil)#ghb
gruppaotvet.setLayout(gruppanapravotvet)#привязываем к направляющей
gruppaotvet.hide()#скрытие группу ответа для скрытия вопроса

glavnapr = QVBoxLayout()
glavnapr.addWidget(vopros)
glavnapr.addWidget(gruppavopros)
glavnapr.addWidget(gruppaotvet)
glavnapr.addWidget(knopka)
glavnoe_okno.setLayout(glavnapr)
knopka.clicked.connect(start)

q1=Question('Какой национальности не существует?','Энцы','Смурфы','Чулымцы','Алеуты')
q2=Question('2+5?','7','2','5','9')
q3=Question('5+5?','10','4','676','0')
q4=Question('567+3?','570','345','5689','569')
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
next_question()
glavnoe_okno.show()

programma.exec_()