# Bliss Language

Bliss is a simple, expressive programming language designed to make programming approachable and fun. Built with flexibility and readability in mind, it integrates familiar syntax with powerful features, aiming to provide a seamless development experience.

## Features

- **Implicit Type Declaration**: Variables in Bliss are implicitly typed, making the syntax cleaner and more intuitive.
- **Rich Set of Operators**: Includes a comprehensive set of operators for arithmetic, logical operations, and more.
- **Control Structures**: Supports conditional statements and loops for complex flow control.
- **Built-in Print Functionality**: Simplified output with a built-in print function that supports various data types.
- **Error Handling**: Offers straightforward error reporting to ease debugging.

## Getting Started

These instructions will guide you through setting up the Bliss programming environment on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or later
- PLY (Python Lex-Yacc). You can learn more about PLY and its capabilities [here](https://www.dabeaz.com/ply/ply.html).

### Installing

Follow these steps to get your development environment running:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/SER-502-Group-27/SER502-Bliss-Team27.git
   cd SER502-Bliss-Team27

2. **Set up the environment**:
conda create -n bliss-env python=3.6
conda activate bliss-env
pip install ply

3. **Run a sample program**
python src/parser.py tests/sample.bs
