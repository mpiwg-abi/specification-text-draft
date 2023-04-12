# Huffman Code

We reserve the range 0..1024 for predefined handles.
This requires 10 bits.
The Huffman code allows us to define
unique values for every predefine handle, which is
useful for debugging purposes.
In the coding scheme, handle kinds can be distinguished
using simple bit-mask operations.
Within each handle type, handles are grouped to 


See print-handle-constants.py for the implementation...
