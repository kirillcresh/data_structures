import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTabWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QSplitter,
    QMessageBox,
    QCheckBox,
)
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from lab_1 import get_power_result
from lab_2 import get_list_method


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
        splitter_2 = QSplitter(Qt.Vertical)

        upper_widget_2 = QWidget()
        upper_layout_2 = QVBoxLayout()
        self.list_window(upper_layout_2)
        upper_widget_2.setLayout(upper_layout_2)

        self.lower_widget_2 = QWidget()
        self.lower_layout_2 = QVBoxLayout()
        self.figure_2 = plt.figure()
        self.canvas_2 = FigureCanvas(self.figure_2)
        self.lower_layout_2.addWidget(self.canvas_2)
        self.lower_widget_2.setLayout(self.lower_layout_2)

        splitter_2.addWidget(upper_widget_2)
        splitter_2.addWidget(self.lower_widget_2)
        splitter_2.setSizes([150, 350])
        layout2.addWidget(splitter_2)
        tab2.setLayout(layout2)

        tab3 = QWidget()
        layout3 = QVBoxLayout()
        layout3.addWidget(QLabel("Содержимое третьей вкладки"))
        tab3.setLayout(layout3)

        self.tabs.addTab(tab1, "Лабораторная 1")
        self.tabs.addTab(tab2, "Лабораторная 2")
        self.tabs.addTab(tab3, "Лабораторная 3")

    def power_window(self, layout: QVBoxLayout):
        title = QLabel()
        title.setFixedSize(550, 20)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        title.setText("Быстрое возведение в степень")
        methods = [
            "Обычный способ",
            "Модуль numpy",
            "Рекурсивное возведение",
            "Быстрое возведение в степень",
            "Быстрое побитовое возведение",
        ]
        self.method_checkboxes = []
        self.input_pairs = []

        layout.addWidget(title)
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
        selected_methods = [
            checkbox.text()
            for checkbox in self.method_checkboxes
            if checkbox.isChecked()
        ]

        if not selected_methods:
            self.show_warning(
                "Пожалуйста, выберите хотя бы один метод возведения в степень."
            )
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
                    self.show_warning(
                        "Пожалуйста, введите числовые значения в оба поля: число и степень."
                    )
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

        ax.set_title("Сравнение методов возведения в степень")
        ax.set_xlabel("Число для возведения в степень")
        ax.set_ylabel("Время выполнения (микросекунды)")
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

    def list_window(self, layout: QVBoxLayout):
        title = QLabel()
        title.setFixedSize(550, 20)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        title.setText("Односвязанные и двусвязанные списки")
        methods = [
            "Добавление в начало",
            "Добавление в конец",
            "Добавление в середину",
            "Поиск",
            "Поиск по индексу",
            "Удаление",
            "Удаление по индексу",
        ]
        self.method_checkboxes = []

        method_layout = QHBoxLayout()
        for method in methods:
            checkbox = QCheckBox(method)
            method_layout.addWidget(checkbox)
            self.method_checkboxes.append(checkbox)
        layout.addWidget(title)
        layout.addLayout(method_layout)

        test_button = QPushButton("Тест")
        test_button.clicked.connect(self.test_lists)
        layout.addWidget(test_button)

    def test_lists(self):
        selected_methods = [
            checkbox.text()
            for checkbox in self.method_checkboxes
            if checkbox.isChecked()
        ]
        if not selected_methods:
            self.show_warning(
                "Пожалуйста, выберите хотя бы один метод возведения в степень."
            )
        time_result = {"standard": {}, "sll": {}, "dll": {}}
        for method in selected_methods:
            for type_list in ("standard", "sll", "dll"):
                if not time_result[type_list].get(method):
                    time_result[type_list][method] = []
                start_time = time.perf_counter()
                get_list_method(method, type_list)
                end_time = time.perf_counter()
                time_result[type_list][method] = (
                    (end_time - start_time) * 10
                    if method
                    in ("Поиск", "Поиск по индексу", "Удаление", "Удаление по индексу")
                    else end_time - start_time
                )
        self.plot_test_results(time_result)

    def plot_test_results(self, time_result):
        self.canvas_2.figure.clear()
        axes = self.canvas_2.figure.subplots(1, 3, sharey=True)

        list_types = ['standard', 'sll', 'dll']
        methods = list(next(iter(time_result.values())).keys())
        colors = ['#3498db', '#e74c3c', '#2ecc71']

        for idx, list_type in enumerate(list_types):
            times = [time_result[list_type][method] for method in methods]
            axes[idx].barh(methods, times, color=colors[idx])
            axes[idx].set_title(f'Тип списка: {list_type.capitalize()}')
            axes[idx].set_xlabel('Время (сек)')
            axes[idx].set_yticks(range(len(methods)))
            axes[idx].set_yticklabels(methods)

        # Перерисовка холста
        self.canvas_2.draw()
