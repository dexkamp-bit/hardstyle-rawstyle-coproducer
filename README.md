# Hardstyle/Rawstyle Co-Producer Plugin

🎵 **Professional FL Studio Plugin for Hardstyle & Rawstyle Production**

## Features

✅ **Hardstyle Kick/Drum Generation** - Generate authentic hardstyle kicks, snares, and hi-hats
✅ **Rawstyle Bass Synthesis** - Create aggressive rawstyle basslines
✅ **Sample Library Integration** - Browse and load professional hardstyle/rawstyle samples
✅ **Real-time MIDI Export** - Export directly to FL Studio Piano Roll
✅ **AI-Powered Co-Production** - Intelligent pattern generation

## Installation

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Build CLAP/VST wrapper: `python setup.py build`
4. Copy plugin to FL Studio plugin folder

## Quick Start

```python
from coproducer import HardstyleCoProducer

producer = HardstyleCoProducer()
kick_midi = producer.generate_hardstyle_kick(bpm=150, intensity=0.8)
bass_midi = producer.generate_rawstyle_bass(bpm=150, intensity=0.9)
```

## Architecture

- `core/` - Core synthesis & generation engines
- `generators/` - Drum, bass, and pattern generators
- `samples/` - Sample library manager
- `vst/` - VST/CLAP wrapper for FL Studio
- `ui/` - User interface components

## License

MIT License
