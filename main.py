import sys

from PyQt5.QtWidgets import QApplication

from main_window import TestDegree


def main():
    app = QApplication(sys.argv)
    ex = TestDegree()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
