# Huffman Code

We reserve the range 0..1024 for predefined handles.
This requires 10 bits.
Using the following Huffman code allows us to define
unique values for every predefine handle, which is
useful for debugging purposes.
```
0123456789 < bit
0 is not datatype
 0 is op or reserved
  000 reserved
     00000 reserved (invalid)
     .....
  001 is op
     00 arithmetic
       000 SUM
       001 MIN
       010 MAX
       011 PROD
       ... reserved
     01 bit ops
       000 BAND
       001 BOR
       010 BXOR
       ... reserved
     10 logical ops
       000 LAND
       001 LOR
       010 LXOR
       ... reserved
     11 other ops
       0 M**LOC
        00 MINLOC
        01 MAXLOC
        .. reserved
       1 other
        0 RMA ops
         0 REPLACE
         1 NO_OP
        1 other
         0 MPI_OP_NULL
         1 reserved
  ... reserved 
     .... reserved
 1 other
  000000 comm
        00 MPI_COMM_NULL
        01 MPI_COMM_WORLD
        10 MPI_COMM_SELF
        11 reserved
  000001 group
        00 MPI_GROUP_NULL
        01 MPI_GROUP_EMPTY
        .. reserved
  000010 win
        00 MPI_WIN_NULL
        .. reserved
  000011 file
        00 MPI_FILE_NULL
        .. reserved
  000100 session
        00 MPI_SESSION_NULL
        .. reserved
  000101 message
        00 MPI_MESSAGE_NULL
        01 MPI_MESSAGE_NO_PROC
        .. reserved
  000110 errhandler
        00 MPI_ERRHANDLER_NULL
        01 MPI_ERRORS_ARE_FATAL
        10 MPI_ERRORS_RETURN
        11 MPI_ERRORS_ABORT
  000111 reserved
        .. reserved
  001000 request
        00 MPI_REQUEST_NULL
        .. reserved
  ...... reserved
1 is datatype
 0 simple types
  000  1 byte
     0 C and C++
      0000 C int8_t
      0001 C uint8_t
      0010 C (real 8b)
      0011 reserved
      0100 C signed character
      0101 C unsigned character
      0110 C bool
      0111 C++ bool
      1... reserved
     1 Fortran and other
      0000 F integer*1
      0001 F (logical*1)
      0010 F (real*1)
      .... reserved
      1111 MPI_BYTE
  001  2 bytes
     0 C and C++
      0000 C int16_t
      0001 C uint16_t
      0010 C (real 16b)
      0011 C (complex 16b)
      0... reserved
      0111 C++ (complex 16b)
      1... reserved
     1 Fortran and other
      0000 F integer*2
      0001 F (logical*2)
      0010 F real*2
      0011 F (complex*2)
      .... reserved
  010  4 bytes
     0 C and C++
      0000 C int32_t
      0001 C uint32_t
      0010 C float
      0011 C (complex half)
      0... reserved
      0111 C++ (complex half)
      1... reserved
     1 Fortran and other
      0000 F integer*4
      0001 F (logical*4)
      0010 F real*4
      0011 F complex*4
      .... reserved
  011  8 bytes
     0 C and C++
      0000 C int32_t
      0001 C uint32_t
      0010 C double
      0011 C (complex float)
      0... reserved
      0111 C++ (complex float)
      1... reserved
     1 Fortran and other
      0000 F integer*8
      0001 F (logical*8)
      0010 F real*8
      0011 F complex*8
      .... reserved
  100 16 bytes
     0 C and C++
      0000 C (int128_t)
      0001 C (uint128_t)
      0010 C (float128_t)
      0011 C complex double
      0... reserved
      0111 C++ complex double
      1... reserved
     1 Fortran and other
      0000 F integer*16
      0001 F (logical*16)
      0010 F real*16
      0011 F complex*16
      .... reserved
  101 32 bytes
     0 C and C++
      .... reserved
     1 Fortran and other
      .... reserved
      0011 F complex*32
      .... reserved
  110 reserved
     ..... reserved
  111 reserved
     ..... reserved
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
     00001 MPI_LB (deleted)
     00010 MPI_UB (deleted)
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
        01 MPI_DATATYPE_NULL
        .. reserved
    .... reserved
        .. reserved
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
       ... reserved
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
       ... reserved
```
