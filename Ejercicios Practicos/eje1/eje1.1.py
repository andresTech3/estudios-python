#promedio de duraciones
otherCoursesMin = 2.5
otherCoursesMax = 7
otherCoursesAverage = 4
daltoCourses = 1.5


#diferencia de duraciones
differencesWithMin = 100 - (daltoCourses / otherCoursesMin * 100)
differencesWithMax = round(100 - (daltoCourses / otherCoursesMax * 100), 1)
differencesWithAverage = 100 - (daltoCourses / otherCoursesAverage * 100)


print(f'el curso de dalto dura un {differencesWithMin} menos que el mas rapido')
print(f'el curso de dalto dura un {differencesWithMax} menos que el mas lento')
print(f'el curso de dalto dura un {differencesWithAverage} menos que el promedio')


