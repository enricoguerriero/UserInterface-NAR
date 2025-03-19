from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QFileDialog

class ClipSelectorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.label = QLabel("Select Video and Clip:")
        self.layout.addWidget(self.label)
        
        self.video_list = QListWidget()
        self.video_list.setFixedHeight(100)
        self.layout.addWidget(self.video_list)
        
        self.clip_list = QListWidget()
        self.clip_list.setFixedHeight(100)
        self.layout.addWidget(self.clip_list)
        
        self.load_button = QPushButton("Scan Directory for Videos")
        self.layout.addWidget(self.load_button)
        
        self.load_button.clicked.connect(self.load_videos)
    
    def load_videos(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Video Directory")
        if directory:
            # For now, simulate loading videos.
            self.video_list.clear()
            # You can later integrate backend.video_processing.scan_directory_for_videos
            self.video_list.addItem("Dummy Video 1.mp4")
            self.video_list.addItem("Dummy Video 2.mp4")
    
    def update_clips(self, video_name):
        """
        Update the clip list based on the selected video.
        """
        self.clip_list.clear()
        # For now, simulate clips; later, load based on video_name.
        self.clip_list.addItem("Clip A")
        self.clip_list.addItem("Clip B")
