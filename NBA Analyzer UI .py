import matplotlib as plt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem
import pandas as pd
class NBAAnalyzerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('NBA Data Analyzer')
        self.setGeometry(100, 100, 800, 600)  # Set the initial window size

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.min_points_label = QLabel('Minimum Points:')
        self.min_points_input = QLineEdit(self)

        self.max_points_label = QLabel('Maximum Points:')
        self.max_points_input = QLineEdit(self)

        self.analyze_button = QPushButton('Analyze Data', self)
        self.analyze_button.clicked.connect(self.analyze_data)

        self.result_table = QTableWidget(self)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.min_points_label)
        layout.addWidget(self.min_points_input)
        layout.addWidget(self.max_points_label)
        layout.addWidget(self.max_points_input)
        layout.addWidget(self.analyze_button)
        layout.addWidget(self.result_table)

        self.setLayout(layout)

        self.show()

    def analyze_data(self):
        try:
            min_points = float(self.min_points_input.text())
            max_points = float(self.max_points_input.text())

            filtered_data = nba_data[(nba_data['PTS'] >= min_points) & (nba_data['PTS'] <= max_points)]

            self.show_filtered_data(filtered_data)

        except ValueError:
            self.show_error('Invalid input. Please enter valid numbers.')

    def show_filtered_data(self, data):
        self.result_table.clear()

        if data.empty:
            self.result_table.setRowCount(1)
            self.result_table.setItem(0, 0, QTableWidgetItem('No data found within the specified range.'))
        else:
            self.result_table.setRowCount(len(data))
            self.result_table.setColumnCount(len(data.columns))
            self.result_table.setHorizontalHeaderLabels(data.columns)

            for row_index, row in data.iterrows():
                for col_index, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.result_table.setItem(row_index, col_index, item)

    def show_error(self, message):
        error_label = QLabel(message, self)
        error_label.setStyleSheet('color: red')
        self.layout().addWidget(error_label)

if __name__ == '__main__':
    # Load NBA data from CSV
    nba_data = pd.read_csv(r'C:/Users/Shrav/OneDrive/Desktop/VSC Projects!/venv/2023_nba_player_stats.csv')

    app = QApplication(sys.argv)
    nba_app = NBAAnalyzerApp()
    sys.exit(app.exec_())

