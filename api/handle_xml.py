# Description: This file is responsible for sending data to Parser microservice.

import dicttoxml

url = 'http://localhost:8200/mews/send'


def mews(mews_object: dict) -> None:
    print('generating xml ', mews_object)
    xml_data = dicttoxml.dicttoxml(mews_object)
    xml_string = xml_data.decode()

    # Define the file path and name for the XML file
    xml_file_path = f'{mews_object["Id"]}.xml'

    # Write the XML data to the file
    with open(xml_file_path, "w") as xml_file:
        xml_file.write(xml_string)

    print(f"XML data saved to {xml_file_path}")
