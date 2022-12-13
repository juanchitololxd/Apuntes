# Capa transporte


Conexion extremo a extremo

## NOAC
    - Cada segmento debe ir a su destino sin importar el estado del destino


## OAC
    - Espera a que el destino le conteste par enviar la información
    - La capa se encarga del cierre de la conexion y maneja duplicados (en el extremo a extremo)

 Direccionamiento (pone direcciones)

 Encapsulamiento

 Sus direcciones son los puertos

 ## Protocolos

 TCP 

 los primeros 1024 son well known ports

 **Multiplexacion:** Permite que en un dispositivo se tengan varias cosas abiertas, porque cada tarea va para puertos diferentes
### UDP

User datagram protocol
Servicio NOAC

Usarlo si:

    - La aplicacion de usuario directamente controla errores
    - Aplicaciones que transmiten pocos datos

 SCTP



============ TEST===========

|    A | B    | C    |
| ---: | ---- | ---- |
|    S | SDFA | FSA  |
|   FD |      |      |
|      | D    |      |

Expectativa:

![image-20221213152943174](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\image-20221213152943174.png)

