from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QFormLayout, QHBoxLayout, QLabel, QComboBox,
                               QLineEdit, QPushButton, QFrame, QSpinBox,
                               QColorDialog, QFileDialog, QToolBar, QStyle)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QAction, QPixmap
import sys
import pyperclip

default_color = "#B0E0E6"

class PersonalCard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Personal Info Card")
        self.setGeometry(100, 100, 420, 550)

        # -------- Central Widget --------
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # -------- Input Section --------
        self.input_layout = QFormLayout()
        self.create_form()
        self.main_layout.addLayout(self.input_layout)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        self.main_layout.addWidget(line)

        # -------- Display Section --------
        self.bg_widget = QWidget()
        self.output_layout = QVBoxLayout(self.bg_widget)
        self.create_display()
        self.main_layout.addWidget(self.bg_widget)

        # -------- Menu / Toolbar --------
        self.create_menu()
    from PySide6.QtWidgets import QStyle

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        generate = QAction(
            self.style().standardIcon(QStyle.SP_MediaPlay),
            "",
            self
        )
        generate.triggered.connect(self.update_display)

        save = QAction(
            self.style().standardIcon(QStyle.SP_DialogSaveButton),
            "",
            self
        )
        save.triggered.connect(self.save_card)

        clear = QAction(
            self.style().standardIcon(QStyle.SP_TrashIcon),
            "",
            self
        )
        clear.triggered.connect(self.clear_all)

        toolbar.addAction(generate)
        toolbar.addAction(save)
        toolbar.addAction(clear)

        self.statusBar().showMessage("Fill in your details and click generate")

    # ================= FORM =================
    def create_form(self):
        self.name = QLineEdit()
        self.name.setPlaceholderText("First name and Lastname")

        self.age = QSpinBox()
        self.age.setRange(1,120)
        self.age.setValue(25)
        self.age.setButtonSymbols(QSpinBox.UpDownArrows)

        self.email = QLineEdit()
        self.email.setPlaceholderText("username@domain.name")

        self.position = QComboBox()
        self.position.addItems(["Teaching Staff","Supporting Staff","Student","Visitor"])
        self.position.setCurrentIndex(-1)

        color_row = QWidget()
        color_layout = QHBoxLayout(color_row)

        self.fav_color = QColor(default_color)
        self.color_swatch = QLabel()
        self.color_swatch.setFixedSize(22,22)
        self.color_swatch.setStyleSheet(
            f"background-color:{self.fav_color.name()}; border:1px solid #888;"
        )

        color_button = QPushButton("Pick New Color")
        color_button.clicked.connect(self.pick_color)

        color_layout.addWidget(self.color_swatch)
        color_layout.addWidget(color_button)

        self.input_layout.addRow("Full name:", self.name)
        self.input_layout.addRow("Age:", self.age)
        self.input_layout.addRow("Email:", self.email)
        self.input_layout.addRow("Position:", self.position)
        self.input_layout.addRow("Your favorite color:", color_row)

    # ================= DISPLAY =================
    def create_display(self):
        self.bg_widget.setStyleSheet(
            f"background-color:{self.fav_color.name()}; border-radius:8px;"
        )

        self.name_label = QLabel("Your name here")
        self.name_label.setStyleSheet("font-size:18pt; font-weight:bold;")

        self.age_label = QLabel("(Age)")
        self.position_label = QLabel("Your position here")
        self.position_label.setStyleSheet("font-size:14pt;")

        self.email_layout = QHBoxLayout()
        self.email_icon = QLabel()
        self.email_icon.hide()

        self.email_label = QLabel("your_username@domain.name")

        self.email_layout.addWidget(self.email_icon)
        self.email_layout.addWidget(self.email_label)

        self.output_layout.addWidget(self.name_label)
        self.output_layout.addWidget(self.age_label)
        self.output_layout.addSpacing(10)
        self.output_layout.addWidget(self.position_label)
        self.output_layout.addLayout(self.email_layout)

    # ================= FUNCTIONS =================
    def pick_color(self):
        color = QColorDialog.getColor(self.fav_color, self)
        if color.isValid():
            self.fav_color = color
            self.color_swatch.setStyleSheet(
                f"background-color:{color.name()}; border:1px solid #888;"
            )
            self.bg_widget.setStyleSheet(
                f"background-color:{color.name()}; border-radius:8px;"
            )

    def update_display(self):
        self.name_label.setText(self.name.text())
        self.age_label.setText(f"({self.age.value()})")
        self.position_label.setText(self.position.currentText())
        self.email_label.setText(self.email.text())

        self.email_icon.setPixmap(
            self.style().standardIcon(
                self.style().SP_MessageBoxInformation
            ).pixmap(16,16)
        )
        self.email_icon.show()

        self.copy_card()
        self.statusBar().showMessage("Card copied to clipboard")

    def save_card(self):
        filename,_ = QFileDialog.getSaveFileName(
            self,"Save Card","my_card.txt","Text Files (*.txt)"
        )
        if filename:
            with open(filename,"w") as f:
                f.write(f"{self.name.text()}\n")
                f.write(f"({self.age.value()})\n")
                f.write(f"{self.position.currentText()}\n")
                f.write(f"Email: {self.email.text()}\n")
            self.statusBar().showMessage("Card saved")

    def copy_card(self):
        text = (f"{self.name.text()}\n"
                f"({self.age.value()})\n"
                f"{self.position.currentText()}\n"
                f"Email: {self.email.text()}")
        pyperclip.copy(text)

    def clear_form(self):
        self.name.clear()
        self.email.clear()
        self.age.setValue(25)
        self.position.setCurrentIndex(-1)
        self.statusBar().showMessage("Form cleared")

    def clear_display(self):
        self.name_label.setText("Your name here")
        self.age_label.setText("(Age)")
        self.position_label.setText("Your position here")
        self.email_label.setText("your_username@domain.name")
        self.email_icon.hide()
        self.bg_widget.setStyleSheet(
            f"background-color:{default_color}; border-radius:8px;"
        )
        self.statusBar().showMessage("Display cleared")

    def clear_all(self):
        self.clear_form()
        self.clear_display()

    # ================= MENU =================
    def create_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        edit_menu = menu.addMenu("Edit")

        generate = QAction("Generate Card", self)
        generate.triggered.connect(self.update_display)

        save = QAction("Save Card", self)
        save.triggered.connect(self.save_card)

        clear_display = QAction("Clear Display", self)
        clear_display.triggered.connect(self.clear_display)

        exit_app = QAction("Exit", self)
        exit_app.triggered.connect(self.close)

        file_menu.addActions([generate,save,clear_display])
        file_menu.addSeparator()
        file_menu.addAction(exit_app)

        copy = QAction("Copy Card", self)
        copy.triggered.connect(self.copy_card)

        clear_form = QAction("Clear Form", self)
        clear_form.triggered.connect(self.clear_form)

        edit_menu.addActions([copy,clear_form])

    # ================= TOOLBAR =================
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        generate = QAction(self.style().standardIcon(
            self.style().SP_ArrowForward),"",self)
        generate.triggered.connect(self.update_display)

        save = QAction(self.style().standardIcon(
            self.style().SP_DialogSaveButton),"",self)
        save.triggered.connect(self.save_card)

        clear = QAction(self.style().standardIcon(
            self.style().SP_TrashIcon),"",self)
        clear.triggered.connect(self.clear_all)

        toolbar.addActions([generate,save,clear])


def main():
    app = QApplication(sys.argv)

    import os
    base_path = os.path.dirname(os.path.abspath(__file__))
    style_path = os.path.join(base_path, "P1Style.qss")

    if os.path.exists(style_path):
        with open(style_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    else:
        print("Style file not found at:", style_path)

    window = PersonalCard()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()