

from Modules.Emloyees.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog






class FormAdd(MYDialog):

    def __init__(self, DB, parent=None):
        super(FormAdd, self).__init__(
            title='Добавление сотрудника',
            parent=parent
        )
        self.attribs = BaseUIAttribs(DB=DB, role=BaseUIAttribs.Editable, parent=self)
        self.main_layout.addWidget(self.attribs)
        self.resize(700, 400)








if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormAdd()
    win.show()
    app.exec_()

