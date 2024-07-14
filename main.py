import time

from webapp_gui import WebAppGUI
from threading import enumerate, main_thread

if __name__ == "__main__":
    test_suite = "some test suite"
    gui = WebAppGUI(test_suite)
    try:
        gui.start()
        for i in range(20):
            print(f"in process num : {i}")
            time.sleep(0.7)
        for i in range(20):
            print(f"in process num : {i}")
    except KeyboardInterrupt:
        print("bye ;)")
    except Exception as e:
        print(e)
    finally:
        list_threads = enumerate()
        print("Hilos después de detener la aplicación:", list_threads)
        gui.stop()
        for thread in list_threads:
            if thread != main_thread():
                print(f"Intentando detener el hilo: {thread.name}")
                thread.join(timeout=1)
                if thread.is_alive():
                    print(f"No se pudo detener el hilo: {thread.name}")
    list_threads = enumerate()
    print("Hilos al final del programa:", list_threads)

