import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QRadioButton, QButtonGroup,
    QComboBox, QTextEdit,
    QDateEdit, QPushButton,
    QVBoxLayout, QHBoxLayout,
    QCheckBox
)
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QFont


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Registration Form")
        self.setFixedSize(400, 600)

        main_layout = QVBoxLayout()

        # -------------------------
        # Title
        # -------------------------
        title = QLabel("Student Registration Form")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # -------------------------
        # Full Name
        # -------------------------
        main_layout.addWidget(QLabel("Full Name:"))
        self.name_input = QLineEdit()
        main_layout.addWidget(self.name_input)

        # -------------------------
        # Email
        # -------------------------
        main_layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        main_layout.addWidget(self.email_input)

        # -------------------------
        # Phone
        # -------------------------
        main_layout.addWidget(QLabel("Phone:"))
        self.phone_input = QLineEdit()
        main_layout.addWidget(self.phone_input)

        # -------------------------
        # Date of Birth
        # -------------------------
        main_layout.addWidget(QLabel("Date of Birth:"))
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("M/dd/yy")
        self.date_edit.setDate(QDate(2000, 1, 1))
        main_layout.addWidget(self.date_edit)

        # -------------------------
        # Gender
        # -------------------------
        main_layout.addWidget(QLabel("Gender:"))

        gender_layout = QHBoxLayout()
        self.gender_group = QButtonGroup(self)

        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        self.nonbinary_radio = QRadioButton("Non-binary")
        self.prefer_radio = QRadioButton("Prefer not to say")

        for btn in [
            self.male_radio,
            self.female_radio,
            self.nonbinary_radio,
            self.prefer_radio
        ]:
            self.gender_group.addButton(btn)
            gender_layout.addWidget(btn)

        main_layout.addLayout(gender_layout)

        # -------------------------
        # Program
        # -------------------------
        main_layout.addWidget(QLabel("Program:"))
        self.program_combo = QComboBox()
        self.program_combo.addItems([
            "Engineering",
            "Computer Engineering",
            "Digital Media Engineering",
            "Environmental Engineering",
            "Electrical Engineering",
            "Mechanical Engineering"
        ])
        main_layout.addWidget(self.program_combo)

        # -------------------------
        # Additional Information
        # -------------------------
        main_layout.addWidget(QLabel("Tell us a little bit about yourself:"))
        self.info_text = QTextEdit()
        self.info_text.setMaximumHeight(100)
        main_layout.addWidget(self.info_text)

        # -------------------------
        # Terms and Conditions
        # -------------------------
        self.terms_checkbox = QCheckBox("I accept the terms and conditions.")
        main_layout.addWidget(self.terms_checkbox)

        # -------------------------
        # Submit Button
        # -------------------------
        self.submit_button = QPushButton("Submit Registration")
        main_layout.addWidget(self.submit_button)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
