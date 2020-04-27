def sort_list(file):
    def sort_by_len(inputStr):
        return len(inputStr)

    file.sort(key=sort_by_len, reverse=True)
    new_list = file
    print()

    new_list_app = []
    for word in new_list:
        if len(word) > 6:
            new_list_app.append(word)

    from collections import Counter

    counter = Counter(new_list_app)

    print(counter.most_common(10))
    print()

def read_from_json():
    import json

    with open(r'newsafr.json', encoding='utf-8') as f:
        json_data = json.load(f)

        description_list = []

        for i in json_data['rss']['channel']['items']:
            ad = i['description'].lower().split()
            description_list.extend(ad)
        
        sort_list(description_list)


def read_from_xml():
    import xml.etree.ElementTree as ET

    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(f'newsafr.xml', parser)
    root = tree.getroot()
    channel = root.find('channel')
    items = channel.findall('item')

    description_list = []

    for item in items:
        i = item.find('description').text
        ad = i.lower().split()
        description_list.extend(ad)

    sort_list(description_list)


read_from_json()

read_from_xml()