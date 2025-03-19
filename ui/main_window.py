from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QSplitter
from PyQt5.QtCore import Qt
from ui.clip_selector import ClipSelectorWidget
from ui.video_player import VideoPlayerWidget
from ui.event_viewer import EventViewerWidget
from ui.model_selector import ModelSelectorWidget

# Import the backend function
from backend.model_inference import run_model_inference

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Event Viewer")
        self.resize(1000, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        splitter = QSplitter(Qt.Horizontal)
        
        # Left panel: Clip selector and video player
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        self.clip_selector_widget = ClipSelectorWidget()
        left_layout.addWidget(self.clip_selector_widget)
        
        self.video_player_widget = VideoPlayerWidget()
        left_layout.addWidget(self.video_player_widget, stretch=1)
        
        # Right panel: Model selector and event viewer
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        self.model_selector_widget = ModelSelectorWidget()
        right_layout.addWidget(self.model_selector_widget)
        
        self.event_viewer_widget = EventViewerWidget()
        right_layout.addWidget(self.event_viewer_widget)
        
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        main_layout.addWidget(splitter)
        
        # Connect signals:
        self.clip_selector_widget.video_list.itemClicked.connect(self.video_selected)
        self.clip_selector_widget.clip_list.itemClicked.connect(self.clip_selected)
        self.model_selector_widget.run_button.clicked.connect(self.run_inference)
    
    def video_selected(self, item):
        video_name = item.text()
        self.clip_selector_widget.update_clips(video_name)
    
    def clip_selected(self, item):
        clip_name = item.text()
        self.video_player_widget.play_clip(clip_name)
    
    def run_inference(self):
        model = self.model_selector_widget.combo_box.currentText()
        prompt = self.model_selector_widget.prompt_input.toPlainText()
        # Here, you’d normally retrieve structured clip data. For now, we use a placeholder.
        current_clip = self.video_player_widget.video_label.text()
        predictions = run_model_inference(current_clip, prompt, model)
        self.event_viewer_widget.update_events(predictions)
