def esBisiesto():
    
    strAnno= input('Indica año: ')
    anno= int(strAnno)

    while anno !=0:
        if anno%400==0:
            print(anno, 'es bisiesto')
        elif anno%100==0:
            print(anno,'no es bisiesto')
        elif anno%4==0:
            print(anno,'es bisiesto')
        else:
            print(anno,'no es bisiesto')
            
        strAnno=input('Indica año: ')
        anno= int(strAnno)
        
        
esBisiesto()
