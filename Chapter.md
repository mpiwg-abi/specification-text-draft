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

`mpi_abi.h` and `libmpi_abi.${platform_specific_suffix}`

## The Status Object

256-bit struct of 8 integers.

## Opaque Handles

Incomplete struct pointers.  Discuss details.

The struct names must be specific, because of Rust.  `MPI_ABI_Handle` is favored right now.

## Integer Constants

These might be specified in the appendix tables, but they should be discussed here.

## Fortran

If we standardize an ABI based on MPI F08, discuss it here.


