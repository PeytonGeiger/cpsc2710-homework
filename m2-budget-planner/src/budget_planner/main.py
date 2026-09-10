import sys
from PySide6.QtWidgets import *
from budget_planner.budget_category_panel import BudgetCategoryPanel
from budget_planner.summary_card import BudgetSummaryCard

class BudgetPlannerWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Monthly Budget Planner")
        main_layout = QVBoxLayout(self)
        grid_layout = QGridLayout()

        categories = ["Housing", "Food", "Transportation", "Savings"]
        self.panels = [BudgetCategoryPanel(cat) for cat in categories]

        for i, panel in enumerate(self.panels):
            grid_layout.addWidget(panel, i // 2, i % 2)

        main_layout.addLayout(grid_layout)

        self.update_btn = QPushButton("Update summary")
        self.update_btn.clicked.connect(self.update_summary)
        main_layout.addWidget(self.update_btn)

        summary_layout = QHBoxLayout()
        self.cards = {
            "planned": BudgetSummaryCard("Total Planned"),
            "actual": BudgetSummaryCard("Total Actual"),
            "remaining": BudgetSummaryCard("Remaining"),
        }
        for card in self.cards.values():
            summary_layout.addWidget(card)

        main_layout.addLayout(summary_layout)
        self.update_summary()

    def update_summary(self):
        try:
            planned_total, actual_total = 0.0, 0.0
            for p in self.panels:
                p_val = float(p.get_planned_amount() or 0)
                a_val = float(p.get_actual_amount() or 0)

                planned_total += p_val
                if p.is_actual_enabled(): 
                    actual_total += min(a_val, p_val)

            self.cards["planned"].set_value(f"${planned_total:,.2f}")
            self.cards["actual"].set_value(f"${actual_total:,.2f}")
            self.cards["remaining"].set_value(f"${planned_total - actual_total:,.2f}")

        except ValueError:
            pass
def main():
    app =QApplication(sys.argv)
    window = BudgetPlannerWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()