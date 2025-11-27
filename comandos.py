import os
import requests

def processar_comando(comando_falado):
    """
    Executa a tarefa baseada no comando reconhecido.
    Retorna True se o assistente deve ser encerrado
    """
    if "desligar" in comando_falado:
        print("Comando detectado: Desligando computador...")
        os.system('shutdown /s /t 30 /f')
        return False
    elif "abrir navegador" in comando_falado:
        print("Comando detectado: Abrindo Navegador...")
        os.system('start msedge')
    elif "até mais" in comando_falado:
        print("Encerrando Jarvis.")
        return True
    else:
        print(f"Comando {comando_falado} não mapeado.")
    return False