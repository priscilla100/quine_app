# Self-Replicating Quine

This Python program demonstrates the concept of a **self-replicating Quine**. A Quine is a program that produces its own source code as its output. In this Quine, the program is designed to print its own source code.

## How it Works

The Quine program consists of two classes:

1. **SelfReplicatingProgram**: An abstract base class defining the structure of a self-replicating program.
   
2. **Quine**: A concrete subclass of SelfReplicatingProgram that implements the self-replication functionality.

The Quine class overrides the `print_source` method of the SelfReplicatingProgram class. This method generates the source code of the program by splitting the header (which contains import statements and class definitions) into lines, escaping newline characters, and printing each line.

## Usage

To run the Quine program, simply execute it using a Python interpreter:

```bash
python quine.py
