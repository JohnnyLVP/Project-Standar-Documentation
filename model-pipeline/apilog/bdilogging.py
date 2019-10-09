import uuid
from datetime import datetime
import requests
import json
import socket


class LoggingBDI:

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.id = str(uuid.uuid4())
        self.time_format = '%Y-%m-%dT%H:%M:%SZ'
        with open('utils/countries_equivalences.json') as json_file:
            self.countries_equivalences = json.load(json_file)

    def create_session(self, app, service, country, type_execution):
        endpoint = self.endpoint + '/' + self.id

        timestamp = datetime.utcnow().strftime(self.time_format)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        user_execution = s.getsockname()[0]
        s.close()

        headers = {'Content-type': 'application/json'}

        data = {
            "app": app,
            "servicio": service,
            "codigoPais": self.countries_equivalences[country],
            "estadoEjecucion": "Pendiente",
            "tipoEjecucion": type_execution,
            "usuarioEjecucion": user_execution,
            "fechaInicio": timestamp,
            "input": {"TiempoEspera": "2000"},
            "output": {}
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def update_session(self):
        endpoint = self.endpoint + '/' + self.id

        headers = {'Content-type': 'application/json'}

        data = {
            "estadoEjecucion": "Iniciada"
        }

        response = requests.put(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def done_session(self):
        endpoint = self.endpoint + '/done/' + self.id

        timestamp = datetime.utcnow().strftime(self.time_format)

        headers = {'Content-type': 'application/json'}

        data = {
            "fechaFin": timestamp
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def failed_session(self, message):
        endpoint = self.endpoint + '/error/' + self.id

        timestamp = datetime.utcnow().strftime(self.time_format)

        headers = {'Content-type': 'application/json'}

        data = {
            "fechaFin": timestamp,
            "mensaje": message
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response

    def add_event(self, type_event, event, initial_datetime, final_datetime, message):
        endpoint = self.endpoint + '/add/' + self.id

        headers = {'Content-type': 'application/json'}

        data = {
            "fechaEjecucion": initial_datetime.strftime(self.time_format),
            "fechaInicio": final_datetime.strftime(self.time_format),
            "tipoEvento": type_event,
            "evento": event,
            "duracion": str((final_datetime - initial_datetime).microseconds / 1000),
            "mensaje": message
        }

        response = requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)

        return response


if __name__ == "__main__":
    ip = ''
    port = '8090'
    endpoint = 'http://' + ip + ':' + port

    logging = LoggingBDI(endpoint)

    app = ""
    service = "DataPreparation"
    country = "PER"
    type_execution = "Manual"

    response = logging.create_session(app, service, country, type_execution)
    print(response.text)
    print(response.headers)
