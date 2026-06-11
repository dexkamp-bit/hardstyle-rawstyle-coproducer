from setuptools import setup, find_packages

setup(
    name="hardstyle-rawstyle-coproducer",
    version="0.1.0",
    description="Professional FL Studio Plugin for Hardstyle & Rawstyle Production",
    author="dexkamp-bit",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.11.0",
        "music21>=9.1.0",
        "midi>=0.2.3",
        "libarosa>=0.10.0",
        "PySide6>=6.5.0",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
