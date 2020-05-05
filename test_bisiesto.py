import Funcion_Bisiesto
import unittest

class Bisiesto_Test(unittest.TestCase):

    def test_div400(self):
        self.assertEqual(Funcion_Bisiesto.bisiesto(1200), True)
        self.assertEqual(Funcion_Bisiesto.bisiesto(1300), False)
        
    def test_div4(self):
        self.assertEqual(Funcion_Bisiesto.bisiesto(2016), True)
        self.assertEqual(Funcion_Bisiesto.bisiesto(2018), False)
        
    def test_div100(self):
        self.assertEqual(Funcion_Bisiesto.bisiesto(2000), True)
        self.assertEqual(Funcion_Bisiesto.bisiesto(1900), False)


if __name__=='__main__':
    unittest.main()
