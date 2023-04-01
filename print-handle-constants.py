#!/usr/bin/env python3

abi_short_size     = 2
abi_int_size       = 4
abi_long_size      = 8
abi_long_long_size = 8

abi_fortran_integer_size = 4
abi_fortran_logical_size = 4
abi_fortran_real_size    = 4
abi_fortran_complex_size = 8

constants    = ["" for x in range(0,1025)]
handle_types = ["" for x in range(0,1025)]

def parse_datatype(h):
    handle_types[h] = "MPI_Datatype"
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
                            constants[h] = "MPI_INT8_T"
                        case 0b0001:
                            constants[h] = "MPI_UINT8_T"
                        case 0b0010:
                            constants[h] = "<float 8b>"
                        case 0b0100:
                            constants[h] = "MPI_SIGNED_CHAR"
                        case 0b0101:
                            constants[h] = "MPI_UNSIGNED_CHAR"
                        case 0b0110:
                            constants[h] = "MPI_C_BOOL"
                        case 0b0111:
                            constants[h] = "MPI_CXX_BOOL"
                        case _:
                            constants[h] = "reserved datatype"
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INTEGER1"
                        case 0b0001:
                            constants[h] = "MPI_LOGICAL1 (not standard)"
                        case 0b0010:
                            constants[h] = "MPI_REAL1"
                        case 0b1111:
                            constants[h] = "MPI_BYTE"
                        case _:
                            constants[h] = "reserved datatype"
            case 2:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INT16_T"
                        case 0b0001:
                            constants[h] = "MPI_UINT16_T"
                        case 0b0010:
                            constants[h] = "<float 16b>"
                        case 0b0011:
                            constants[h] = "<C complex 2x8b>"
                        case 0b0111:
                            constants[h] = "<C++ complex 2x8b>"
                        case _:
                            constants[h] = "reserved datatype"
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INTEGER2"
                        case 0b0001:
                            constants[h] = "MPI_LOGICAL2 (not standard)"
                        case 0b0010:
                            constants[h] = "MPI_REAL2"
                        case 0b0011:
                            constants[h] = "<Fortran complex 2x8b>"
                        case _:
                            constants[h] = "reserved datatype"
            case 4:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INT32_T"
                        case 0b0001:
                            constants[h] = "MPI_UINT32_T"
                        case 0b0010:
                            constants[h] = "MPI_FLOAT"
                        case 0b0011:
                            constants[h] = "<C complex 2x16b>"
                        case 0b0111:
                            constants[h] = "<C++ complex 2x16b>"
                        case _:
                            constants[h] = "reserved datatype"
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INTEGER4"
                        case 0b0001:
                            constants[h] = "MPI_LOGICAL4 (not standard)"
                        case 0b0010:
                            constants[h] = "MPI_REAL4"
                        case 0b0011:
                            constants[h] = "MPI_COMPLEX4"
                        case _:
                            constants[h] = "reserved datatype"
            case 8:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INT64_T"
                        case 0b0001:
                            constants[h] = "MPI_UINT64_T"
                        case 0b0010:
                            constants[h] = "MPI_DOUBLE"
                        case 0b0011:
                            constants[h] = "MPI_C_FLOAT_COMPLEX"
                        case 0b0111:
                            constants[h] = "MPI_CXX_FLOAT_COMPLEX"
                        case _:
                            constants[h] = "reserved datatype"
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INTEGER8"
                        case 0b0001:
                            constants[h] = "MPI_LOGICAL8 (not standard)"
                        case 0b0010:
                            constants[h] = "MPI_REAL8"
                        case 0b0011:
                            constants[h] = "MPI_COMPLEX8"
                        case 0b0111:
                            constants[h] = "MPI_DOUBLE_PRECISION"
                        case _:
                            constants[h] = "reserved datatype"
            case 16:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case 0b0000:
                            constants[h] = "<C int128_t>"
                        case 0b0001:
                            constants[h] = "<C uint128_t>"
                        case 0b0010:
                            constants[h] = "<C float128_t>"
                        case 0b0011:
                            constants[h] = "MPI_C_DOUBLE_COMPLX"
                        case 0b0111:
                            constants[h] = "MPI_CXX_DOUBLE_COMPLEX"
                        case _:
                            constants[h] = "reserved datatype"
                # Fortran and other
                else:
                    match kind:
                        case 0b0000:
                            constants[h] = "MPI_INTEGER16"
                        case 0b0001:
                            constants[h] = "MPI_LOGICAL16 (not standard)"
                        case 0b0010:
                            constants[h] = "MPI_REAL16"
                        case 0b0011:
                            constants[h] = "MPI_COMPLEX16"
                        case 0b0111:
                            constants[h] = "MPI_DOUBLE_COMPLEX"
                        case _:
                            constants[h] = "reserved datatype"
            case 32:
                kind = (h & 0b1111)
                # C/C++
                if not(h & 0b10000):
                    match kind:
                        case _:
                            constants[h] = "reserved datatype"
                # Fortran and other
                else:
                    match kind:
                        case 0b0011:
                            constants[h] = "MPI_COMPLEX32"
                        case _:
                            constants[h] = "reserved datatype"
            case _:
                constants[h] = "reserved datatype"
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
                            string = "MPI_SHORT of " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case 0b001:
                        if (bytesize == abi_int_size):
                            string = "MPI_INT of " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case 0b010:
                        if (bytesize == abi_long_size):
                            string = "MPI_LONG of " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case 0b011:
                        if (bytesize == abi_long_long_size):
                            string = "MPI_LONG_LONG of " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case 0b100:
                        if (bytesize == abi_short_size):
                            string = "MPI_UNSIGNED_SHORT " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case 0b101:
                        if (bytesize == abi_int_size):
                            string = "MPI_UNSIGNED_INT " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case 0b110:
                        if (bytesize == abi_long_size):
                            string = "MPI_UNSIGNED_LONG " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case 0b111:
                        if (bytesize == abi_long_long_size):
                            string = "MPI_UNSIGNED_LONG_LONG " + str(bytesize) + " bytes"
                            constants[h] = string
                        else:
                            constants[h] = "reserved datatype"
                    case _:
                        constants[h] = "reserved datatype"

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
                                string = "MPI_INTEGER of " + str(bytesize) + " bytes"
                                constants[h] = string
                            else:
                                constants[h] = "reserved datatype"
                        case 0b01:
                            if (bytesize == abi_fortran_logical_size):
                                string = "MPI_LOGICAL of " + str(bytesize) + " bytes"
                                constants[h] = string
                            else:
                                constants[h] = "reserved datatype"
                        case 0b10:
                            if (bytesize == abi_fortran_real_size):
                                string = "MPI_REAL of " + str(bytesize) + " bytes"
                                constants[h] = string
                            else:
                                constants[h] = "reserved datatype"
                        case 0b11:
                            if (bytesize == abi_fortran_complex_size):
                                string = "MPI_COMPLEX of " + str(bytesize) + " bytes"
                                constants[h] = string
                            else:
                                constants[h] = "reserved datatype"
                else:
                    if (h & 0b11111 == 0b00000):
                        constants[h] = "MPI_WCHAR_T"
                    elif (h & 0b11111 == 0b00001):
                        constants[h] = "MPI_LB"
                    elif (h & 0b11111 == 0b00010):
                        constants[h] = "MPI_UB"
                    else:
                        constants[h] = "reserved datatype"

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
                                constants[h] = "MPI_AINT"
                            case 0b01:
                                constants[h] = "MPI_COUNT"
                            case 0b10:
                                constants[h] = "MPI_OFFSET"
                            case _:
                                constants[h] = "reserved datatype"
                    case 0b0001:
                        subkind = (h & 0b11)
                        match subkind:
                            case 0b00:
                                constants[h] = "MPI_PACKED"
                            case 0b01:
                                constants[h] = "MPI_DATATYPE_NULL"
                            case _:
                                constants[h] = "reserved datatype"
                        
                    case _:
                        constants[h] = "reserved datatype"

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
                                    constants[h] = "MPI_FLOAT_INT"
                                case 0b001:
                                    constants[h] = "MPI_DOUBLE_INT"
                                case 0b010:
                                    constants[h] = "MPI_LONG_INT"
                                case 0b011:
                                    constants[h] = "MPI_2INT"
                                case 0b100:
                                    constants[h] = "MPI_SHORT_INT"
                                case 0b101:
                                    constants[h] = "MPI_LONG_DOUBLE_INT"
                                case _:
                                    constants[h] = "reserved datatype"
                        # Fortran pair types
                        case 0b01:
                            match subkind:
                                case 0b000:
                                    constants[h] = "MPI_2REAL"
                                case 0b001:
                                    constants[h] = "MPI_2DOUBLE_PRECISION"
                                case 0b010:
                                    constants[h] = "MPI_2INTEGER"
                                case _:
                                    constants[h] = "reserved datatype"
                        case _:
                            constants[h] = "reserved datatype"
                # other
                else:
                    # long double
                    if (h & 0b11000) == 0b00000:
                        # real
                        if (h & 0b100) == 0b000:
                            language = (h & 0b11)
                            match language:
                                case 0b00:
                                    constants[h] = "MPI_LONG_DOUBLE"
                                case 0b10:
                                    constants[h] = "<Fortran long double>"
                                case _:
                                    constants[h] = "reserved datatype"
                        # complex
                        else:
                            language = (h & 0b11)
                            match language:
                                case 0b00:
                                    constants[h] = "MPI_C_LONG_DOUBLE_COMPLEX"
                                case 0b01:
                                    constants[h] = "MPI_CXX_LONG_DOUBLE_COMPLEX"
                                case 0b10:
                                    constants[h] = "<Fortran long double complex>"
                                case _:
                                    constants[h] = "reserved datatype"

                    else:
                        constants[h] = "reserved datatype"


def parse_other(h):
    handle_type = h & 0b11111100
    if   (handle_type == 0b00000000):
        handle_types[h] = "MPI_Comm"
        comm_type = (h & 0b11) 
        if   (comm_type == 0b00):
            constants[h] = "MPI_COMM_NULL"
        elif (comm_type == 0b01):
            constants[h] = "MPI_COMM_WORLD"
        elif (comm_type == 0b10):
            constants[h] = "MPI_COMM_SELF"
        else:
            constants[h] = "reserved comm"
    elif (handle_type == 0b00000100):
        handle_types[h] = "MPI_Group"
        group_type = (h & 0b11) 
        if   (group_type == 0b00):
            constants[h] = "MPI_GROUP_NULL"
        elif (group_type == 0b01):
            constants[h] = "MPI_GROUP_EMPTY"
        else:
            constants[h] = "reserved group"
    elif (handle_type == 0b00001000):
        handle_types[h] = "MPI_Win"
        win_type = (h & 0b11) 
        if   (win_type == 0b00):
            constants[h] = "MPI_WIN_NULL"
        else:
            constants[h] = "reserved win"
    elif (handle_type == 0b00001100):
        handle_types[h] = "MPI_File"
        file_type = (h & 0b11) 
        if   (file_type == 0b00):
            constants[h] = "MPI_FILE_NULL"
        else:
            constants[h] = "reserved file"
    elif (handle_type == 0b00010000):
        handle_types[h] = "MPI_Session"
        session_type = (h & 0b11) 
        if   (session_type == 0b00):
            constants[h] = "MPI_SESSION_NULL"
        else:
            constants[h] = "reserved session"
    elif (handle_type == 0b00010100):
        handle_types[h] = "MPI_Message"
        message_type = (h & 0b11) 
        if   (message_type == 0b00):
            constants[h] = "MPI_MESSAGE_NULL"
        elif (message_type == 0b01):
            constants[h] = "MPI_MESSAGE_NO_PROC"
        else:
            constants[h] = "reserved message"
    elif (handle_type == 0b00011000):
        handle_types[h] = "MPI_Errhandler"
        errhandler_type = (h & 0b11) 
        if   (errhandler_type == 0b00):
            constants[h] = "MPI_ERRHANDLER_NULL"
        elif (errhandler_type == 0b01):
            constants[h] = "MPI_ERRORS_ARE_FATAL"
        elif (errhandler_type == 0b10):
            constants[h] = "MPI_ERRORS_RETURN"
        elif (errhandler_type == 0b11):
            constants[h] = "MPI_ERRORS_ABORT"
    elif (handle_type == 0b00100000):
        handle_types[h] = "MPI_Request"
        request_type = (h & 0b11) 
        if (request_type == 0b00):
            constants[h] = "MPI_REQUEST_NULL"
        else:
            constants[h] = "reserved request"
    else:
        constants[h] = "reserved handle"



def parse_op(h):
    handle_types[h] = "MPI_Op"
    op_type = h & 0b11000
    if   (op_type == 0b00000):
        # arithmetic
        op = h & 0b111
        if   (op == 0b000):
            constants[h] = "MPI_OP_SUM"
        elif (op == 0b001):
            constants[h] = "MPI_OP_MIN"
        elif (op == 0b010):
            constants[h] = "MPI_OP_MAX"
        elif (op == 0b011):
            constants[h] = "MPI_OP_PROD"
        else:
            constants[h] = "reserved arithmetic op"
    elif (op_type == 0b01000):
        # bit ops
        op = h & 0b111
        if   (op == 0b000):
            constants[h] = "MPI_OP_BAND"
        elif (op == 0b001):
            constants[h] = "MPI_OP_BOR"
        elif (op == 0b010):
            constants[h] = "MPI_OP_BXOR"
        else:
            constants[h] = "reserved bit op"
    elif (op_type == 0b10000):
        # logical ops
        op = h & 0b111
        if   (op == 0b000):
            constants[h] = "MPI_OP_LAND"
        elif (op == 0b001):
            constants[h] = "MPI_OP_LOR"
        elif (op == 0b010):
            constants[h] = "MPI_OP_LXOR"
        else:
            constants[h] = "reserved logical op"
    elif (op_type == 0b11000):
        # other ops
        op = h & 0b111
        if   (op == 0b000):
            constants[h] = "MPI_OP_MINLOC"
        elif (op == 0b001):
            constants[h] = "MPI_OP_MAXLOC"
        elif (op == 0b100):
            constants[h] = "MPI_OP_REPLACE"
        elif (op == 0b101):
            constants[h] = "MPI_OP_REPLACE"
        elif (op == 0b110):
            constants[h] = "MPI_OP_NULL"
        else:
            constants[h] = "reserved other op"

def parse_handle(h):
    # if h > 1023 also works :-)
    if (h & 0b1111111111111111111111111111111111111111111111111111110000000000):
        constants[h] = "not a predefined handle constant"
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
                    constants[h] = "reserved as invalid (uninitialized)"
                else:
                    constants[h] = "reserved handle"
            elif (h & 0b0011100000 == 0b0000100000):
                parse_op(h)
            else:
                constants[h] = "reserved handle"
        

def main():
    for h in range(0,1025):
        parse_handle(h)

    for h in range(0,1025):
        if constants[h][0:4] == 'MPI_':
            print(h,constants[h],handle_types[h],hex(h))

if __name__ == '__main__':
    main()

