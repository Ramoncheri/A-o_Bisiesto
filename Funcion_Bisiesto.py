
def bisiesto(anno):
    
    return (anno%4== 0 and anno% 100 !=0) or anno% 400== 0
 
 # Es lo mismo que lo de abajo

 #   if (anno%4== 0 and anno% 100 !=0) or anno% 400== 0:
#        return True
#    else:
 #       return False


def entero(n):
    try:
        int(n)
        return True
    except ValueError:
        return False




