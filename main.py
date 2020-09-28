import sys
from PyQt5.QtWidgets import QApplication
from model import evaluateExpression
from controller import Controller

from view import GUI


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    model = evaluateExpression
    Controller(model=model, view=view)
    # Show the calculator's GUI
    view = GUI()
    view.show()
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
