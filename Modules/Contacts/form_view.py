

from PyQt5.QtGui import QIcon
from Widgets.PushButton import MYPushButton
from icons import ICON
from Modules.Contacts.BaseClases.base_ui_attribs import BaseUIAttribs





class FormView(BaseUIAttribs):

    def __init__(self, parent=None):
        super(FormView, self).__init__(parent=parent, type='nonedit')
        self.btn_edit = MYPushButton(parent=self)
        self.btn_remove = MYPushButton(parent=self)

        self.btn_edit.setIcon(QIcon(ICON.DEFAULT.edit()))
        self.btn_remove.setIcon(QIcon(ICON.DEFAULT.remove()))

        self.btns_layout.addWidget(self.btn_edit)
        self.btns_layout.addWidget(self.btn_remove)




if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormView()
    win.show()
    app.exec_()

