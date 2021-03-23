import Vigenere

criptograma = 'QB HN DNKRZ RQ ZN MSGGYI RQ QHYG GSDJFQ BB QMBIIW OOCEDSKQV VC TO ZUUAS KQSYDB VAOMR CB TWQADZS'
clave = 'MONASTERIO'
Vigenere.generar_tabla(Vigenere.ALFABETO)
print(Vigenere.descifrarMensaje(clave, criptograma))
