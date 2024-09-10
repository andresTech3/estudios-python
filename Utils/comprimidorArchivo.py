import aspose.pdf as ap

# Cargar archivo PDF
compressPdfDocument = ap.Document("../pdf/fisica1")

# Crear un objeto de la clase OptimizationOptions
pdfoptimizeOptions = ap.optimization.OptimizationOptions()

# Habilitar la compresión de imágenes
pdfoptimizeOptions.image_compression_options.compress_images = True

# Establecer la calidad de la imagen
pdfoptimizeOptions.image_compression_options.image_quality = 50

# Comprimir PDF
compressPdfDocument.optimize_resources(pdfoptimizeOptions)

# Guarda el PDF comprimido
compressPdfDocument.save("cuaderno de fisica 1 - Andres Narvaez(compres).pdf")
