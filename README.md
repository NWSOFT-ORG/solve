# Solve
A tool to solve linear equations in one unknown
## Introduction of NWSh
This is part of the NWSh project. NWSh is a shell that has got all sorts of useful
tools that you need, which is fully extensible in Python.
## Structure
```text
plugin/
    +- solve.json   -- NWSh plugin data
src/
    +- interface.py -- Input and output functions
    +- solver.py    -- Wrapper of sympy solve
main.py             -- Entrypoint
```