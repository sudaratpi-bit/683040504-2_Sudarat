import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtGui import QFont

# ─────────────────────────────────────────────
# Room Card
# ─────────────────────────────────────────────
class RoomCard(QWidget):

    room_selected = Signal(str, int)

    def __init__(self, room_name, price, description, emoji="🏨"):
        super().__init__()
        self.room_name = room_name
        self.price = price
        self._build_ui(emoji, description)
        self.deselect()

    def _build_ui(self, emoji, description):
        self.setFixedSize(200, 220)

        layout = QVBoxLayout(self)
        layout.setSpacing(6)

        emoji_lbl = QLabel(emoji)
        emoji_lbl.setAlignment(Qt.AlignCenter)
        emoji_lbl.setFont(QFont("Segoe UI Emoji", 28))

        name_lbl = QLabel(self.room_name)
        name_lbl.setAlignment(Qt.AlignCenter)
        name_lbl.setFont(QFont("Segoe UI", 11, QFont.Bold))

        price_lbl = QLabel(f"${self.price} / night")
        price_lbl.setAlignment(Qt.AlignCenter)

        desc_lbl = QLabel(description)
        desc_lbl.setAlignment(Qt.AlignCenter)
        desc_lbl.setWordWrap(True)
        desc_lbl.setStyleSheet("color: gray; font-size: 11px;")

        self.select_btn = QPushButton("Select Room")
        self.select_btn.setFixedHeight(30)
        self.select_btn.clicked.connect(self._on_select_clicked)

        layout.addWidget(emoji_lbl)
        layout.addWidget(name_lbl)
        layout.addWidget(price_lbl)
        layout.addWidget(desc_lbl)
        layout.addStretch()
        layout.addWidget(self.select_btn)

    def _on_select_clicked(self):
        self.room_selected.emit(self.room_name, self.price)

    def select(self):
        self.setStyleSheet("border:2px solid #22c55e; border-radius:12px; background:white;")
        self.select_btn.setText("✓ Selected")
        self.select_btn.setStyleSheet("background:#22c55e; color:white; border-radius:8px;")

    def deselect(self):
        self.setStyleSheet("border:1px solid #e5e7eb; border-radius:12px; background:white;")
        self.select_btn.setText("Select Room")
        self.select_btn.setStyleSheet("""
            QPushButton {
                color:white;
                border-radius:8px;
                padding:6px;
                background:qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #6366f1,
                    stop:1 #8b5cf6
                );
            }
        """)

# ─────────────────────────────────────────────
# Booking Page
# ─────────────────────────────────────────────
class BookingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.cards = []
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 25, 50, 25)
        layout.setSpacing(18)

        # TITLE
        title_layout = QHBoxLayout()
        icon = QLabel("🏨")
        icon.setFont(QFont("Segoe UI Emoji", 18))

        title = QLabel("Book Your Stay at CozyStay")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))

        title_layout.addWidget(icon)
        title_layout.addWidget(title)
        title_layout.addStretch()

        subtitle = QLabel("Fill in your details and choose your room")
        subtitle.setStyleSheet("color: gray;")

        layout.addLayout(title_layout)
        layout.addWidget(subtitle)

        # SECTION
        section1 = QLabel("📄 Guest Information")
        section1.setFont(QFont("Segoe UI", 11, QFont.Bold))
        layout.addWidget(section1)

        # INPUT
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.checkin_input = QDateEdit()
        self.checkout_input = QDateEdit()
        self.guests_input = QSpinBox()

        self.checkin_input.setDate(QDate.currentDate())
        self.checkout_input.setDate(QDate.currentDate().addDays(1))
        self.checkin_input.setDisplayFormat("dd/MM/yyyy")
        self.checkout_input.setDisplayFormat("dd/MM/yyyy")

        self.guests_input.setRange(1, 10)
        self.guests_input.setSuffix(" guest(s)")

        for w in [self.name_input, self.phone_input,
                  self.checkin_input, self.checkout_input,
                  self.guests_input]:
            w.setFixedHeight(34)

        form = QFormLayout()
        form.setSpacing(12)

        form.addRow("Full Name :", self.name_input)
        form.addRow("Phone Number :", self.phone_input)
        form.addRow("Check-in Date :", self.checkin_input)
        form.addRow("Check-out Date :", self.checkout_input)
        form.addRow("Guests :", self.guests_input)

        # label bold
        for i in range(form.rowCount()):
            label = form.itemAt(i, QFormLayout.LabelRole).widget()
            label.setFont(QFont("Segoe UI", 10, QFont.Bold))

        form_box = QFrame()
        form_box.setLayout(form)
        form_box.setMaximumWidth(650)

        # ✅ FIX สี label หาย
        form_box.setStyleSheet("""
            QFrame {
                background:#f9fafb;
                border:1px solid #e5e7eb;
                border-radius:12px;
                padding:15px;
            }

            QLabel {
                color: black;
            }

            QLineEdit, QDateEdit, QSpinBox {
                background: white;
                color: black;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                padding: 4px;
            }
        """)

        layout.addWidget(form_box, alignment=Qt.AlignCenter)

        # ROOMS
        section2 = QLabel("🛏 Select a Room")
        section2.setFont(QFont("Segoe UI", 11, QFont.Bold))
        layout.addWidget(section2)

        rooms_layout = QHBoxLayout()
        rooms_layout.setSpacing(20)

        rooms = [
            ("Standard Room", 50, "Single bed", "🛏"),
            ("Deluxe Room", 120, "Ocean view with balcony", "🌊"),
            ("Suite Room", 250, "Luxury suite with living room", "👑"),
            ("Family Room", 160, "2 Bedrooms for family", "👨‍👩‍👧‍👦"),
        ]

        for r in rooms:
            card = RoomCard(*r)
            card.room_selected.connect(self._on_room_selected)
            self.cards.append(card)
            rooms_layout.addWidget(card)

        layout.addLayout(rooms_layout)
        layout.setAlignment(rooms_layout, Qt.AlignCenter)

        # BUTTON
        btn_layout = QHBoxLayout()
        self.clear_btn = QPushButton("Clear Info")
        self.next_btn = QPushButton("Next →")

        self.next_btn.setStyleSheet("""
            QPushButton {
                color:white;
                padding:8px 18px;
                border-radius:8px;
                background:qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #6366f1,
                    stop:1 #8b5cf6
                );
            }
        """)

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.next_btn)

        layout.addLayout(btn_layout)

    def _on_room_selected(self, name, price):
        for c in self.cards:
            if c.room_name == name:
                c.select()
            else:
                c.deselect()

# ─────────────────────────────────────────────
# Main Window
# ─────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CozyStay")
        self.setFixedSize(1000, 720)

        screen = QApplication.primaryScreen().availableGeometry()
        self.move((screen.width()-1000)//2, (screen.height()-720)//2)

        self.setCentralWidget(BookingPage())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()