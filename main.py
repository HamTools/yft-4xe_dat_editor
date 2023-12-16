from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QFileDialog, QPushButton, QLabel
import sys
import data as rd

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle("Yaesu FT-4XE data editor")

        self.__yaesu_ft_4xe = rd.YaesuFt4Xe()

        pagelayout = QVBoxLayout()
        table_layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()

        pagelayout.addLayout(table_layout)
        pagelayout.addLayout(bottom_layout)

        self.setLayout(pagelayout)
        
        self.file_path_label = QLabel('')
        self.table_widget = QTableWidget()
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save)

        bottom_layout.addWidget(self.file_path_label)
        bottom_layout.addWidget(self.save_button)
        table_layout.addWidget(self.table_widget)
        self.table_widget.itemChanged.connect(self.log_change)
        self.changed_items = []

        file_path = self.open_file_name_dialog()
        self.__yaesu_ft_4xe.set_file_path(file_path)
        self.__yaesu_ft_4xe.read()
        self.load_data()
        self.changed_items = []
    
    def log_change(self, item):
        self.changed_items.append(item)
        print('Text:',item.text(), 'Col:',item.column(), 'Row:',item.row())
    
    def save(self):
        for item in self.changed_items:
            self.__yaesu_ft_4xe.write(item)
            
    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self,"Dat file", "","Data Files (*.dat)", options=options)
        if file_path:
            print(file_path)
            self.file_path_label.setText(file_path)
            return file_path
        else:
            sys.exit("File not selected") 

    def load_data(self):
        channels = self.__yaesu_ft_4xe.get_channels()
        self.table_widget.setRowCount(len(channels))
        self.table_widget.setColumnCount(4)
        print(channels)
        list_values = channels
        self.table_widget.setHorizontalHeaderLabels(['#No','Name', 'Frequency (Mhz)', 'Offset (Mhz)','Use'])
        
        row_index = 0
        for value_tuple in list_values:
            col_index = 0
            for value in value_tuple:
                self.table_widget.setItem(row_index , col_index, QTableWidgetItem(str(value)))
                col_index += 1
            row_index += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    app.exec_()