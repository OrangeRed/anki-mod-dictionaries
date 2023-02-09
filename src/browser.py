import os
from typing import Optional, Sequence
from .util import get_path

from aqt import mw, utils
from anki.errors import InvalidInput
from anki.models import NotetypeId
from anki.notes import NoteId
from aqt.browser import Browser

from aqt.qt import (
    QAction,
    QComboBox,
    QCheckBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    Qt,
    QWidget,
    QPushButton,
)


class DictionaryLookup(QDialog):
    def test_func(self) -> None:
        # get the number of cards in the current collection, which is stored in the main window
        card_count = mw.col.cardCount()
        # show a message box
        utils.showInfo("Card count: %d" % card_count)

    def __init__(
        self,
        brws: Browser,
        note_type_id: NotetypeId,
        notes: Sequence[NoteId],
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)

        """Init all interactive elements"""
        self.setWindowTitle("Dictionary Lookup")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        user_files = get_path("user_files")
        if not os.path.exists(user_files):
            utils.showWarning("user_files folder doesn't exist, can't access dictionaries")
            self.reject()

        self.dictionaries = QComboBox(self)
        self.dictionaries.addItems(os.listdir(user_files))
        self.dictionaries.setToolTip("The dictionary from which to look up words.")

        # sort fields by position, just to be safe
        fields = [field["name"] for field in sorted(brws.col.models.get(note_type_id)["flds"], key=lambda f: f["ord"])]
        self.search_fields = QComboBox(self)
        self.search_fields.addItems(fields)
        self.search_fields.setToolTip("The field that will be used to query the dictionary.")
        self.target_fields = QComboBox(self)
        self.target_fields.addItems(fields)
        self.target_fields.setToolTip("The field that will contain the queried defintion.")

        self.no_def_tag = QCheckBox("Tag notes whose query was not found.", self)
        self.no_def_tag.setChecked(True)
        self.no_def_tag.setToolTip(
            "If this option is enabled notes will be tagged if the search came up with no results."
        )

        """
        TODO Create Dictionary Look up logic
        """
        test_btn = QPushButton("Card Count", self)
        test_btn.clicked.connect(self.test_func)

        """Create Layouts"""
        form_layout = QFormLayout()
        form_layout.addRow("Dictionary:", self.dictionaries)
        form_layout.addRow("Search Field:", self.search_fields)
        form_layout.addRow("Target Field:", self.target_fields)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(test_btn)

        layout = QVBoxLayout(self)
        layout.addLayout(form_layout)
        layout.addWidget(self.no_def_tag)
        layout.addLayout(btn_layout)


def insert_menu_item(brws: Browser) -> None:
    def show_ui() -> None:
        note_ids = brws.selected_notes()
        try:
            note_type_id = brws.col.models.get_single_notetype_of_notes(note_ids)
        except InvalidInput:
            utils.showWarning("Please make sure the selected notes are the same note type.")

        brws.dict_lookup = DictionaryLookup(brws, note_type_id, note_ids, brws)
        brws.dict_lookup.show()

    notes_menu = brws.form.menu_Notes
    dict_lookup = QAction("&Modular Dictionary Add Definitions...", notes_menu)
    dict_lookup.triggered.connect(show_ui)
    notes_menu.addAction(dict_lookup)
