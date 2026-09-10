import sys
from PySide6.QtWidgets import *


class BudgetCategoryPanel(QWidget):

    def __init__(self, category_name: str = "Housing", parent=None):
        super().__init__(parent)
        main_layout = QVBoxLayout(self)
        self.category_label = QLabel(category_name)
        main_layout.addWidget(self.category_label)
        form_layout = QFormLayout()
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Essential", "Optional"])
        form_layout.addRow("Budget type", self.type_combo)
        self.planned_edit = QLineEdit()
        form_layout.addRow("Planned amount", self.planned_edit)
        self.record_actual_checkbox = QCheckBox("Record actual spending")
        form_layout.addRow(self.record_actual_checkbox)
        self.actual_edit = QLineEdit()
        self.actual_edit.setEnabled(False) 
        form_layout.addRow("Actual amount", self.actual_edit)
        main_layout.addLayout(form_layout)
        self.record_actual_checkbox.toggled.connect(self.actual_edit.setEnabled)

    def set_category_name(self, name):
        self.category_label.setText(name)

    def get_category_name(self):
        return self.category_label.text()

    def get_budget_type(self):
        return self.type_combo.currentText()

    def get_planned_amount(self):
        return self.planned_edit.text()

    def is_actual_enabled(self):
        return self.record_actual_checkbox.isChecked()

    def get_actual_amount(self):
        return self.actual_edit.text()

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Budget Category Panel Test")

    layout = QVBoxLayout(window)
    panel = BudgetCategoryPanel("Housing")
    layout.addWidget(panel)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()