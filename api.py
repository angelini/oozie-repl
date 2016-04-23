import os
import requests
import urllib

HOST = os.environ['OOZIE_HOST']


def _get_workflows(filters, offset, length):
    filters = [urllib.parse.urlencode({k: v})
               for (k, v) in filters.items()
               if v]

    response = requests.get(HOST + '/oozie/v1/jobs', params={
        'timezone': 'EST',
        'offset': offset,
        'len': length,
        'filter': ';'.join(filters)
    })

    response.raise_for_status()
    return response.json()['workflows']


def get_workflows(filters, offset=1, length=50):
    while True:
        workflows = _get_workflows(filters, offset, length)

        for workflow in workflows:
            yield workflow

        offset += length

        if len(workflows) < length:
            return


def get_graph_png(workflow_id):
    response = requests.get(HOST + '/oozie/v1/job/{}'.format(workflow_id), params={
        'show': 'graph'
    })

    response.raise_for_status
    return response.content


def get_workflow_info(workflow_id):
    response = requests.get(HOST + '/oozie/v1/job/{}'.format(workflow_id), params={
        'timezone': 'EST',
        'show': 'info'
    })

    response.raise_for_status
    return response.json()


def get_full_tree(workflow_id):
    workflow = get_workflow_info(workflow_id)
    tree = {}

    for action in workflow['actions']:
        if action['type'] == 'sub-workflow':
            tree[action['name']] = {
                'status': action['status'],
                'start': action['startTime'],
                'end': action['endTime'],
                'children': get_full_tree(action['externalId'])
            }

        if action['type'] == 'shell':
            tree[action['name']] = {
                'status': action['status'],
                'start': action['startTime'],
                'end': action['endTime']
            }

    return tree
