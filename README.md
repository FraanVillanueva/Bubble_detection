# Bubble Detection and Size distribution
# Objetivo:
Detectar circulos (burbujas en emulsiones, espumas, etc) en imágenes con el fin de optimizar el análisis de muestras. 
Para que una espuma/emulsión sea estable es imperativo que el tamaño de las burbujas sean pequeñas y uniformes, por lo que el análisis de estas es importante para la evaluación de la performance de la muestra.
# Uso:
1. Checkear/installar librerías a usar (opencv-python, numpy, matplotlib, Pillow)
2. Corregir el path de la imagen que desee analizar.
3. Correr programa.
4. Si resultado no es el deseado corregir siguientes parámetros:
  a. Linea 30: min y max de Radio de burbuja a detectar.
  b. Descomentar linea 19-24 en caso de que background de imágen no sea limpio. Jugar con threshold en línea 21.
  
 Este es un projecto ejemplo, puede ser mejorado/ alterado para otro usos.
