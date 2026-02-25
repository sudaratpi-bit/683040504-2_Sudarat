"""
Sudarat Pitakwongroj
683040504-2
P1
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QComboBox, QSpinBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QMessageBox
)
from PySide6.QtCore import Qt


class StudentGradeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grade Calculator")
        self.resize(900, 500)

        self.students = {}   # {id: name}
        self.load_students()

        self.init_ui()
        self.apply_style()

    # ---------- Load students from file ----------
    def load_students(self):
        try:
            with open("students.txt", "r", encoding="utf-8") as file:
                for line in file:
                    sid, name = line.strip().split(",")
                    self.students[sid] = name
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "students.txt not found")
            sys.exit()

    # ---------- UI ----------
    def init_ui(self):
        # Student ID
        self.id_combo = QComboBox()
        self.id_combo.addItem("Select Student ID")
        self.id_combo.addItems(self.students.keys())
        self.id_combo.currentTextChanged.connect(self.show_name)

        # Student name
        self.name_label = QLabel("")
        self.name_label.setFixedHeight(30)

        # Scores
        self.math_spin = QSpinBox()
        self.science_spin = QSpinBox()
        self.english_spin = QSpinBox()

        for spin in (self.math_spin, self.science_spin, self.english_spin):
            spin.setRange(0, 100)

        # Buttons
        self.add_btn = QPushButton("Add Student")
        self.reset_btn = QPushButton("Reset Input")
        self.clear_btn = QPushButton("Clear All")

        self.add_btn.clicked.connect(self.add_student)
        self.reset_btn.clicked.connect(self.reset_input)
        self.clear_btn.clicked.connect(self.clear_table)

        # Table
        self.table = QTableWidget(0, 8)
        self.table.setHorizontalHeaderLabels([
            "Student ID", "Name", "Math", "Science",
            "English", "Total", "Average", "Grade"
        ])

        # ----- Layout -----
        main_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Student ID:"))
        row1.addWidget(self.id_combo)
        row1.addWidget(QLabel("Student Name:"))
        row1.addWidget(self.name_label)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Math"))
        row2.addWidget(self.math_spin)
        row2.addWidget(QLabel("Science"))
        row2.addWidget(self.science_spin)
        row2.addWidget(QLabel("English"))
        row2.addWidget(self.english_spin)

        row3 = QHBoxLayout()
        row3.addWidget(self.add_btn)
        row3.addWidget(self.reset_btn)
        row3.addWidget(self.clear_btn)

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    # ---------- Styling (QSS) ----------
    def apply_style(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #5DADE2;
                color: white;
                padding: 8px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3498DB;
            }
            QTableWidget {
                gridline-color: #ccc;
            }
            QHeaderView::section {
                background-color: #AED6F1;
                padding: 6px;
                font-weight: bold;
            }
        """)

    # ---------- Functions ----------
    def show_name(self, sid):
        self.name_label.setText(self.students.get(sid, ""))

    def calculate_grade(self, avg):
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def add_student(self):
        sid = self.id_combo.currentText()
        if sid == "Select Student ID":
            QMessageBox.warning(self, "Warning", "Please select Student ID")
            return

        name = self.students[sid]
        math = self.math_spin.value()
        science = self.science_spin.value()
        english = self.english_spin.value()

        total = math + science + english
        avg = total / 3
        grade = self.calculate_grade(avg)

        row = self.table.rowCount()
        self.table.insertRow(row)

        data = [sid, name, math, science, english, total, f"{avg:.2f}", grade]

        for col, value in enumerate(data):
            item = QTableWidgetItem(str(value))
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, col, item)

        self.table.sortItems(0)

    def reset_input(self):
        self.id_combo.setCurrentIndex(0)
        self.math_spin.setValue(0)
        self.science_spin.setValue(0)
        self.english_spin.setValue(0)
        self.name_label.clear()

    def clear_table(self):
        self.table.setRowCount(0)


# ---------- Run App ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentGradeApp()
    window.show()
    sys.exit(app.exec())
