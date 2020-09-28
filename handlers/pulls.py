#! /usr/bin/env python
import requests


class GetJson:
    def __init__(self, json_arr, params, url):
        if params:
            self.params = params
        else:
            self.params = {'per_page': 100, 'state': "all"}

        if url:
            self.url = url
        else:
            self.url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'

        if json_arr:
            self.json_data = json_arr
        else:
            self.json_data = self.get_json()

    def get_json(self):
        return requests.get(self.url, params=self.params).json()

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


def get_pulls(state, json_arr=None, params=None, url=None):
    obj_json = GetJson(json_arr, params, url)
    if state:
        return obj_json.parse_json(state)
