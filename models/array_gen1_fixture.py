from models.fixture import Fixture
from models.relay import Relay


class ArrayGen1Fixture(Fixture):
    def __init__(self):
        super().__init__()
        self.relay1 = Relay(id=1, name="seccion 1", label_energize="Encender", label_de_energize="Apagar", options=["Prendido", "Apagado"])
        self.relay2 = Relay(id=2, name="seccion 2", label_energize="Encender", label_de_energize="Apagar", options=["Prendido", "Apagado"])



if __name__ == "__main__":
    fixture = ArrayGen1Fixture()
    data = fixture.get_render_metadata()
    result = fixture.execute_action_component(2,"Relay", "Encender")
    print(result)
    print(data)
