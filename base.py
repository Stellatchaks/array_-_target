def base(inputbase,number,outputbase):
    if inputbase==10:
        
     if outputbase == 2:
        return bin(number)[2:]  
     elif outputbase == 8:
        return oct(number)[2:]  
     elif outputbase == 16:
        return hex(number)[2:]

print(base(10,36,2))