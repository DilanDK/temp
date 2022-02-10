import sys
from PySide2 import QtWidgets, QtCore


class CheckBoxDemo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CheckBoxDemo, self).__init__(parent)
        self.groupBox = QtWidgets.QGroupBox("Checkboxes")
        self.groupBox.setFlat(False)
        self.childCheckboxes = []

        self.layout = QtWidgets.QVBoxLayout()
        self.groupBox.setLayout(self.layout)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.groupBox)

        self.setLayout(mainLayout)
        self.setWindowTitle("checkbox demo")
        self.masterCheckbox = QtWidgets.QCheckBox("Master")
        self.layout.addWidget(self.masterCheckbox)

        self.add_checkbox()

        self.masterCheckbox.stateChanged.connect(self.toggle_all_checkbox)

    def add_checkbox(self):
        for i in range(0, 3):
            checkbox = QtWidgets.QCheckBox("P{}".format(i+1))
            checkbox.data = "Some data here"
            self.childCheckboxes.append(checkbox)
            self.layout.addWidget(checkbox)

    def toggle_all_checkbox(self):
        for checkbox in self.childCheckboxes:
            if self.masterCheckbox.isChecked():
                checkbox.setCheckState(QtCore.Qt.Checked)
            else:
                checkbox.setCheckState(QtCore.Qt.Unchecked)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    checkboxDemo = CheckBoxDemo()
    checkboxDemo.show()
    sys.exit(app.exec_())
