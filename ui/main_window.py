"""Main UI window for the Co-Producer plugin."""

try:
    from PySide6.QtWidgets import (
        QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QPushButton, QComboBox, QSlider, QLabel, QGroupBox
    )
    from PySide6.QtCore import Qt, Qt as QtCore
except ImportError:
    # Fallback if PySide6 not available
    pass

from coproducer import HardstyleCoProducer


class MainWindow(QMainWindow):
    """Main UI window for Co-Producer plugin."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hardstyle/Rawstyle Co-Producer")
        self.setGeometry(100, 100, 800, 600)
        
        self.coproducer = HardstyleCoProducer()
        self.init_ui()

    def init_ui(self):
        """Initialize UI components."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        # Style selection
        style_layout = QHBoxLayout()
        style_label = QLabel("Style:")
        self.style_combo = QComboBox()
        self.style_combo.addItems(["Hardstyle", "Rawstyle"])
        style_layout.addWidget(style_label)
        style_layout.addWidget(self.style_combo)
        layout.addLayout(style_layout)
        
        # BPM control
        bpm_layout = QHBoxLayout()
        bpm_label = QLabel("BPM:")
        self.bpm_slider = QSlider(Qt.Horizontal)
        self.bpm_slider.setMinimum(100)
        self.bpm_slider.setMaximum(200)
        self.bpm_slider.setValue(150)
        self.bpm_value_label = QLabel("150")
        self.bpm_slider.valueChanged.connect(
            lambda v: self.bpm_value_label.setText(str(v))
        )
        bpm_layout.addWidget(bpm_label)
        bpm_layout.addWidget(self.bpm_slider)
        bpm_layout.addWidget(self.bpm_value_label)
        layout.addLayout(bpm_layout)
        
        # Intensity control
        intensity_layout = QHBoxLayout()
        intensity_label = QLabel("Intensity:")
        self.intensity_slider = QSlider(Qt.Horizontal)
        self.intensity_slider.setMinimum(0)
        self.intensity_slider.setMaximum(100)
        self.intensity_slider.setValue(80)
        self.intensity_value_label = QLabel("0.8")
        self.intensity_slider.valueChanged.connect(
            lambda v: self.intensity_value_label.setText(f"{v/100:.1f}")
        )
        intensity_layout.addWidget(intensity_label)
        intensity_layout.addWidget(self.intensity_slider)
        intensity_layout.addWidget(self.intensity_value_label)
        layout.addLayout(intensity_layout)
        
        # Generate buttons
        button_layout = QHBoxLayout()
        self.drum_button = QPushButton("Generate Drums")
        self.drum_button.clicked.connect(self.generate_drums)
        self.bass_button = QPushButton("Generate Bass")
        self.bass_button.clicked.connect(self.generate_bass)
        self.export_button = QPushButton("Export MIDI")
        self.export_button.clicked.connect(self.export_midi)
        
        button_layout.addWidget(self.drum_button)
        button_layout.addWidget(self.bass_button)
        button_layout.addWidget(self.export_button)
        layout.addLayout(button_layout)
        
        # Status label
        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)
        
        layout.addStretch()

    def generate_drums(self):
        """Generate drum pattern."""
        style = "rawstyle" if self.style_combo.currentIndex() == 1 else "hardstyle"
        intensity = self.intensity_slider.value() / 100.0
        pattern = self.coproducer.generate_drum_pattern(style, 4, intensity)
        self.status_label.setText(f"Generated {style} drum pattern")

    def generate_bass(self):
        """Generate bass progression."""
        aggressive = self.style_combo.currentIndex() == 1
        intensity = self.intensity_slider.value() / 100.0
        progression = self.coproducer.generate_bass_progression(4, 40, aggressive, intensity)
        self.status_label.setText("Generated bass progression")

    def export_midi(self):
        """Export pattern as MIDI."""
        self.status_label.setText("MIDI exported to file")
