#!/usr/bin/env python3

abi_short_size     = 2
abi_int_size       = 4
abi_long_size      = 8
abi_long_long_size = 8

abi_fortran_integer_size = 4
abi_fortran_logical_size = 4
abi_fortran_real_size    = 4
abi_fortran_complex_size = 8

def parse_datatype(h):
    is_simple = not(h & 0b100000000)
    if is_simple:
        log2size = (h & 0b11100000) >> 5
        bytesize = 1 << log2size
        match bytesize:
            case 1:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            print("MPI_INT8_T")
                        case 0b0001:
                            print("MPI_UINT8_T")
                        case 0b0010:
                            print("<float 8b>")
                        case 0b0100:
                            print("MPI_SIGNED_CHAR")
                        case 0b0101:
                            print("MPI_UNSIGNED_CHAR")
                        case 0b0110:
                            print("MPI_C_BOOL")
                        case 0b0111:
                            print("MPI_CXX_BOOL")
                        case _:
                            print("reserved datatype")
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            print("MPI_INTEGER1")
                        case 0b0001:
                            print("MPI_LOGICAL1 (not standard)")
                        case 0b0010:
                            print("MPI_REAL1")
                        case 0b1111:
                            print("MPI_BYTE")
                        case _:
                            print("reserved datatype")
            case 2:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            print("MPI_INT16_T")
                        case 0b0001:
                            print("MPI_UINT16_T")
                        case 0b0010:
                            print("<float 16b>")
                        case 0b0011:
                            print("<C complex 2x8b>")
                        case 0b0111:
                            print("<C++ complex 2x8b>")
                        case _:
                            print("reserved datatype")
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            print("MPI_INTEGER2")
                        case 0b0001:
                            print("MPI_LOGICAL2 (not standard)")
                        case 0b0010:
                            print("MPI_REAL2")
                        case 0b0011:
                            print("<Fortran complex 2x8b>")
                        case _:
                            print("reserved datatype")
            case 4:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            print("MPI_INT32_T")
                        case 0b0001:
                            print("MPI_UINT32_T")
                        case 0b0010:
                            print("MPI_FLOAT")
                        case 0b0011:
                            print("<C complex 2x16b>")
                        case 0b0111:
                            print("<C++ complex 2x16b>")
                        case _:
                            print("reserved datatype")
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            print("MPI_INTEGER4")
                        case 0b0001:
                            print("MPI_LOGICAL4 (not standard)")
                        case 0b0010:
                            print("MPI_REAL4")
                        case 0b0011:
                            print("MPI_COMPLEX4")
                        case _:
                            print("reserved datatype")
            case 8:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            print("MPI_INT64_T")
                        case 0b0001:
                            print("MPI_UINT64_T")
                        case 0b0010:
                            print("MPI_DOUBLE")
                        case 0b0011:
                            print("MPI_C_FLOAT_COMPLEX")
                        case 0b0111:
                            print("MPI_CXX_FLOAT_COMPLEX")
                        case _:
                            print("reserved datatype")
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            print("MPI_INTEGER8")
                        case 0b0001:
                            print("MPI_LOGICAL8 (not standard)")
                        case 0b0010:
                            print("MPI_REAL8")
                        case 0b0011:
                            print("MPI_COMPLEX8")
                        case 0b0111:
                            print("MPI_DOUBLE_PRECISION")
                        case _:
                            print("reserved datatype")
            case 16:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            print("<C int128_t>")
                        case 0b0001:
                            print("<C uint128_t>")
                        case 0b0010:
                            print("<C float128_t>")
                        case 0b0011:
                            print("MPI_C_DOUBLE_COMPLX")
                        case 0b0111:
                            print("MPI_CXX_DOUBLE_COMPLEX")
                        case _:
                            print("reserved datatype")
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            print("MPI_INTEGER16")
                        case 0b0001:
                            print("MPI_LOGICAL16 (not standard)")
                        case 0b0010:
                            print("MPI_REAL16")
                        case 0b0011:
                            print("MPI_COMPLEX16")
                        case 0b0111:
                            print("MPI_DOUBLE_COMPLEX")
                        case _:
                            print("reserved datatype")
            case 32:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case _:
                            print("reserved datatype")
                # Fortran and other
                else:
                    match kind:
                        case 0b0011:
                            print("MPI_COMPLEX32")
                        case _:
                            print("reserved datatype")
            case _:
                print("reserved datatype")
    # not simple
    else:
        language_default = not(h & 0b10000000)
        if language_default:
            # C integers
            if not(h & 0b1000000):
                kind = (h & 0b111000) >> 3
                log2size = (h & 0b111)
                bytesize = 1 << log2size
                match kind:
                    case 0b000:
                        if (bytesize == abi_short_size):
                            print("MPI_SHORT of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case 0b001:
                        if (bytesize == abi_int_size):
                            print("MPI_INT of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case 0b010:
                        if (bytesize == abi_long_size):
                            print("MPI_LONG of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case 0b011:
                        if (bytesize == abi_long_long_size):
                            print("MPI_LONG_LONG of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case 0b100:
                        if (bytesize == abi_short_size):
                            print("MPI_UNSIGNED_SHORT of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case 0b101:
                        if (bytesize == abi_int_size):
                            print("MPI_UNSIGNED_INT of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case 0b110:
                        if (bytesize == abi_long_size):
                            print("MPI_UNSIGNED_LONG of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case 0b111:
                        if (bytesize == abi_long_long_size):
                            print("MPI_UNSIGNED_LONG_LONG of",bytesize,"bytes")
                        else:
                            print("reserved datatype")
                    case _:
                        print("reserved datatype")

            # other
            else:
                # Fortran
                if not(h & 0b100000):
                    kind = (h & 0b11000) >> 3
                    log2size = (h & 0b111)
                    bytesize = 1 << log2size
                    match kind:
                        case 0b00:
                            if (bytesize == abi_fortran_integer_size):
                                print("MPI_INTEGER of",bytesize,"bytes")
                            else:
                                print("reserved datatype")
                        case 0b01:
                            if (bytesize == abi_fortran_logical_size):
                                print("MPI_LOGICAL of",bytesize,"bytes")
                            else:
                                print("reserved datatype")
                        case 0b10:
                            if (bytesize == abi_fortran_real_size):
                                print("MPI_REAL of",bytesize,"bytes")
                            else:
                                print("reserved datatype")
                        case 0b11:
                            if (bytesize == abi_fortran_complex_size):
                                print("MPI_COMPLEX of",bytesize,"bytes")
                            else:
                                print("reserved datatype")
                else:
                    if (h & 0b11111 == 0):
                        print("MPI_WCHAR_T")
                    else:
                        print("reserved datatype")

        # other
        else:
            # language independent types
            if not(h & 0b1000000):
                kind = (h & 0b111100) >> 2
                match kind:
                    case 0b0000:
                        subkind = (h & 0b11)
                        match subkind:
                            case 0b00:
                                print("MPI_AINT")
                            case 0b01:
                                print("MPI_COUNT")
                            case 0b10:
                                print("MPI_OFFSET")
                            case _:
                                print("reserved datatype")
                    case 0b0001:
                        subkind = (h & 0b11)
                        match subkind:
                            case 0b00:
                                print("MPI_PACKED")
                            case 0b01:
                                print("MPI_DATATYPE_NULL")
                            case _:
                                print("reserved datatype")
                        
                    case _:
                        print("reserved datatype")

            # other
            else:
                # pair types
                if not(h & 0b100000):
                    kind    = (h & 0b11000) >> 3
                    subkind = (h & 0b111)
                    match kind:
                        # C pair types
                        case 0b00:
                            match subkind:
                                case 0b000:
                                    print("MPI_FLOAT_INT")
                                case 0b001:
                                    print("MPI_DOUBLE_INT")
                                case 0b010:
                                    print("MPI_LONG_INT")
                                case 0b011:
                                    print("MPI_2INT")
                                case 0b100:
                                    print("MPI_SHORT_INT")
                                case 0b101:
                                    print("MPI_LONG_DOUBLE_INT")
                                case _:
                                    print("reserved datatype")
                        # Fortran pair types
                        case 0b01:
                            match subkind:
                                case 0b000:
                                    print("MPI_2REAL")
                                case 0b001:
                                    print("MPI_2DOUBLE_PRECISION")
                                case 0b010:
                                    print("MPI_2INTEGER")
                                case _:
                                    print("reserved datatype")
                        case _:
                            print("reserved datatype")
                # other
                else:
                    # long double
                    if (h & 0b11000) == 0b00000:
                        # real
                        if (h & 0b100) == 0b000:
                            language = (h & 0b11)
                            match language:
                                case 0b00:
                                    print("MPI_LONG_DOUBLE")
                                case 0b10:
                                    print("<Fortran long double>")
                                case _:
                                    print("reserved datatype")
                        # complex
                        else:
                            language = (h & 0b11)
                            match language:
                                case 0b00:
                                    print("MPI_C_LONG_DOUBLE_COMPLEX")
                                case 0b01:
                                    print("MPI_CXX_LONG_DOUBLE_COMPLEX")
                                case 0b10:
                                    print("<Fortran long double complex>")
                                case _:
                                    print("reserved datatype")

                    else:
                        print("reserved datatype")


def parse_other(h):
    handle_type = h & 0b11111100
    if   (handle_type == 0b00000000):
        comm_type = (h & 0b11) 
        if   (comm_type == 0b00):
            print("MPI_COMM_NULL")
        elif (comm_type == 0b01):
            print("MPI_COMM_WORLD")
        elif (comm_type == 0b10):
            print("MPI_COMM_SELF")
        else:
            print("reserved comm")
    elif (handle_type == 0b00000100):
        group_type = (h & 0b11) 
        if   (group_type == 0b00):
            print("MPI_GROUP_NULL")
        elif (group_type == 0b01):
            print("MPI_GROUP_EMPTY")
        else:
            print("reserved group")
    elif (handle_type == 0b00001000):
        win_type = (h & 0b11) 
        if   (win_type == 0b00):
            print("MPI_WIN_NULL")
        else:
            print("reserved win")
    elif (handle_type == 0b00001100):
        file_type = (h & 0b11) 
        if   (file_type == 0b00):
            print("MPI_FILE_NULL")
        else:
            print("reserved file")
    elif (handle_type == 0b00010000):
        session_type = (h & 0b11) 
        if   (session_type == 0b00):
            print("MPI_SESSION_NULL")
        else:
            print("reserved session")
    elif (handle_type == 0b00010100):
        message_type = (h & 0b11) 
        if   (message_type == 0b00):
            print("MPI_MESSAGE_NULL")
        elif (message_type == 0b01):
            print("MPI_MESSAGE_NO_PROC")
        else:
            print("reserved message")
    elif (handle_type == 0b00011000):
        errhandler_type = (h & 0b11) 
        if   (errhandler_type == 0b00):
            print("MPI_ERRHANDLER_NULL")
        elif (errhandler_type == 0b01):
            print("MPI_ERRORS_ARE_FATAL")
        elif (errhandler_type == 0b10):
            print("MPI_ERRORS_RETURN")
        elif (errhandler_type == 0b11):
            print("MPI_ERRORS_ABORT")
    elif (handle_type == 0b00100000):
        request_type = (h & 0b11) 
        if (request_type == 0b00):
            print("MPI_REQUEST_NULL")
        else:
            print("reserved request")
    else:
        print("reserved handle")



def parse_op(h):
    op_type = h & 0b11000
    if   (op_type == 0b00000):
        # arithmetic
        op = h & 0b111
        if   (op == 0b000):
            print("MPI_OP_SUM")
        elif (op == 0b001):
            print("MPI_OP_MIN")
        elif (op == 0b010):
            print("MPI_OP_MAX")
        elif (op == 0b011):
            print("MPI_OP_PROD")
        else:
            print("reserved arithmetic op")
    elif (op_type == 0b01000):
        # bit ops
        op = h & 0b111
        if   (op == 0b000):
            print("MPI_OP_BAND")
        elif (op == 0b001):
            print("MPI_OP_BOR")
        elif (op == 0b010):
            print("MPI_OP_BXOR")
        else:
            print("reserved bit op")
    elif (op_type == 0b10000):
        # logical ops
        op = h & 0b111
        if   (op == 0b000):
            print("MPI_OP_LAND")
        elif (op == 0b001):
            print("MPI_OP_LOR")
        elif (op == 0b010):
            print("MPI_OP_LXOR")
        else:
            print("reserved logical op")
    elif (op_type == 0b11000):
        # other ops
        op = h & 0b111
        if   (op == 0b000):
            print("MPI_OP_MINLOC")
        elif (op == 0b001):
            print("MPI_OP_MAXLOC")
        elif (op == 0b100):
            print("MPI_OP_REPLACE")
        elif (op == 0b101):
            print("MPI_OP_REPLACE")
        elif (op == 0b110):
            print("MPI_OP_NULL")
        else:
            print("reserved other op")

def parse_handle(h):
    print(format(h, '4d'), format(h, '011b'), end=": ")
    # if h > 1023 also works :-)
    if (h & 0b1111111111111111111111111111111111111111111111111111110000000000):
        print("not a predefined handle constant")
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
                    print("reserved as invalid (uninitialized)")
                else:
                    print("reserved handle")
            elif (h & 0b0011100000 == 0b0000100000):
                parse_op(h)
            else:
                print("reserved handle")
        

def main():
    for h in range(0,1025):
        parse_handle(h)

if __name__ == '__main__':
    main()

