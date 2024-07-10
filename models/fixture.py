from models.fixture_component import FixtureComponent
import json


class Fixture:
    def __init__(self):
        self.components = list()

    def get_render_metadata(self):
        json_components = {'components': []}
        for item in self.__dict__.values():
            if isinstance(item, FixtureComponent):
                self.components.append(item)
                json_components['components'].append(
                    {
                        'id': item.id,
                        'name': item.name,
                        'type': item.type,
                        'actions': [action.get_render_metadata() for action in item.actions],
                        'status': [status.get_render_metadata() for status in item.statuses],
                        'logs': item.logs
                    }
                )
        return json.dumps(json_components)

    def execute_action_component(self, id: int, type: str, name_action: str):
        for item in self.__dict__.values():
            if isinstance(item, FixtureComponent):
                for action in item.actions:
                    if action.name == name_action and item.id == id and item.type == type:
                        return action.run()
        return False

