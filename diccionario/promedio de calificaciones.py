def promedio_calificaciones():
    calificaciones = {'Ana': 4.0, 'Luis': 3.5, 'Sofía': 4.5}
    
    promedio = sum(calificaciones.values()) / len(calificaciones)
    print(f"Promedio general: {promedio}")

promedio_calificaciones()