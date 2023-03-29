```c
// Error classes
enum {
    MPI_SUCCESS                         = 0,
    MPI_ERR_BUFFER                      = 1,
    MPI_ERR_COUNT                       = 2,
    MPI_ERR_TYPE                        = 3,
    MPI_ERR_TAG                         = 4,
    MPI_ERR_COMM                        = 5,
    MPI_ERR_RANK                        = 6,
    MPI_ERR_REQUEST                     = 7,
    MPI_ERR_ROOT                        = 8,
    MPI_ERR_GROUP                       = 9,
    MPI_ERR_OP                          = 10,
    MPI_ERR_TOPOLOGY                    = 11,
    MPI_ERR_DIMS                        = 12,
    MPI_ERR_ARG                         = 13,
    MPI_ERR_UNKNOWN                     = 14,
    MPI_ERR_TRUNCATE                    = 15,
    MPI_ERR_OTHER                       = 16,
    MPI_ERR_INTERN                      = 17,
    MPI_ERR_PENDING                     = 18,
    MPI_ERR_IN_STATUS                   = 19,
    MPI_ERR_ACCESS                      = 20,
    MPI_ERR_AMODE                       = 21,
    MPI_ERR_ASSERT                      = 22,
    MPI_ERR_BAD_FILE                    = 23,
    MPI_ERR_BASE                        = 24,
    MPI_ERR_CONVERSION                  = 25,
    MPI_ERR_DISP                        = 26,
    MPI_ERR_DUP_DATAREP                 = 27,
    MPI_ERR_FILE_EXISTS                 = 28,
    MPI_ERR_FILE_IN_USE                 = 29,
    MPI_ERR_FILE                        = 30,
    MPI_ERR_INFO_KEY                    = 31,
    MPI_ERR_INFO_NOKEY                  = 32,
    MPI_ERR_INFO_VALUE                  = 33,
    MPI_ERR_INFO                        = 34,
    MPI_ERR_IO                          = 35,
    MPI_ERR_KEYVAL                      = 36,
    MPI_ERR_LOCKTYPE                    = 37,
    MPI_ERR_NAME                        = 38,
    MPI_ERR_NO_MEM                      = 39,
    MPI_ERR_NOT_SAME                    = 40,
    MPI_ERR_NO_SPACE                    = 41,
    MPI_ERR_NO_SUCH_FILE                = 42,
    MPI_ERR_PORT                        = 43,
    MPI_ERR_PROC_ABORTED                = 44,
    MPI_ERR_QUOTA                       = 45,
    MPI_ERR_READ_ONLY                   = 46,
    MPI_ERR_RMA_ATTACH                  = 47,
    MPI_ERR_RMA_CONFLICT                = 48,
    MPI_ERR_RMA_RANGE                   = 49,
    MPI_ERR_RMA_SHARED                  = 50,
    MPI_ERR_RMA_SYNC                    = 51,
    MPI_ERR_RMA_FLAVOR                  = 52,
    MPI_ERR_SERVICE                     = 53,
    MPI_ERR_SESSION                     = 54,
    MPI_ERR_SIZE                        = 55,
    MPI_ERR_SPAWN                       = 56,
    MPI_ERR_UNSUPPORTED_DATAREP         = 57,
    MPI_ERR_UNSUPPORTED_OPERATION       = 58,
    MPI_ERR_VALUE_TOO_LARGE             = 59,
    MPI_ERR_WIN                         = 60,
    MPI_T_ERR_CANNOT_INIT               = 1000,
    MPI_T_ERR_NOT_ACCESSIBLE            = 1001,
    MPI_T_ERR_NOT_INITIALIZED           = 1002,
    MPI_T_ERR_NOT_SUPPORTED             = 1003,
    MPI_T_ERR_MEMORY                    = 1004,
    MPI_T_ERR_INVALID                   = 1005,
    MPI_T_ERR_INVALID_INDEX             = 1006,
    MPI_T_ERR_INVALID_ITEM              = 1007,
    MPI_T_ERR_INVALID_SESSION           = 1008,
    MPI_T_ERR_INVALID_HANDLE            = 1009,
    MPI_T_ERR_INVALID_NAME              = 1010,
    MPI_T_ERR_OUT_OF_HANDLES            = 1011,
    MPI_T_ERR_OUT_OF_SESSIONS           = 1012,
    MPI_T_ERR_CVAR_SET_NOT_NOW          = 1013,
    MPI_T_ERR_CVAR_SET_NEVER            = 1014,
    MPI_T_ERR_PVAR_NO_WRITE             = 1015,
    MPI_T_ERR_PVAR_NO_STARTSTOP         = 1016,
    MPI_T_ERR_PVAR_NO_ATOMIC            = 1017,
    MPI_ERR_LASTCODE                    = 2000,
};
```

```c
// Buffer Address Constants
#define MPI_BOTTOM          ((void*)0)
#define MPI_IN_PLACE        ((void*)1)

// Constants Specifying Empty or Ignored Input
#define MPI_ARGV_NULL       ((char**)0)
#define MPI_ARGVS_NULL      ((char***)0)
#define MPI_ERRCODES_IGNORE ((int*)0)
#define MPI_STATUS_IGNORE   ((MPI_Status*)0)
#define MPI_STATUSES_IGNORE ((MPI_Status*)0)
#define MPI_UNWEIGHTED      ((int*)2)
#define MPI_WEIGHTS_EMPTY   ((int*)3)
```

```c
// Assorted Constants

// rank sentinels - must be negative
enum {
    MPI_ANY_SOURCE      = -1,
    MPI_PROC_NULL       = -2,
    MPI_ROOT            = -4,
};

// tag sentinels - should be negative
enum {
    MPI_ANY_TAG         = -1
};

// multi-purpose sentinel - must be negative
enum {
    MPI_UNDEFINED       = -32766
};

// feature-specific constant
enum {
     MPI_BSEND_OVERHEAD = 512 // MPICH=96, OMPI=128
};

// attribute constant - must be negative
enum {
    MPI_KEYVAL_INVALID  = -1
};

// RMA lock constants - arbitrary values
enum {
    MPI_LOCK_EXCLUSIVE  = 1,
    MPI_LOCK_SHARED     = 2
};
```

```c
// Fortran status array size and reserved index values (in C)
enum {
    MPI_F_STATUS_SIZE   = 8
};

// Status indexing - must match MPI_Status definition
enum {
    MPI_F_SOURCE        = 0,
    MPI_F_TAG           = 1,
    MPI_F_ERROR         = 2
};
```

```c
#define MPI_MAX_DATAREP_STRING               128 // OMPI only has it
#define MPI_MAX_ERROR_STRINGa                512 // MPICH was bigger
#define MPI_MAX_INFO_KEY                     255 // MPICH was bigger
#define MPI_MAX_INFO_VAL                    1024 // MPICH was bigger
#define MPI_MAX_LIBRARY_VERSION_STRING      8192 // MPICH was bigger
#define MPI_MAX_OBJECT_NAME                  128 // MPICH was bigger
#define MPI_MAX_PORT_NAME                   1024 // OMPI was bigger
#define MPI_MAX_PROCESSOR_NAME               256 // OMPI was bigger
#define MPI_MAX_STRINGTAG_LEN                256 // MPICH only has it
#define MPI_MAX_PSET_NAME_LEN                256 // MPICH only has it
```

```c
// Communicator split type constants - arbitrary values
enum {
    MPI_COMM_TYPE_SHARED        = 1,
    MPI_COMM_TYPE_HW_UNGUIDED   = 2,
    MPI_COMM_TYPE_HW_GUIDED     = 4
};
```

```c
//Results of communicator and group comparisons
enum {
    MPI_IDENT       = 0,
    MPI_CONGRUENT   = 1,
    MPI_SIMILAR     = 2,
    MPI_UNEQUAL     = 3
};
```

```c
// Environmental inquiry keys and Predefined Attribute Keys
// These apply to MPI_COMM_WORLD
enum {
    MPI_TAG_UB          = -1,
    MPI_IO              = -2,
    MPI_HOST            = -3,
    MPI_WTIME_IS_GLOBAL = -4,
    MPI_APPNUM          = -5,
    MPI_LASTUSEDCODE    = -6,
    MPI_UNIVERSE_SIZE   = -7
};

// Predefined Attribute Keys
// These apply to Windows
enum {
    MPI_WIN_BASE            = -1,
    MPI_WIN_DISP_UNIT       = -2,
    MPI_WIN_SIZE            = -3,
    MPI_WIN_CREATE_FLAVOR   = -4,
    MPI_WIN_MODEL           = -5
};
```

```c
// MPI Window Create Flavors
enum {
    MPI_WIN_FLAVOR_ALLOCATE = 0xA,
    MPI_WIN_FLAVOR_CREATE   = 0xC,
    MPI_WIN_FLAVOR_DYNAMIC  = 0xD,
    MPI_WIN_FLAVOR_SHARED   = 0x5
```

```c
// MPI Window Models
enum {
    MPI_WIN_SEPARATE    =  1,
    MPI_WIN_UNIFIED     = -1
}
```

```c
// Mode Constants
// must be powers-of-2 to support OR-ing
enum {
    // Files
    MPI_MODE_APPEND             = 1,
    MPI_MODE_CREATE             = 2,
    MPI_MODE_DELETE_ON_CLOSE    = 4,
    MPI_MODE_EXCL               = 8,
    MPI_MODE_RDONLY             = 16,
    MPI_MODE_RDWR               = 32,
    MPI_MODE_SEQUENTIAL         = 64,
    MPI_MODE_UNIQUE_OPEN        = 128,
    MPI_MODE_WRONLY             = 256,
    // Windows
    MPI_MODE_NOCHECK            = 1024,
    MPI_MODE_NOPRECEDE          = 2048,
    MPI_MODE_NOPUT              = 4096,
    MPI_MODE_NOSTORE            = 8192,
    MPI_MODE_NOSUCCEED          = 16384
};
```

```c
// Datatype Decoding Constants
enum {
    MPI_COMBINER_NAMED              = 1,
    MPI_COMBINER_DUP                = 2,
    MPI_COMBINER_CONTIGUOUS         = 3,
    MPI_COMBINER_VECTOR             = 4,
    MPI_COMBINER_HVECTOR            = 5,
    MPI_COMBINER_INDEXED            = 6,
    MPI_COMBINER_HINDEXED           = 7,
    MPI_COMBINER_INDEXED_BLOCK      = 8,
    MPI_COMBINER_HINDEXED_BLOCK     = 9,
    MPI_COMBINER_STRUCT             = 10,
    MPI_COMBINER_SUBARRAY           = 11,
    MPI_COMBINER_DARRAY             = 12,
    MPI_COMBINER_F90_REAL           = 13,
    MPI_COMBINER_F90_COMPLEX        = 14,
    MPI_COMBINER_F90_INTEGER        = 15,
    MPI_COMBINER_RESIZED            = 16
};
```

```c
// Threads Constants
enum {
    MPI_THREAD_SINGLE       = 100,
    MPI_THREAD_FUNNELED     = 200,
    MPI_THREAD_SERIALIZED   = 300,
    MPI_THREAD_MULTIPLE     = 400
};
```

```c
//
enum {
    MPI_DISPLACEMENT_CURRENT = -1
}
```

```c
// File Operation Constants (?)
enum {
    MPI_DISTRIBUTE_BLOCK        = 0xB,
    MPI_DISTRIBUTE_CYCLIC       = 0xC,
    MPI_DISTRIBUTE_DFLT_DARG    = 0xD,
    MPI_DISTRIBUTE_NONE         = 0xE
};

enum {
    MPI_ORDER_C                 = 0xC,
    MPI_ORDER_FORTRAN           = 0xF
};

enum {
    MPI_SEEK_CUR                = 0xC,
    MPI_SEEK_END                = 0xE,
    MPI_SEEK_SET                = 0x5
};
```

```c
// F90 Datatype Matching Constants
enum {
    MPI_TYPECLASS_REAL          = 1,
    MPI_TYPECLASS_COMPLEX       = 2,
    MPI_TYPECLASS_INTEGER       = 3
}
```
