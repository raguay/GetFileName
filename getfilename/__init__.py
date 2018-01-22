from fman import DirectoryPaneCommand, show_alert
from fman.url import as_human_readable
from fman.clipboard import set_text
import os.path
import ntpath


class getFileName(DirectoryPaneCommand):
    def __call__(self):
        filesSelection = self.pane.get_selected_files()
        if not filesSelection:
            fileUnderCursor = self.pane.get_file_under_cursor()
            if fileUnderCursor is not None:
                filepath = as_human_readable(fileUnderCursor)
                set_text(ntpath.basename(filepath))
        else:
            fileList = ""
            first = True
            for files in filesSelection:
                if first:
                    fileList += ntpath.basename(as_human_readable(files))
                    first = False
                else:
                    fileList += ", " + ntpath.basename(as_human_readable(files))
            set_text(fileList)
