"""
Sudarat Pitakwongroj
683040504-2
P1
"""


import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QComboBox,
    QSizePolicy, QSpacerItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

kg = "kilograms"
cm = "centimeters"
adult = "Adults 20+"
child = "Children and Teenagers (5-19)"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P1: BMI Calculator")
        self.setFixedSize(360, 520)

        central = QWidget()
        main_layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        #Header 
        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            background-color: #B22222;
            color: white;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
        """)
        main_layout.addWidget(title)

        #Sections
        input_section = InputSection()
        output_section = OutputSection()

        result_container = QWidget()
        result_container.setStyleSheet("background-color: #FAF0E6;")
        result_container.setLayout(output_section)

        main_layout.addLayout(input_section)
        main_layout.addWidget(result_container)

        #Signals 
        input_section.submit_btn.clicked.connect(
            lambda: input_section.submit_reg(output_section)
        )
        input_section.clear_btn.clicked.connect(
            lambda: input_section.clear_form(output_section)
        )


class InputSection(QVBoxLayout):
    def __init__(self):
        super().__init__()

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignTop)
        form.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)

        # BMI age group
        self.age_group = QComboBox()
        self.age_group.addItems([adult, child])
        form.addRow("BMI age group:", self.age_group)

        # Weight
        w_layout = QHBoxLayout()
        self.weight = QLineEdit()
        self.weight.setFixedWidth(110)

        self.weight_unit = QComboBox()
        self.weight_unit.addItem(kg)
        self.weight_unit.setFixedWidth(110)

        w_layout.addWidget(self.weight)
        w_layout.addWidget(self.weight_unit)
        form.addRow("Weight:", w_layout)

        # Height
        h_layout = QHBoxLayout()
        self.height = QLineEdit()
        self.height.setFixedWidth(110)

        self.height_unit = QComboBox()
        self.height_unit.addItem(cm)
        self.height_unit.setFixedWidth(110)

        h_layout.addWidget(self.height)
        h_layout.addWidget(self.height_unit)
        form.addRow("Height:", h_layout)

        self.addLayout(form)

        # Buttons
        btn_layout = QHBoxLayout()
        self.clear_btn = QPushButton("clear")
        self.submit_btn = QPushButton("Submit Registration")
        btn_layout.addWidget(self.clear_btn)
        btn_layout.addWidget(self.submit_btn)
        self.addLayout(btn_layout)

    def clear_form(self, output_section):
        self.weight.clear()
        self.height.clear()
        output_section.clear_result()

    def submit_reg(self, output_section):
        bmi = self.calculate_BMI()
        if bmi is not None:
            output_section.update_results(
                bmi, self.age_group.currentText()
            )

    def calculate_BMI(self):
        try:
            w = float(self.weight.text())
            h = float(self.height.text()) / 100
            return w / (h ** 2)
        except:
            return None


class OutputSection(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.title = QLabel("Your BMI")
        self.title.setFont(QFont("Arial", 12, QFont.Bold))
        self.title.setStyleSheet("color: black;")
        self.addWidget(self.title, alignment=Qt.AlignCenter)

        self.result_label = QLabel("0.00")
        self.result_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.result_label.setStyleSheet("color: blue;")
        self.addWidget(self.result_label, alignment=Qt.AlignCenter)

        self.extra_layout = None

        self.spacer = QSpacerItem(
            20, 40,
            QSizePolicy.Minimum,
            QSizePolicy.Expanding
        )
        self.addItem(self.spacer)

    def update_results(self, bmi, age_group):
        self.clear_result()
        self.result_label.setText(f"{bmi:.2f}")

        if age_group == adult:
            self.show_adult_table()
        else:
            self.show_child_link()

    def show_adult_table(self):
        self.extra_layout = QGridLayout()

        headers = ["BMI", "Condition"]
        for i, h in enumerate(headers):
            label = QLabel(h)
            label.setFont(QFont("Arial", 10, QFont.Bold))
            label.setStyleSheet("color: black;")
            self.extra_layout.addWidget(label, 0, i, Qt.AlignCenter)

        data = [
            ("< 18.5", "Thin"),
            ("18.5 - 25.0", "Normal"),
            ("25.1 - 30.0", "Overweight"),
            ("> 30.0", "Obese")
        ]

        for r, (bmi, cond) in enumerate(data, start=1):
            bmi_label = QLabel(bmi)
            bmi_label.setStyleSheet("color: black;")

            cond_label = QLabel(cond)
            cond_label.setStyleSheet("color: black;")

            self.extra_layout.addWidget(bmi_label, r, 0, Qt.AlignCenter)
            self.extra_layout.addWidget(cond_label, r, 1)

        self.insertLayout(2, self.extra_layout)

    def show_child_link(self):
        self.extra_layout = QHBoxLayout()

        boy = QLabel(
            '<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-boys-z-5-19years.pdf">BMI graph for BOYS</a>'
        )
        girl = QLabel(
            '<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-girls-z-5-19years.pdf">BMI graph for GIRLS</a>'
        )
        boy.setOpenExternalLinks(True)
        girl.setOpenExternalLinks(True)

        boy.setStyleSheet("color: black;")
        girl.setStyleSheet("color: black;")

        self.extra_layout.addWidget(boy)
        self.extra_layout.addWidget(girl)

        self.insertLayout(2, self.extra_layout)

    def clear_result(self):
        if self.extra_layout:
            while self.extra_layout.count():
                item = self.extra_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.removeItem(self.extra_layout)
            self.extra_layout = None

        self.result_label.setText("0.00")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
