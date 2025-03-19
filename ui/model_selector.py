from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton

class ModelSelectorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.label = QLabel("Select Model:")
        self.layout.addWidget(self.label)
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Model A", "Model B", "LLM Model"])
        self.layout.addWidget(self.combo_box)
        
        self.prompt_label = QLabel("Enter Prompt:")
        self.layout.addWidget(self.prompt_label)
        
        self.prompt_input = QTextEdit()
        self.prompt_input.setFixedHeight(100)
        self.layout.addWidget(self.prompt_input)
        
        self.run_button = QPushButton("Run Inference")
        self.layout.addWidget(self.run_button)
