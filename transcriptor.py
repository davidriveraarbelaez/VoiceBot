import numpy as np
import sounddevice as sd
import speech_recognition as sr
import scipy.io.wavfile as wavfile

# Parámetros
duration = 5
fs = 44100

# Grabar audio
def grabar_audio(duration,fs):
    # Abrir el mic, escuchar nuestra voz y reproducir el audio
    # Voz a texto
    print("Habla ahora, por favor")
    # Grabar el audio
    audio = sd.rec(int(duration*fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait() # Esperamos que termine la grabación
    print ("Gracias por grabar el audio, ahora vamos a reproducirlo")
    return audio

def reproducir_audio(audio,fs):
    sd.play(audio,fs)
    sd.wait()

def guardar_audio(audio, fs, filename):
    # Guardar el audio grabado en un archivo WAV
    wavfile.write("audio_grabado.wav", fs, audio)

def reconocer_voz(filename):
    # Crear una instancia para reconocer la voz
    recognizer = sr.Recognizer()
    # Utilizar el archivo WAV para reconocimiento de voz
    with sr.AudioFile("audio_grabado.wav") as source:
        audio_data = recognizer.record(source)
        try:
            texto = recognizer.recognize_google(audio_data, language="es-ES")
            print("Texto reconocido: " + texto)
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print("Error al solicitar resultados del servicio de reconocimiento de voz")

def main():
    audio = grabar_audio(duration, fs)
    reproducir_audio(audio,fs)
    guardar_audio(audio,fs,"audio_grabado.wav")
    reconocer_voz("audio_grabado.wav")

if __name__ == "__main__":
    main()