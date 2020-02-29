from cx_Freeze import setup, Executable

setup(name="JoKenPô", version="0.1", description="Jogo de Jokenpô", executables=[Executable("ex045.py")],
      requires=['emoji'])
