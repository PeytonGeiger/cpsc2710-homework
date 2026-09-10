import sys
from PySide6.QtWidgets import *

class BudgetSummaryCard(QWidget):

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self._name = name
        self._value = "$0.00"
        layout = QVBoxLayout(self)

        self._name_label=QLabel(self._name)
        self._value_label=QLabel(self._value)

        layout.addWidget(self._name_label)
        layout.addWidget(self._value_label)

    def set_value(self, value):
        self._value = str(value)
        self._value_label.setText(self._value)

    def get_value(self):
        return self._value

def main():
    app = QApplication(sys.argv)  
    window = QWidget()
    window.setWindowTitle("Budget Summary Card Test")

    layout = QVBoxLayout(window)
    card = BudgetSummaryCard("Planned Total")
    layout.addWidget(card)

    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()