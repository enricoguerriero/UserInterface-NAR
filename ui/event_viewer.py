from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

class EventViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Events:")
        self.layout.addWidget(self.label)
        self.event_list = QListWidget()
        # Initial hardcoded events
        events = ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5", "Event 6", "Event 7"]
        self.event_list.addItems(events)
        self.layout.addWidget(self.event_list)
    
    def update_events(self, events):
        """
        Update the event list with new events or predictions.
        """
        self.event_list.clear()
        self.event_list.addItems(events)
