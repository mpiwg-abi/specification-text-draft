# Huffman Code

We reserve the range 0..1024 for predefined handles.
This requires 10 bits.
Using the following Huffman code allows us to define
unique values for every predefine handle, which is
useful for debugging purposes.
```
0123456789 < bit
0 is not datatype
 0 is op
  00 arithmetic
    000 SUM
    001 MIN
    010 MAX
    011 PROD
    ... reserved
  01 bit ops
    00 BAND
    01 BOR
    10 BXOR
    11 reserved
  10 logical ops
    00 LAND
    01 LOR
    10 LXOR
    11 reserved
  11 other ops
    0 M**LOC
     0 MINLOC
     1 MAXLOC
    1 other
     0 RMA ops
      0 REPLACE
      1 NO_OP
     1 other
      . reserved
 1 other
  0000 comm
      00 MPI_COMM_NULL
      01 MPI_COMM_WORLD
      10 MPI_COMM_SELF
      11 reserved
  0001 group
      00 MPI_GROUP_NULL
      01 MPI_GROUP_EMPTY
      .. reserved
  0010 win
      00 MPI_WIN_NULL
      .. reserved
  0011 file
      00 MPI_FILE_NULL
      .. reserved
  0100 session
      00 MPI_SESSION_NULL
      .. reserved
  0101 message
      00 MPI_MESSAGE_NULL
      01 MPI_MESSAGE_NO_PROC
      .. reserved
  0110 request
      0000 MPI_REQUEST_NULL
      .... reserved
  0111 errhandler
      0000 MPI_ERRHANDLER_NULL
      0001 MPI_ERRORS_ARE_FATAL
      0010 MPI_ERRORS_RETURN
      0011 MPI_ERRORS_ABORT
      .... reserved
  .... reserved
1 is datatype
 0 simple types
  000  1 byte
     0000 C int8_t
     0001 C uint8_t
     0010 C (real 8b)
     0011 reserved
     0100 C signed character
     0101 C unsigned character
     0110 C bool
     0111 C++ bool
     1000 F integer*1
     1001 F (logical*1)
     1010 F (real*1)
     .... reserved
     1111 MPI_BYTE
  001  2 bytes
     0000 C int16_t
     0001 C uint16_t
     0010 C (real 16b)
     0011 C (complex 16b)
     .... reserved
     0111 C++ (complex 16b)
     1000 F integer*2
     1001 F (logical*2)
     1010 F real*2
     1011 F (complex*2)
     .... reserved
  010  4 bytes
     0000 C int32_t
     0001 C uint32_t
     0010 C float
     0011 C (complex half)
     .... reserved
     0111 C++ (complex half)
     1000 F integer*4
     1001 F (logical*4)
     1010 F real*4
     1011 F complex*4
     .... reserved
  011  8 bytes
     0000 C int32_t
     0001 C uint32_t
     0010 C double
     0011 C (complex float)
     .... reserved
     0111 C++ (complex float)
     1000 F integer*8
     1001 F (logical*8)
     1010 F real*8
     1011 F complex*8
     .... reserved
  100 16 bytes
     0000 C (int128_t)
     0001 C (uint128_t)
     0010 C (float128_t)
     0011 C complex double
     .... reserved
     0111 C++ complex double
     1000 F integer*16
     1001 F (logical*16)
     1010 F real*16
     1011 F complex*16
     .... reserved
  101 32 bytes
     .... reserved
     1011 F complex*32
     .... reserved
  110 reserved
  111 reserved
 1 other types
  0 language defaults - these may not be necessary, i.e. can/should be aliases to fixed-size types
   0 C integers
    000 C short
       ... log2(size in bytes)
    001 C int
       ... log2(size in bytes)
    010 C long
       ... log2(size in bytes)
    011 C long long
       ... log2(size in bytes)
    100 C unsigned short
       ... log2(size in bytes)
    101 C unsigned int
       ... log2(size in bytes)
    110 C unsigned long
       ... log2(size in bytes)
    111 C unsigned long long
       ... log2(size in bytes)
   1 other
    0 Fortran default types
     00 F integer
       ... log2(size in bytes)
     01 F logical
       ... log2(size in bytes)
     10 F real
       ... log2(size in bytes)
     11 F complex
       ... log2(size in bytes)
    1 other
     00000 wchar_t
     ..... reserved
  1 other
   0 language-independent types
    0000 special integer types
        00 MPI_AINT
        01 MPI_COUNT
        10 MPI_OFFSET
        11 reserved
    0001 other
        00 MPI_PACKED
        .. reserved
    .... reserved
   1 other
    0 pair types
     00 C pair types
       000 MPI_FLOAT_INT
       001 MPI_DOUBLE_INT
       010 MPI_LONG_INT
       011 MPI_2INT
       100 MPI_SHORT_INT
       101 MPI_LONG_DOUBLE_INT
       110 reserved
       111 reserved
     01 F pair types
       000 MPI_2REAL
       001 MPI_2DOUBLE_PRECISION
       010 MPI_2INTEGER
       ... reserved
     .. reserved
    1 other
     00 long double
       0 real
        00 C
        01 C++
        10 F
        11 reserved
       1 complex
        00 C
        01 C++
        10 F
        11 reserved
     .. reserved
```
