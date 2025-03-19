from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class VideoPlayerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.video_label = QLabel("Video Player Area")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setStyleSheet("background-color: #ccc; border: 1px solid #999;")
        self.layout.addWidget(self.video_label)
    
    def play_clip(self, clip_name):
        """
        Display the clip in the video player area.
        Replace this with QMediaPlayer integration if needed.
        """
        self.video_label.setText(f"Playing: {clip_name}")
