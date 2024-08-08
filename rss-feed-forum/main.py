import xml.etree.ElementTree as ET

import requests


def main():
    response = requests.get('https://forum.jugger.org/app.php/feed')
    forum_xml = response.text

    tree = ET.fromstring(forum_xml)

    entries = []

    for entry in tree.findall('{http://www.w3.org/2005/Atom}entry'):
        print(entry.tag, entry.text, entry.attrib)
        published = entry.find('{http://www.w3.org/2005/Atom}published')
        print(published)


if __name__ == '__main__':
    main()
