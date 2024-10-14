# Software Requirements Specification (SRS)

**Project Name**: Backend de Roseta para Sistema de Monitoreo  
**Version**: 1.0  
**Date**: Octubre 10, 2024  


## 1. Introducción

### 1.1 Propósito
El propósito de este documento es especificar los requisitos funcionales y no funcionales para el desarrollo del backend de la roseta, diseñado para integrar dispositivos inteligentes que proporcionen control y monitoreo en cada habitación de un hogar. Este backend permitirá gestionar sensores y dispositivos de seguridad, conectados a través de una Raspberry Pi y desarrollado con Flask.

### 1.2 Alcance
Este sistema permitirá la monitorización y control de los siguientes dispositivos:
- **Punto de acceso WiFi** para comunicación entre dispositivos.
- **Sensor de humo** para detectar posibles incendios.
- **Sensor de humedad** para medir las condiciones ambientales.
- **Cámaras de vigilancia** o infrarrojas para monitoreo visual.
- **Bocina de alarma o timbre** para emitir alertas o replicar sonidos en toda la casa.
- **Sensor de movimiento** para detectar intrusiones o actividad en habitaciones.

### 1.3 Definiciones, acrónimos y abreviaciones
- **API**: Interfaz de Programación de Aplicaciones.
- **HTTP**: Protocolo de Transferencia de Hipertexto.
- **JSON**: Notación de Objetos de JavaScript, formato de intercambio de datos.
- **WiFi**: Tecnología inalámbrica para redes de área local.
- **UI**: Interfaz de Usuario.

### 1.4 Referencias
- Guías de Flask para el desarrollo de APIs.
- Documentación de la Raspberry Pi para la gestión de hardware y periféricos.

---

## 2. Descripción General del Sistema

### 2.1 Perspectiva del Producto
El sistema estará centrado en la Raspberry Pi, la cual servirá como el controlador principal de los dispositivos conectados a la red. El backend será responsable de recibir y procesar datos de los sensores, así como de enviar comandos a los dispositivos de salida (como las bocinas de alarma o el timbre).

### 2.2 Funciones del Producto
1. **Gestión de Puntos de Acceso WiFi**:
   - El sistema configurará y mantendrá el punto de acceso WiFi en cada roseta para asegurar la conectividad entre los dispositivos y el controlador central.

2. **Monitoreo del Sensor de Humo**:
   - El backend recibirá datos en tiempo real desde los sensores de humo y generará alertas si los niveles de humo superan un umbral predefinido.

3. **Monitoreo del Sensor de Humedad**:
   - Los sensores de humedad proporcionarán datos sobre la humedad en cada habitación, permitiendo ajustes o alarmas cuando los niveles estén fuera de un rango adecuado.

4. **Control y Visualización de Cámaras de Vigilancia**:
   - Las cámaras de vigilancia o infrarrojas enviarán imágenes o video en tiempo real al backend, que serán accesibles para los usuarios mediante la interfaz de usuario.

5. **Activación de Bocinas de Alarma o Timbre**:
   - El sistema podrá activar las bocinas de alarma o replicar el timbre de la casa en todas las habitaciones, en caso de detección de humo, intrusiones o alertas configuradas.

6. **Monitoreo del Sensor de Movimiento**:
   - Los sensores de movimiento enviarán datos de actividad que, en caso de detección de movimiento no autorizado, generarán una alerta y activarán la alarma.

### 2.3 Características de los Usuarios
El usuario principal del sistema será el administrador de la casa, que podrá interactuar con el sistema a través de una interfaz de usuario, accediendo a las funcionalidades descritas anteriormente.

---

## 3. Requisitos Específicos

### 3.1 Requisitos Funcionales

1. **RF-01**: El sistema debe permitir la configuración y gestión de puntos de acceso WiFi para cada roseta.
2. **RF-02**: El sistema debe recibir y procesar datos de los sensores de humo, generando alertas en caso de detección de humo.
3. **RF-03**: El sistema debe recibir y procesar datos de los sensores de humedad en cada habitación.
4. **RF-04**: El sistema debe permitir el acceso en tiempo real a las imágenes o videos capturados por las cámaras de vigilancia.
5. **RF-05**: El sistema debe ser capaz de activar bocinas de alarma o timbres en respuesta a eventos configurables (detención de humo, intrusión, etc.).
6. **RF-06**: El sistema debe recibir y procesar datos de los sensores de movimiento, activando alarmas si se detecta actividad no autorizada.

### 3.2 Requisitos No Funcionales

1. **RNF-01**: El sistema debe ser escalable para soportar múltiples rosetas en diferentes habitaciones.
2. **RNF-02**: El sistema debe garantizar la seguridad de los datos transmitidos entre los sensores y el backend mediante cifrado.
3. **RNF-03**: El sistema debe proporcionar respuestas rápidas con un tiempo de latencia inferior a 1 segundo para eventos críticos como detección de humo o intrusiones.
4. **RNF-04**: El sistema debe ser accesible desde dispositivos móviles y de escritorio mediante una interfaz web.
5. **RNF-05**: El sistema debe tener una alta disponibilidad del 99.9%, asegurando que los dispositivos estén siempre conectados y operativos.

---

## 4. Modelos de Caso de Uso

### 4.1 Caso de Uso 1: Monitorear los Sensores
**Descripción**: El sistema recibe datos de los sensores de humo, humedad y movimiento, y los muestra al usuario.

**Flujo de eventos**:
1. El usuario accede al panel de control del sistema.
2. El sistema muestra los valores actuales de los sensores.
3. Si se detecta una anomalía (humo, alta humedad, movimiento), el sistema genera una alerta.

### 4.2 Caso de Uso 2: Activar la Alarma
**Descripción**: El sistema activa las bocinas de alarma en respuesta a eventos configurables.

**Flujo de eventos**:
1. Se detecta un evento como humo o intrusión.
2. El backend procesa el evento y envía un comando para activar las bocinas de alarma o replicar el sonido del timbre en todas las habitaciones.

---

## 5. Consideraciones Técnicas

### 5.1 Plataforma
El sistema será desarrollado utilizando Flask como framework backend. La integración con la Raspberry Pi se realizará a través de bibliotecas de Python, permitiendo la interacción con los sensores y cámaras.

### 5.2 Base de Datos
El sistema utilizará PostgreSQL como base de datos para almacenar los eventos capturados por los sensores, el historial de alertas y la configuración de cada dispositivo.

### 5.3 Seguridad
El sistema debe utilizar SSL para cifrar las comunicaciones y OAuth2 para la autenticación y autorización de usuarios.

---

## 6. Glosario

- **Roseta**: Dispositivo central que controla y gestiona la conectividad de sensores y actuadores en cada habitación.
- **Backend**: Componente que realiza el procesamiento de datos y control de dispositivos.
