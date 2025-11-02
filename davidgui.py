import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QFrame
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

def truncate_to_2_digits(value):
    return int(value * 100) / 100.0

class CholeraSurvivalPredictor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Cholera Survival Predictor")
        self.setGeometry(100, 100, 550, 470)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f2ff;
                font-family: 'Times New Roman';
            }
            QLabel {
                color: #003366;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #007acc;
                border-radius: 10px;
                background-color: #ffffff;
                font-size: 14px;
            }
            QPushButton {
                border-radius: 10px;
                font-size: 14px;
            }
        """)

        layout = QVBoxLayout()

        # Heading
        heading = QLabel("🦠 Welcome to Cholera Survival Predictor")
        heading.setFont(QFont("Times New Roman", 20, QFont.Bold))
        heading.setAlignment(Qt.AlignCenter)
        heading.setStyleSheet("margin-top: 15px; margin-bottom: 10px;")
        layout.addWidget(heading)

        # Subheading
        subheading = QLabel("Estimate survivors from cholera using exponential model")
        subheading.setAlignment(Qt.AlignCenter)
        subheading.setStyleSheet("font-size: 13px; margin-bottom: 20px;")
        layout.addWidget(subheading)

        # Input section wrapper
        def create_row(label_text, widget):
            row = QHBoxLayout()
            label = QLabel(label_text)
            label.setFixedWidth(30)
            row.addWidget(label)
            row.addWidget(widget)
            return row

        # S₀ input
        self.s_input = QLineEdit()
        layout.addLayout(create_row("S₀ =", self.s_input))

        # T dropdown
        self.t_dropdown = QComboBox()
        self.t_dropdown.addItems([f"T{i}" for i in range(31)])
        layout.addLayout(create_row("T =", self.t_dropdown))

        # α input
        self.alpha_input = QLineEdit()
        layout.addLayout(create_row("α =", self.alpha_input))

        # e constant
        self.e_input = QLineEdit("2.718")
        self.e_input.setReadOnly(True)
        self.e_input.setStyleSheet("background-color: #dddddd;")
        layout.addLayout(create_row("e =", self.e_input))

        # Line divider
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: #007acc; margin-top: 15px; margin-bottom: 10px;")
        layout.addWidget(line)

        # Predict button
        self.predict_button = QPushButton(" Predict")
        self.predict_button.setStyleSheet("background-color: #007acc; color: white; padding: 8px;")
        self.predict_button.clicked.connect(self.predict)
        layout.addWidget(self.predict_button)

        # Result display
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 12px;
            padding: 15px;
            font-size: 15px;
            margin-top: 15px;
            border: 1px solid #ccc;
        """)
        layout.addWidget(self.result_label)

        # Clear button
        self.clear_button = QPushButton(" Clear")
        self.clear_button.setStyleSheet("background-color: #f44336; color: white; padding: 6px;")
        self.clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(self.clear_button)

        self.setLayout(layout)

    def predict(self):
        try:
            s = float(self.s_input.text())
            alpha = float(self.alpha_input.text())
            t = self.t_dropdown.currentIndex()
            year = 2021 + t

            exponent = alpha * t
            e_to_alpha_t = truncate_to_2_digits(math.exp(exponent))
            predicted = int(s * e_to_alpha_t)

            self.result_label.setText(
                f"<b>Predicted Value:</b> S = {predicted}<br>"
                f"<b>{predicted:,}</b> people will survive cholera in the year <b>{year}</b>."
            )
        except Exception as e:
            self.result_label.setText(f"<span style='color:red;'>Error: {str(e)}</span>")

    def clear_fields(self):
        self.s_input.clear()
        self.alpha_input.clear()
        self.t_dropdown.setCurrentIndex(0)
        self.result_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CholeraSurvivalPredictor()
    window.show()
    sys.exit(app.exec_())
