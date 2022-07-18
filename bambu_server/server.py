
from .routes import app
import argparse
import json

def main():
    argument_parser = argparse.ArgumentParser(description="bambu-server: model provisiong tool for Bambu")
    argument_parser.add_argument('-H', '--host', required=True, help="host address")
    argument_parser.add_argument('-p', '--port', required=True, help='host port')
    argument_parser.add_argument('-c', '--config', required=True, help='host port')
    arguments = argument_parser.parse_args()

    with open(arguments.config) as reader:
        app.config['BAMBU_CONFIG'] = json.loads(reader.read())

    app.run(host=arguments.host, port=arguments.port)

if __name__ == '__main__':
    main()