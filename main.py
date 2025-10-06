from db import Conexion as cn
from View.dashboard import run_dashboard


def main():
    try:
        cn.Conexion()
    except Exception as e:
        print(f"Advertencia: no se pudo inicializar la conexión a BD: {e}")

    run_dashboard()


if __name__ == "__main__":
    main()
