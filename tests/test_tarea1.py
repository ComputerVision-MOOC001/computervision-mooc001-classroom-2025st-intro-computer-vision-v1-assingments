import os
from solutions.tarea1_solucion import detect_edges

def test_detect_edges():
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_image = os.path.join(base_path, "../tasks/tarea1/input_data/lena.png")
    output_image = os.path.join(base_path, "../tasks/tarea1/output_data/lena_output.png")
    detect_edges(input_image, output_image)

    assert os.path.exists(output_image), "La imagen de salida no se generó."
