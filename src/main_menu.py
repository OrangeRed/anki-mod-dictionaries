from typing import Optional

from aqt import mw, utils
from aqt.qt import QAction, QDialog, QHBoxLayout, QVBoxLayout, QPushButton, Qt, QWidget


class AddonSettings(QDialog):
    def test_func(self) -> None:
        # get the number of cards in the current collection, which is stored in the main window
        card_count = mw.col.cardCount()
        # show a message box
        utils.showInfo("Card count: %d" % card_count)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        """Init all interactive elements"""
        self.setWindowTitle("Modular Dictionary Settings")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        """
        TODO Create import dictionary logic
        """
        test_btn = QPushButton("Card Count", self)
        test_btn.clicked.connect(self.test_func)

        """Create Layouts"""
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(test_btn)

        # Init dictionary import widget
        main_layout = QVBoxLayout(self)
        """
        TODO Make dictionary import widget
        # main_layout.addWidget(DictionaryWidget)
        """
        main_layout.addLayout(btn_layout)


def insert_menu_item() -> None:
    def show_ui() -> None:
        mw.addon_settings = AddonSettings(mw)
        mw.addon_settings.show()

    tools_menu = mw.form.menuTools
    open_dict_config = QAction("&Dictionary Settings...", tools_menu)
    open_dict_config.triggered.connect(show_ui)
    tools_menu.addAction(open_dict_config)
