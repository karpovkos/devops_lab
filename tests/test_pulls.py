from unittest import TestCase
import handlers.pulls


base_json = [
    {
        'number': '10',
        'title': 'homework1',
        'state': 'open',
        'labels': [
            {'name': 'accepted'}
        ],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/10'
    },
    {
        'number': '23',
        'title': 'homework2',
        'state': 'open',
        'labels': [
            {'name': 'needs work'}
        ],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/23'
    },
    {
        'number': '38',
        'title': 'homework3',
        'state': 'open',
        'labels': [
            {'name': 'accepted'}
        ],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/38'
    },
    {
        'number': '55',
        'title': 'homework4',
        'state': 'open',
        'labels': [
            {'name': 'needs work'}
        ],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/55'
    },
    {
        'number': '66',
        'title': 'homework5',
        'state': 'open',
        'labels': [],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/66'
    },
    {
        'number': '30',
        'title': 'homework2',
        'state': 'closed',
        'labels': [],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/30'
    }
]


open_state = [
    {
        'num': '10',
        'title': 'homework1',
        'link': 'https://github.com/alenaPy/devops_lab/pull/10'
    },
    {
        'num': '23',
        'title': 'homework2',
        'link': 'https://github.com/alenaPy/devops_lab/pull/23'
    },
    {
        'num': '38',
        'title': 'homework3',
        'link': 'https://github.com/alenaPy/devops_lab/pull/38'
    },
    {
        'num': '55',
        'title': 'homework4',
        'link': 'https://github.com/alenaPy/devops_lab/pull/55'
    },
    {
        'num': '66',
        'title': 'homework5',
        'link': 'https://github.com/alenaPy/devops_lab/pull/66'
    }
]

closed_state = [
    {
        'num': '30',
        'title': 'homework2',
        'link': 'https://github.com/alenaPy/devops_lab/pull/30'
    }
]

accepted_state = [
    {
        'num': '10',
        'title': 'homework1',
        'link': 'https://github.com/alenaPy/devops_lab/pull/10'
    },
    {
        'num': '38',
        'title': 'homework3',
        'link': 'https://github.com/alenaPy/devops_lab/pull/38'
    }
]

needs_work_state = [
    {
        'num': '23',
        'title': 'homework2',
        'link': 'https://github.com/alenaPy/devops_lab/pull/23'
    },
    {
        'num': '55',
        'title': 'homework4',
        'link': 'https://github.com/alenaPy/devops_lab/pull/55'
    }
]


class TestPulls(TestCase):
    """Testing web server on python"""

    def test_state(self):
        """Testing states"""
        self.assertEqual(handlers.pulls.get_pulls("open", base_json), open_state)
        self.assertEqual(handlers.pulls.get_pulls("closed", base_json), closed_state)

    def test_labels(self):
        """Testing labels"""
        self.assertEqual(handlers.pulls.get_pulls("accepted", base_json), accepted_state)
        self.assertEqual(handlers.pulls.get_pulls("needs work", base_json), needs_work_state)
