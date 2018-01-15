from fman import DirectoryPaneCommand, show_alert
from fman.url import as_human_readable
from fman.clipboard import set_text
import os.path
import ntpath


class getFileName(DirectoryPaneCommand):
    def __call__(self):
        fileUnderCursor = self.pane.get_file_under_cursor()
        if fileUnderCursor is not None:
            filepath = as_human_readable(fileUnderCursor)
            set_text(ntpath.basename(filepath))
