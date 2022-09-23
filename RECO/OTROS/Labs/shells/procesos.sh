select $lista in listarProcesos buscarProceso matarProceso reiniciarProceso salir
do 
	case $lista in
		listarProcesos)
			top
			;;
		buscarProceso)
			read -p "digite algo relacionado al proceso (ID, user, nombre etc)" ER
			top | grep -i $ER
			;;
		reiniciarProceso)
			read -p "digite el ID del proceso" ID 
			killall -HUP $ID 
			;;
		salir)
			break
			;;
	esac
done
			