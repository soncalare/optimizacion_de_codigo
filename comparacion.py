import cProfile
import pstats

# Ejecutar y guardar el perfil del código original
cProfile.run("exec(open('PRIMOS.py').read())", "profiling_original.prof")

# Ejecutar y guardar el perfil del código optimizado
cProfile.run("exec(open('optimizacion1.py').read())", "profiling_optimizado.prof")


# ✅ Convertir los .prof en archivos .txt legibles
def guardar_perfil(nombre_archivo_prof, nombre_archivo_txt):
    with open(nombre_archivo_txt, 'w') as f:
        stats = pstats.Stats(nombre_archivo_prof, stream=f)
        stats.sort_stats('cumulative')  # Orden por tiempo acumulado
        stats.print_stats()

# Guardar los resultados legibles
guardar_perfil("profiling_original.prof", "profiling_original.txt")
guardar_perfil("profiling_optimizado.prof", "profiling_optimizado.txt")

