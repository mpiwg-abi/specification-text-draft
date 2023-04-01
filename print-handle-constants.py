#!/usr/bin/env python3

def parse_datatype(h):
    return

def parse_other(h):
    return


def parse_op(h):
    op_type = h & 0b11000
    if   (op_type == 0b00000):
        #print("- arithmetic")
        op = h & 0b111
        if   (op == 0b000):
            print("- MPI_OP_SUM")
        elif (op == 0b001):
            print("- MPI_OP_MIN")
        elif (op == 0b010):
            print("- MPI_OP_MAX")
        elif (op == 0b011):
            print("- MPI_OP_PROD")
        else:
            print("- reserved")
    elif (op_type == 0b01000):
        #print("- bit ops")
        op = h & 0b111
        if   (op == 0b000):
            print("- MPI_OP_BAND")
        elif (op == 0b001):
            print("- MPI_OP_BOR")
        elif (op == 0b010):
            print("- MPI_OP_BXOR")
        else:
            print("- reserved")
    elif (op_type == 0b10000):
        #print("- logical ops")
        op = h & 0b111
        if   (op == 0b000):
            print("- MPI_OP_LAND")
        elif (op == 0b001):
            print("- MPI_OP_LOR")
        elif (op == 0b010):
            print("- MPI_OP_LXOR")
        else:
            print("- reserved")
    elif (op_type == 0b11000):
        #print("- other ops")
        op = h & 0b111
        if   (op == 0b000):
            print("- MPI_OP_MINLOC")
        elif (op == 0b001):
            print("- MPI_OP_MAXLOC")
        elif (op == 0b100):
            print("- MPI_OP_REPLACE")
        elif (op == 0b101):
            print("- MPI_OP_REPLACE")
        elif (op == 0b110):
            print("- MPI_OP_NULL")
        else:
            print("- reserved")

def parse_handle(h):
    print(format(h, '4d'), format(h, '011b'), end=" ")
    if (h & 0xFFFFF400):
        print("- not a predefined handle constant")
        return

    if (h & 0b1000000000):
        parse_datatype(h)
    else:
        if (h & 0b0100000000):
            parse_other(h)
        else:
            # op or reserved
            if (h & 0b0011100000 == 0):
                if (h & 0b0000011111 == 0):
                    print("- reserved as invalid (uninitialized)")
                else:
                    print("- reserved")
            elif (h & 0b0011100000 == 0b0000100000):
                parse_op(h)
            else:
                print("- reserved")
        

def main():
    for h in range(0,1025):
        parse_handle(h)

if __name__ == '__main__':
    main()

