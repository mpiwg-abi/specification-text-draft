#!/usr/bin/env python3

def parse_datatype(h):
    print("")
    return

def parse_other(h):
    handle_type = h & 0b11111100
    if   (handle_type == 0b00000000):
        comm_type = (h & 0b11) 
        if   (comm_type == 0b00):
            print("- MPI_COMM_NULL")
        elif (comm_type == 0b01):
            print("- MPI_COMM_WORLD")
        elif (comm_type == 0b10):
            print("- MPI_COMM_SELF")
        else:
            print("- reserved comm")
    elif (handle_type == 0b00000100):
        group_type = (h & 0b11) 
        if   (group_type == 0b00):
            print("- MPI_GROUP_NULL")
        elif (group_type == 0b01):
            print("- MPI_GROUP_EMPTY")
        else:
            print("- reserved group")
    elif (handle_type == 0b00001000):
        win_type = (h & 0b11) 
        if   (win_type == 0b00):
            print("- MPI_WIN_NULL")
        else:
            print("- reserved win")
    elif (handle_type == 0b00001100):
        file_type = (h & 0b11) 
        if   (file_type == 0b00):
            print("- MPI_FILE_NULL")
        else:
            print("- reserved file")
    elif (handle_type == 0b00010000):
        session_type = (h & 0b11) 
        if   (session_type == 0b00):
            print("- MPI_SESSION_NULL")
        else:
            print("- reserved session")
    elif (handle_type == 0b00010100):
        message_type = (h & 0b11) 
        if   (message_type == 0b00):
            print("- MPI_MESSAGE_NULL")
        elif (message_type == 0b01):
            print("- MPI_MESSAGE_NO_PROC")
        else:
            print("- reserved message")
    elif (handle_type == 0b00011000):
        errhandler_type = (h & 0b11) 
        if   (errhandler_type == 0b00):
            print("- MPI_ERRHANDLER_NULL")
        elif (errhandler_type == 0b01):
            print("- MPI_ERRORS_ARE_FATAL")
        elif (errhandler_type == 0b10):
            print("- MPI_ERRORS_RETURN")
        elif (errhandler_type == 0b11):
            print("- MPI_ERRORS_ABORT")
    elif (handle_type == 0b00100000):
        request_type = (h & 0b11) 
        if (request_type == 0b00):
            print("- MPI_REQUEST_NULL")
        else:
            print("- reserved request")
    else:
        print("- reserved")



def parse_op(h):
    op_type = h & 0b11000
    if   (op_type == 0b00000):
        # arithmetic
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
            print("- reserved arithmetic op")
    elif (op_type == 0b01000):
        # bit ops
        op = h & 0b111
        if   (op == 0b000):
            print("- MPI_OP_BAND")
        elif (op == 0b001):
            print("- MPI_OP_BOR")
        elif (op == 0b010):
            print("- MPI_OP_BXOR")
        else:
            print("- reserved bit op")
    elif (op_type == 0b10000):
        # logical ops
        op = h & 0b111
        if   (op == 0b000):
            print("- MPI_OP_LAND")
        elif (op == 0b001):
            print("- MPI_OP_LOR")
        elif (op == 0b010):
            print("- MPI_OP_LXOR")
        else:
            print("- reserved logical op")
    elif (op_type == 0b11000):
        # other ops
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
            print("- reserved other op")

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

