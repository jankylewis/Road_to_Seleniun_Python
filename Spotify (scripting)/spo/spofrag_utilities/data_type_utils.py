import json


class DataTypeHandler:

    # bool section goes here
    @staticmethod
    def cast_to_bool(casted_data) -> bool:
        return json.loads(casted_data.lower())
