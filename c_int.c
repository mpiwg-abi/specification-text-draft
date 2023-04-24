// cc c_int.c && ./a.out

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <limits.h>

#define PRINT(x)  printf("%12s = %20lld\n", #x, (long long int) x)
#define UPRINT(x) printf("%12s = %20llu\n", #x, (unsigned long long int) x)

int main(void)
{
    PRINT(INT_MAX);
    PRINT(INT_MIN);
    UPRINT(UINT_MAX);

    PRINT(LONG_MAX);
    PRINT(LONG_MIN);
    UPRINT(ULONG_MAX);

    PRINT(LLONG_MAX);
    PRINT(LLONG_MIN);
    UPRINT(ULLONG_MAX);

    PRINT(PTRDIFF_MIN);
    PRINT(PTRDIFF_MAX);
    UPRINT(SIZE_MAX);

    PRINT(INTPTR_MAX);
    PRINT(INTPTR_MIN);
    UPRINT(UINTPTR_MAX);

    return 0;
}
