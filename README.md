# 🕹️ Arcade HUD Overlay
Visualizador gráfico de entradas tipo arcade para joystick o teclado, diseñado como overlay para emuladores.
Perfecto para tutoriales de juegos de pelea, demostraciones de habilidad o como herramienta de entrenamiento.

## Características
* El archivo de configuración en "~/.HUDOverlay.toml"
* Soporta joystick y teclado.
* Transparencia total

> Para la configuración controles (porfavor consulte la [api de RAYLIB](https://www.raylib.com/cheatsheet/cheatsheet.html) para saber el codigo de los botones)


## Estado actual del proyecto (Versión 1)
* Se a refactorizado el programa utilizando raylib en vez de Pygame para una mejor compatibilidad
* Se ha optado por usar toml en vez de sqlite para las configuraciones
* Puedes intercalar entre el jostick y teclado pulsando "la flecha Izquierda"

### Por Hacer
1. Crear una UI para la configuración
2. Usar sprite para representar los botones
3. Reconocimiento de combos comunes


## Compilación
No olvides descargar las dependencias de raylib primero:
https://github.com/raysan5/raylib/wiki/Working-on-GNU-Linux

### Requisitos 
* python >= 3.14
* uv >= 0.10
* raylib >= 5.5.0
* nuitka[onefile]>=4.0

### Ejecución

 ```bash
#Clonar el repositorio
git clone https://github.com/MayorTom4815/hud_overlay.git

#Cambiar a la carpeta del proyecto
cd hud_overlay

#Crear el entorno virtual
uv venv

#Descargar las librerias con uv
uv sync

#Activar el entorno virtual en linux
source .venv/bin/activate

#Activar el entorno virtual en windows
.venv/bin/activate.ps1

#Iniciar el programa
make release
```

## 👾 Créditos
Este proyecto fue desarrollado con amor al figthing y **mucha paciencia por leer el codigo de un novato**
**@Cat-not-furry** (creador del proyecto)
