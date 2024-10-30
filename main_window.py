import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QTabWidget, QHBoxLayout, QLineEdit, QPushButton, \
    QSplitter, QMessageBox, QCheckBox
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from lab_1 import get_power_result


class TestDegree(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Быстрое возведение в степень")
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        available_geometry = screen.availableGeometry()
        available_width = available_geometry.width()
        taskbar_height = screen_geometry.height() - available_geometry.height()
        available_height = available_geometry.height() - int(round(taskbar_height / 2))
        self.setFixedSize(available_width, available_height)

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)
        self.create_tabs()
        self.show()

    def create_tabs(self):
        tab1 = QWidget()
        main_layout = QVBoxLayout()
        splitter = QSplitter(Qt.Vertical)

        upper_widget = QWidget()
        upper_layout = QVBoxLayout()
        self.power_window(upper_layout)
        upper_widget.setLayout(upper_layout)

        self.lower_widget = QWidget()
        self.lower_layout = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.lower_layout.addWidget(self.canvas)
        self.lower_widget.setLayout(self.lower_layout)

        splitter.addWidget(upper_widget)
        splitter.addWidget(self.lower_widget)
        splitter.setSizes([150, 350])

        main_layout.addWidget(splitter)
        tab1.setLayout(main_layout)

        tab2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Содержимое второй вкладки"))
        tab2.setLayout(layout2)

        tab3 = QWidget()
        layout3 = QVBoxLayout()
        layout3.addWidget(QLabel("Содержимое третьей вкладки"))
        tab3.setLayout(layout3)

        self.tabs.addTab(tab1, "Лабораторная 1")
        self.tabs.addTab(tab2, "Лабораторная 2")
        self.tabs.addTab(tab3, "Лабораторная 3")

    def power_window(self, layout: QVBoxLayout):
        methods = ["Обычный способ", "Модуль numpy", "Рекурсивное возведение", "Быстрое возведение в степень",
                   "Быстрое побитовое возведение"]
        self.method_checkboxes = []
        self.input_pairs = []

        method_layout = QHBoxLayout()
        for method in methods:
            checkbox = QCheckBox(method)
            method_layout.addWidget(checkbox)
            self.method_checkboxes.append(checkbox)
        layout.addLayout(method_layout)

        self.exponent_input = QLineEdit()
        self.exponent_input.setPlaceholderText("Степень")
        layout.addWidget(self.exponent_input)

        for _ in range(5):
            input_layout = QHBoxLayout()
            num_input = QLineEdit()
            num_input.setPlaceholderText("Число")
            second_num_input = QLineEdit()
            second_num_input.setPlaceholderText("Число")

            input_layout.addWidget(num_input)
            input_layout.addWidget(second_num_input)
            layout.addLayout(input_layout)

            self.input_pairs.append(num_input)
            self.input_pairs.append(second_num_input)

        test_button = QPushButton("Тест")
        test_button.clicked.connect(self.test_powers)
        layout.addWidget(test_button)

    def test_powers(self):
        selected_methods = [checkbox.text() for checkbox in self.method_checkboxes if checkbox.isChecked()]

        if not selected_methods:
            self.show_warning("Пожалуйста, выберите хотя бы один метод возведения в степень.")
            return

        num_values = []
        exponent_text = self.exponent_input.text().strip()
        if not exponent_text:
            self.show_warning("Пожалуйста, введите степень.")
            return

        for num_input in self.input_pairs:
            num_text = num_input.text().strip()
            if num_text:
                try:
                    num = int(num_text)
                    exponent = int(exponent_text)
                    num_values.append(num)
                except ValueError:
                    self.show_warning("Пожалуйста, введите числовые значения в оба поля: число и степень.")
                    return
        if not num_values:
            self.show_warning("Пожалуйста, введите хотя бы одно число.")
            return
        self.generate_comparative_plot(selected_methods, num_values, exponent)

    def generate_comparative_plot(self, methods, num_values, exponent):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        time_results = {method: [] for method in methods}

        for num in num_values:
            for method in methods:
                start_time = time.perf_counter()
                get_power_result(method, num, exponent)
                end_time = time.perf_counter()
                time_results[method].append((end_time - start_time) * 1000000)
        for method, times in time_results.items():
            ax.plot(num_values, times, label=method, marker="o")

        ax.set_title('Сравнение методов возведения в степень')
        ax.set_xlabel('Число для возведения в степень')
        ax.set_ylabel('Время выполнения (микросекунды)')
        ax.legend()
        ax.grid(True)
        self.canvas.draw()

    @staticmethod
    def show_warning(message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Ошибка ввода")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
