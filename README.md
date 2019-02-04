# PYSPY

Pyspy is injecting tracing into a running Python program by patching its bytecode.
The output is supposed to be displayed in form of sequence diagrams in order to help debugging and program understanding.

## Use it like this:
(See test.py)

```python
import my_module
import pyspy

def trace_call(frame):
    print "Entering:", frame.f_code.co_name

def trace_exit(frame):
    print "Entering:", frame.f_code.co_name

pyspy.patch.apply_patch(my_module.run, trace_call, trace_exit)
my_module.run()
```
