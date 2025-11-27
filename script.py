import speech_recognition as sr
import pvporcupine as pv
from dotenv import load_dotenv
import pyaudio
import os
import struct
import time
import pyttsx3
from comandos import processar_comando

load_dotenv()
HOTWORD = "jarvis"

ACESS_KEY = os.getenv("PICOVOICE_ACCESS_KEY")

if ACESS_KEY is None:
    print("ERRO: A chave de acesso não foi carregada.")
    exit()
    
try:
    engine = pyttsx3.init()
except Exception as e:
    print(f"Nao foi possivel iniciar Voz: {e}")
    
def falar(texto):
    """Faz o assistente falar o texto fornecido."""
    global engine
    if engine:
        engine.say(texto)
        engine.runAndWait()

def ouvir():
    """Ouve o microfone APENAS após o hotword ser detectado."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pronto para ouvir o comando (5 segundos)...")
        r.adjust_for_ambient_noise(source, duration = 0.5)
        
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            comando = r.recognize_google(audio, language='pt-BR')
            print(f"Comando: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi o comando.")
        except sr.UnknownValueError:
            print("Tempo limite excedido.")
        except sr.UnknownValueError:
            print("Este comando não existe.")
        except sr.UnknownValueError:
            print("Erro de Conexão. Verifique sua internet.")
    return ""

def iniciar_jarvis():
    
    porcupine = None
    pa = None
    audio_stream = None
    
    try:
        porcupine = pv.create(
            access_key=ACESS_KEY,
            keywords=[HOTWORD],
            sensitivities=[0.7]
        )
    except Exception as e:
        print(f"Erro ao inicializar Porcupine. Erro: {e}")
        return
    
    pa=pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
    
    print(f"-------------------------------------------------------")
    print(f"⭐ Assistente rodando. Escutando o hotword: '{HOTWORD}' ⭐")
    print(f"Para encerrar diga: '{HOTWORD} fechar assistente'")
    print(f"-------------------------------------------------------")
    
    falar("Bem Vindo, Jarvis Iniciado!")
    
    terminar_loop = False
    
    while not terminar_loop:
        try:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            result = porcupine.process(pcm)
            
            if result >= 0:
                print("\n🚨 GATILHO DETECTADO 🚨")
                
                # falar("Estou pronto!")
                
                time.sleep(0.5)
                comando = ouvir()
                if comando:
                    terminar_loop = processar_comando(comando)
                print("Escutando")
        except KeyboardInterrupt:
            terminar_loop = True
        except Exception as e:
            print(f"Erro inesperado no loop: {e}")
            time.sleep(1)
   
    falar("Até Mais, se precisar novamente basta me chamar.")
    
    print("Encerrando Jarvis...")
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if pa is not None:
        pa.terminate()
        
    global engine
    if engine:
        engine.stop()
if __name__ == "__main__":
    iniciar_jarvis()