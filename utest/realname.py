import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog


class FileRenamerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('重命名')
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.directory_label = QLabel('已选择的目录:')
        layout.addWidget(self.directory_label)

        self.directory_button = QPushButton('选择目录')
        self.directory_button.clicked.connect(self.select_directory)
        layout.addWidget(self.directory_button)

        self.file_name_label = QLabel('输入文件名')
        layout.addWidget(self.file_name_label)

        self.file_name_edit = QLineEdit()
        layout.addWidget(self.file_name_edit)

        self.target_name_label = QLabel('要修改为')
        layout.addWidget(self.target_name_label)

        self.target_name_edit = QLineEdit()
        layout.addWidget(self.target_name_edit)

        self.rename_button = QPushButton('确定')
        self.rename_button.clicked.connect(self.rename_files)
        layout.addWidget(self.rename_button)

        self.central_widget.setLayout(layout)

    def select_directory(self):
        dir_path = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if dir_path:
            self.selected_directory = dir_path
            self.directory_label.setText(f'Selected Directory: {self.selected_directory}')

    def rename_files(self):
        if hasattr(self, 'selected_directory'):
            file_name = self.file_name_edit.text()
            target_name = self.target_name_edit.text()

            for filename in os.listdir(self.selected_directory):
                if filename.startswith(file_name):
                    old_path = os.path.join(self.selected_directory, filename)
                    new_filename = filename.replace(file_name, target_name)
                    new_path = os.path.join(self.selected_directory, new_filename)
                    os.rename(old_path, new_path)

            self.file_name_edit.clear()
            self.target_name_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = FileRenamerApp()
    main_window.show()
    sys.exit(app.exec_())
