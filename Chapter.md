# Application Binary Interface

Historically, MPI specified an Application Programminng Interface, which defined
a set of opaque handle types and named constants without specifying their memory
layout or values, respectively.
This allowed implementations to choose these according different types of requirement.
However, this flexibility means that different implementations are incompatible
from the perspective of compiled applications, because the Application Binary Interface (ABI)
is not specified.

This chapter defines an Application Binary Interface (ABI) for MPI, meaning that it specifies
the memory layouts of all opaque types, the values of integer constants and other aspects
of MPI required by use cases that require a defined ABI.
The standard MPI ABI exists in parallel with existing implementation ABIs, in order to
preserve backwards-compatibility of existing MPI implementations.

A standard MPI ABI serves many purposes, including support for third-party languages
that intend to call MPI directly from the ABI, rather than via the API using C code, for example.

## The MPI ABI header file and shared library

The ABI should be implemented using a header named `mpi.h`, to ensure that users
can adopt the ABI without code changes.  If another `mpi.h` that defines
a different ABI already exists, implementations should documented the locations
and behavors of these headers and associated object files.

For example, an implementation may have its own ABI defined in `path/include/mpi.h`
and `path/lib/libmpi.so`, in which case, `path/abi/include/mpi.h` and
`path/abi/lib/libmpi.so` indicate to the user that these files are associated with
the MPI standard ABI.

## The Status Object

The `MPI_Status` object is 256-bit struct of 8 integers containing the three
public member fields described in Section 3.2.5 ("Return Status").
The 5 private fields are reserved for implementations and must never be
accessed or set by applications.

## Opaque Handles

Handles for MPI objects are defined to be incomplete struct pointers,
which allows for C compilers to do type-checking, while also satisfying
the existing requirements, such as equality comparison.

Rationale: _Integer handles do not provide type safety, while `struct`
or `union` handles fail to satisfy the existing API requirements._

The following handle type definitions are part of the MPI ABI:
```c
typedef struct mpi_abi_comm * MPI_Comm;
typedef struct mpi_abi_request * MPI_Request;
...
```

## Handle constants

Every handle type has at least one and often many predefined constants of that type.
The MPI ABI defines handle constants to be compile-time constants, which are specified
as integers.

Rationale: _Link-time constants, while convenient, are not strictly portable._

All predefined handle constants correspond to integer representations that are not
valid addresses.  Implementations must ensure that the handles they create for the user
are never in the range reserved for predefined handle constants.
The MPI ABI reservers addresses corresponding to the integers 1 to 4095 for predefined
constants.

Advice to implementers: _Many operating systems support a "zero page" the corresponds
to the above address range, in which case, implementations will not need to do any
runtime checking to ensure the above requirement is satisfied._

## Integer Constants

Integer constants fall into groups, where all groups must have unique
values.  To enforce unique values, groups of integer constants are defined in
anonymous unions.

In cases where integer constants are combined using bitwise logical
expressions, there are additional requirements, specified elsewhere
(e.g. Section 14.2 under `MPI_File_open`).

A different constraint
exists in cases like `MPI_ANY_SOURCE`, which must be negative, because
any non-negative integer may be a valid rank.

All of the constants are specified in the Appendix.

## Fortran

If we standardize an ABI based on MPI F08, discuss it here.


