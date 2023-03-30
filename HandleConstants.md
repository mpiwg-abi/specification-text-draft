# Huffman Code

We reserve the range 0..1024 for predefined handles.
This requires 10 bits.
Using the following Huffman code allows us to define
unique values for every predefine handle, which is
useful for debugging purposes.
```
0123456789 < bit
0 is not datatype
1 is datatype
 0 simple types
  000  1 byte
     0000 C int8_t
     0001 C uint8_t
     0010 C signed character
     0011 C unsigned character
     0100 C bool
     0101 C++ bool
     0110 reserved 
     0111 reserved
     1000 F integer*1
     1001 F (logical*1)
     1xxx reserved
  001  2 bytes
     0000 C int16_t
     0001 C uint16_t
     .... reserved
     1000 F integer*2
     1001 F (logical*2)
     1010 F real*2
     .... reserved
  010  4 bytes
     0000 C int32_t
     0001 C uint32_t
     0010 C float
     0011 C (complex half)
     .... reserved
     1000 F integer*4
     1001 F (logical*4)
     1010 F real*4
     1011 F complex*4
     .... reserved
  011  8 bytes
     0000 C int32_t
     0001 C uint32_t
     0010 C float
     0011 C (complex half)
     .... reserved
     1000 F integer*4
     1001 F (logical*4)
     1010 F real*4
     1011 F complex*4
     .... reserved
  100 16 bytes
  101 32 bytes
 1 other types


 110 other
    0 pair types
     0 C pair types
      000 MPI_FLOAT_INT
      001 MPI_DOUBLE_INT
      010 MPI_LONG_INT
      011 MPI_2INT
      100 MPI_SHORT_INT
      101 MPI_LONG_DOUBLE_INT
      110 reserved
      111 reserved
     1 F pair types
      00 MPI_2REAL
      01 MPI_2DOUBLE_PRECISION
      10 MPI_2INTEGER
      11 reserved
    1 other
     000 MPI_AINT
     001 MPI_COUNT
     010 MPI_OFFSET
     011 reserved
     100 MPI_BYTE
     101 MPI_PACKED
     110 reserved
     111 reserved
 111 reserved
```
