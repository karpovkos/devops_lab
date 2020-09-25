#! /usr/bin/env python
import requests


class GetJson:
    def __init__(self):
        self.json_data = self.get_json({'per_page': 100, 'state': "all"})

    @staticmethod
    def get_json(params):
        return requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                            params=params).json()

    def parse_json(self, state):
        new_arr = []
        for element in self.json_data:
            a = element["number"]
            b = element["title"]
            c = element["html_url"]

            if element["state"] == state:
                new_arr.append({"num": a, "title": b, "link": c})
            elif element["labels"] and element["labels"][0]["name"] == state:
                new_arr.append({"num": a, "title": b, "link": c})
        return new_arr


def get_pulls(state):
    obj_json = GetJson()
    if state:
        return obj_json.parse_json(state)
