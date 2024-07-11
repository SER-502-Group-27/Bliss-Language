# Bliss Language

Bliss is a simple, expressive programming language designed to make programming approachable and fun. Built with flexibility and readability in mind, it integrates familiar syntax with powerful features, aiming to provide a seamless development experience.

## Features

- **Implicit Type Declaration**: Variables are implicitly typed, streamlining syntax.
- **Rich Set of Operators**: Supports arithmetic, logical operations, and more.
- **Control Structures**: Enables complex flow control with conditional statements and loops.
- **Built-in Print Functionality**: Simplifies output for various data types.
- **Error Handling**: Enhances debugging with straightforward error reporting.

## System Requirements

Bliss can be used on GNUstep, Linux, Unix, Windows, and Mac OS.

## Tools Used

- Python 3.6 or later
- PLY (Python Lex-Yacc) for building lexers and parsers.

## Getting Started

### Prerequisites

- Python 3.6 or later
- [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/ply.html)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SER-502-Group-27/Bliss-Language.git
   cd Bliss-Language


2. **Set up the environment**:
conda create -n bliss-env python=3.6
conda activate bliss-env
pip install ply

3. **Run a sample program**
python src/parser.py tests/sample.bs
Here, if tests/sample.bs does not work, try adding the complete path of the bliss file you want to run.

Youtube video link - https://youtu.be/Tg9lAqzFxOc
