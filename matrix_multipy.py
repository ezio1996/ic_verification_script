def matrix_multipy_signed(input1,input2,bit_num):
    
    if(input1 >=0 and input2 >=0):
        out = input1 * input2 
    elif(input1 <0 and input2 <0):
        #print((abs(input1) ^ bit_num) + 1)
        #print((abs(input2) ^ bit_num) + 1)
        out = ((abs(input1) ^ bit_num) + 1 ) * ((abs(input2) ^ bit_num) + 1 )
    elif(input1 >0 and input2 <0):
        #print((abs(input2) ^ bit_num) + 1)
        out = ((abs(input2) ^ bit_num) + 1 ) * input1 * (-1)
    elif(input1 <0 and input2 >0):
        #print((abs(input1) ^ bit_num) + 1)
        out = ((abs(input1) ^ bit_num) + 1 ) * input2 * (-1)
    return out

if __name__ == "__main__":
    out = matrix_multipy_signed(30, -20, 0b11111)
    print(out)
    out = matrix_multipy_signed(-30, -20, 0b11111)
    print(out)
    out = matrix_multipy_signed(30, 20, 0b11111)
    print(out)