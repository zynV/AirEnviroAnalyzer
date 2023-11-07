import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QPushButton, QComboBox
import pandas as pd

class FlightAnalysisApp(QMainWindow):
    def __init__(self, data_file):
        super().__init__()

        self.setWindowTitle("Анализ перелетов")
        self.setGeometry(100, 100, 800, 600)

        # Создаем вкладки
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Вкладка с круговой диаграммой
        self.tab1 = QWidget(self)
        self.tabs.addTab(self.tab1, "Круговая диаграмма")

        layout = QVBoxLayout(self.tab1)

        # Создаем выпадающий список для выбора поля анализа
        self.field_combobox = QComboBox()
        self.field_combobox.addItem("Возраст")
        self.field_combobox.addItem("Пол")
        self.field_combobox.addItem("Национальность")
        layout.addWidget(self.field_combobox)

        # Создаем кнопку для обновления диаграммы
        self.update_button = QPushButton("Обновить диаграмму")
        layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.update_diagram)

        # Создаем холст для круговой диаграммы
        self.figure, self.ax = plt.subplots()
        layout.addWidget(self.figure.canvas)

        # Загрузка данных из CSV-файла
        self.data = pd.read_csv(data_file)

    def update_diagram(self):
        field = self.field_combobox.currentText()

        if field == "Возраст":
            data = self.data["Age"]
        elif field == "Пол":
            data = self.data["Gender"]
        elif field == "Национальность":
            data = self.data["Nationality"]

        if len(data) == 0:
            print("Нет данных для анализа.")
            return

        labels = data.value_counts().index
        values = data.value_counts().values

        # Создаем круговую диаграмму
        self.ax.clear()
        self.ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        self.ax.axis('equal')
        self.figure.canvas.draw()

if __name__ == '__main__':
    data_file = "Airline Dataset.csv"
    app = QApplication(sys.argv)
    window = FlightAnalysisApp(data_file)
    window.show()
    sys.exit(app.exec_())
