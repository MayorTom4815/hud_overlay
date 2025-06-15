# 🕹️ Arcade HUD Overlay (Linux)

Visualizador gráfico de entradas tipo arcade para joystick o teclado, diseñado como overlay para emuladores.
Perfecto para tutoriales de juegos de pelea, demostraciones de habilidad o como herramienta de entrenamiento.
### Hola

Espero tengas un excelente dia, este overlay lo hice para grabar gameplays, desafortunadamente no me fue posible, si ya conoces mi historia sabras el motivo.
En fin espero te sirva, la logica no es tan complicada por si quieres personalizarlo, si es haci, me haria muy feliz que me mencionaras para ver las mejoras que pudieras haber implementado.

# Estado actual del proyecto 
## (Junio 2025)
### Cosas arregadas
Se redimenciono el tamaño de la ventana del fightstick<br>
Se corrigio el tamaño de las letras y al igual que la interfaz se hubicaron acorde al tamaño de la ventana<br>
Se corrigio el error de main.py (no cargaba key_bindings.json), ya no es necesario remapear en la opcion del teclado, a menos que elimines el archivo, al igual que en el caso de joystick_bindings.json.

## Bueno, a lo que vinimos...
#### Caracteristicas.

Representacion virtual de un Fightsitck para GNU/Linux.<br>
HUD gráfico en Pygame que se muestra encima de otros programas (overlay).<br>
Visualiza un joystick arcade virtual y hasta 6 botones (configurables).<br>
Modo joystick y modo teclado disponibles.<br>
Permite elegir entre formato de 4 o 6 botones, con layout adaptativo.<br>
Cada botón se representa con íconos (por ejemplo: lp.png, hp.png).<br>
Los íconos se iluminan al presionar los botones reales.

#### Asignación de controles

Al iniciar, pregunta:<br>
¿Formato de botones? (4 o 6)<br>
¿Tipo de entrada? (teclado o joystick)<br>
Si eliges teclado, puedes mapear manualmente teclas (una sola vez por formato).<br>
Guarda en bindings.json → formato_4 y formato_6.<br>
Si eliges joystick, puedes mapear cada botón arcade (una sola vez por formato).<br>
Guarda en joystick_bindings.json.

#### 📁 Estructura del proyecto

hud_overlay/<br>
├── main.py<br>
├── config.py<br>
├── input_reader.py<br>
├── joystick_mapper.py<br>
├── keymapper.py<br>
├── hud_renderer.py<br>
├── input_selector.py<br>
├── button_format_selector.py<br>
├── bindings.json<br>
├── joystick_bindings.json<br>
├── libs/<br>
│   ├── pygame/<br>
│   └── evdev/<br>
└── icons/<br>
    ├── lp.png<br>
    ├── mp.png<br>
    └── ...
    
Gracias al uso de la carpeta libs/, no se requiere instalar dependencias con pip.

#### 🐧 Requisitos (Linux)

Python 3.7+
Acceso a /dev/input/*

>[!WARNING]
>Si al ejecutar te da error por no tener permisos para leer dispositivos, utiliza este comando...

```bash
sudo chmod a+r /dev/input/event*
```

>[!NOTE]
>Cuando deje de procrastinar hare una version para Windows y pregare el link <a href="https://github.com/Cat-Not-Furry/Cat-Not-Furry">aqui</a>
#### ✔️ Características

- Soporta joystick y teclado (vía `evdev`)<br>
- Detecta 4 o 6 botones<br>
- Asignación personalizada para cada botón<br>
- Compatible con overlays encima de emuladores (como MAME)<br>
- Sin necesidad de instalación con pip (`libs/` incluida), solo descomprime las librerias.

#### Notas técnicas

Las teclas se guardan en bindings.json.<br>
Los botones del joystick se guardan en joystick_bindings.json.<br>
Los íconos de los botones se pueden cambiar libremente en icons/.<br>
Puedes expandir el sistema fácilmente para agregar más entradas o estilos visuales.

#### Uso

 ```bash
git clone https://github.com/tu_usuario/hud_overlay.git
cd hud_overlay
python3 main.py
```

### 👾 Créditos
Este proyecto fue desarrollado con amor al figthing 🕹️, mucha paciencia, y la ayuda de ChatGPT.
