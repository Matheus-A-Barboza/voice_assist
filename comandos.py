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
        
    elif "pesquisar por" in comando_falado:
        termo = comando_falado.replace("pesquisar por", "").strip()
        if termo:
            print(f"Pesquisando por '{termo}' no Google...")
            url_pesquisa = f"https://www.google.com/search?q={termo.replace(' ', '+')}"
            os.system(f'start {url_pesquisa}')
            
    elif "entretenimento" in comando_falado:
        print("Comando detectado: Abrindo Twitch...")
        url_twitch = "https://www.twitch.tv/"
        os.system(f'start {url_twitch}')
        
    elif "abrir steam" in comando_falado:
        print("Comando detectado: Abrindo Steam")
        os.system(r'start "" "E:\Steam\Steam.exe"')
        return False
    
    elif "até mais" in comando_falado:
        print("Encerrando Jarvis.")
        return True
    
    else:
        print(f"Comando {comando_falado} não mapeado.")
    return False