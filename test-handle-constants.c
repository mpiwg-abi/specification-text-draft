#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

void print_binary(int num)
{
    const int bits = 12;
    for (int i = bits-1; i >= 0; i--) {
        if (num & (1 << i)) {
            printf("1");
        } else {
            printf("0");
        }
    }
}

void parse_C_sized_types(int i)
{
    

}

void parse_handle(int i)
{
    print_binary(i);
    printf("\t");

    if (i & 0xFFFFF400) {
        printf("%d is not a valid predefined handle\n", i);
        return;
    }

    if (i & 0x200) {
        // is a datatype
        if (i & 0x100) {
            // not simple types
        }
        else {
            // simple types
            const int log2size = (i & 0xE0) >> 5;
            const int size = 1 << log2size;
            if (i & 0x10) {
                // Fortran and other
            }
            else {
                // C and C++
            }
            //if (size == 1) {
            //printf("log2size = %d size = %d\n", log2size, size);
            //return;
        }
    }
    else {
        // is not a datatype
        if (i & 0x100) {
        }
        else {
            if (i & 0xFF) {
                printf("%d is reserved\n", i);
                return;
            }
            else {
                printf("%d is reserved as invalid (uninitialized)\n", i);
                return;
            }
        }



    }
    printf("?\n");
}

int main(int argc, char* argv[])
{
    for (int i=0; i<=1024; i++) {
        parse_handle(i);
    }
    return 0;
}
