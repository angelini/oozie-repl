import os
import requests
import urllib

OOZIE_HOST = os.environ['OOZIE_HOST']
HISTORY_SERVER = os.environ['HISTORY_SERVER']


def _get_workflows(filters, offset, length):
    filters = [urllib.parse.urlencode({k: v})
               for (k, v) in filters.items()
               if v]

    response = requests.get(OOZIE_HOST + '/oozie/v1/jobs', params={
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
    response = requests.get(OOZIE_HOST + '/oozie/v1/job/{}'.format(workflow_id), params={
        'show': 'graph'
    })

    response.raise_for_status
    return response.content


def get_logs_link(application_uri, yarn_job_id, status):
    if status == 'RUNNING':
        uri = application_uri + 'ws/v1/mapreduce/jobs/{}/jobattempts'.format(yarn_job_id)
    else:
        uri = HISTORY_SERVER + '/ws/v1/history/mapreduce/jobs/{}/jobattempts'.format(yarn_job_id)

    response = requests.get(uri)
    response.raise_for_status()

    attempts = response.json()['jobAttempts']['jobAttempt']
    if len(attempts) == 0:
        raise Exception('No attempts found for: {}'.format(yarn_job_id))

    return attempts[0]['logsLink'] + '/stdout/?start=0'


def get_workflow_info(workflow_id):
    response = requests.get(OOZIE_HOST + '/oozie/v1/job/{}'.format(workflow_id), params={
        'timezone': 'EST',
        'show': 'info'
    })

    response.raise_for_status
    return response.json()
