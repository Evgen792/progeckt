from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QCheckBox

class StartWidget(QWidget):
    def __init__(self, btn_exitClicked, btn_enterClicked):
        super().__init__()
        self.question = QLabel("<center>Готовы ли вы пройти тест?</center>")
        self.btn_enter = QPushButton("Да")
        self.btn_exit = QPushButton("Выход")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btn_enter)
        self.hbox.addWidget(self.btn_exit)
        self.question.setObjectName('LabelTestWindow')
        self.btn_exit.clicked.connect(btn_exitClicked)
        self.btn_enter.clicked.connect(btn_enterClicked)
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addLayout(self.hbox)
        self.setLayout(vbox)
        

class TestWidget1(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        self.question_1 = QLabel("<center>Вопрос 1: Какой формат используется для изображений в интернете?</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1: BMP")
        self.rb2 = QRadioButton("Ответ 2: JPEG")
        self.rb3 = QRadioButton("Ответ 3: TIFF")
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        # self.question.setObjectName("LabelQuestionTestWindow")
        vbox = QVBoxLayout()
        vbox.addWidget(self.question_1)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)
        

class TestWidget2(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        self.question_2 = QLabel("<center>Вопрос 2: Какие форматы видеозаписей поддерживает сайт?</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1: AVI, MP4, 3GP, MPEG, MOV, MP3")
        self.rb2 = QRadioButton("Ответ 2: FLV, WMV, MKV, TS, VOB.")
        self.rb3 = QRadioButton("Ответ 3: Оба варианта верны")
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        # self.question.setObjectName("LabelQuestionTestWindow")
        self.btn_next.clicked.connect(btn_nextClicked)
        vbox = QVBoxLayout()
        vbox.addWidget(self.question_2)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)
        

class TestWidget3(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        self.question_3 = QLabel("<center>Вопрос 3: Какой формат используется для изображений в интернете?</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1: PHP, JavaScript, ActionScript, HTML, CSS")
        self.rb2 = QRadioButton("Ответ 2: Python, CSS, HTML")
        self.rb3 = QRadioButton("Ответ 3: C++, HTML, CSS,")
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        # self.question.setObjectName("LabelQuestionTestWindow")
        vbox = QVBoxLayout()
        vbox.addWidget(self.question_3)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)

class TestWidget4(QWidget):
    
    def __init__(self, btn_nextClicked):
        super().__init__()
        
        self.question_4 = QLabel("<center>Вопрос 4: Какие существуют языки программирования?</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QCheckBox(" PHP")
        self.rb2 = QCheckBox(" Python")
        self.rb3 = QCheckBox(" Java ")
        self.rb4 = QCheckBox(" HTML")
        self.rb5 = QCheckBox(" C++")
        self.rb6 = QCheckBox(" Go ")
        self.rb7 = QCheckBox(" C--")
        self.rb8 = QCheckBox(" Picha/")
        self.rb9 = QCheckBox(" Hotop")
        self.rb10 = QCheckBox(" PIP")
        self.rb11 = QCheckBox(" HPH")
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        # self.question.setObjectName("LabelQuestionTestWindow")
        vbox = QVBoxLayout()
        vbox.addWidget(self.question_4)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.rb4)
        vbox.addWidget(self.rb5)
        vbox.addWidget(self.rb6)
        vbox.addWidget(self.rb7)
        vbox.addWidget(self.rb8)
        vbox.addWidget(self.rb9)
        vbox.addWidget(self.rb10)
        vbox.addWidget(self.rb11)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)

            

class EndWidget(QWidget):
    def __init__(self,  question_1 = None, question_2 = None, question_3 = None):
        super().__init__()
        self.txt = QLabel(f"Пользователь успешно прошел тест, результаты сохранены в файле (test.txt)")
        self.txt.setObjectName("LabelQuestionTestWindow")
        vbox = QVBoxLayout()
        vbox.addWidget(self.txt)
        self.setLayout(vbox)
        
        with open ("test.txt", "w", encoding="utf-8") as f:
            f.write("Тест") 
        