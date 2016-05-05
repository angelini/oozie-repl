import os
import requests
import urllib
from enum import Enum

OOZIE_HOST = os.environ['OOZIE_HOST']
HISTORY_SERVER = os.environ['HISTORY_SERVER']


class ArtifactType(Enum):
    Workflow = 1
    WorkflowAction = 2
    Coordinator = 3
    CoordinatorAction = 4

JOB_TYPE_STRINGS = {
    ArtifactType.Workflow: ('wf', 'workflows', 'id'),
    ArtifactType.Coordinator: ('coordinator', 'coordinatorjobs', 'coordJobId'),
}

def _get_jobs(form, filters, offset, length):
    filters = [urllib.parse.urlencode({k: v})
               for (k, v) in filters.items()
               if v]

    job_type, result_type, _ = JOB_TYPE_STRINGS[form]
    response = requests.get(OOZIE_HOST + '/oozie/v2/jobs', params={
        'timezone': 'EST',
        'offset': offset,
        'len': length,
        'filter': ';'.join(filters),
        'jobtype': job_type
    })

    response.raise_for_status()
    return response.json()[result_type]


def get_jobs(form, filters, offset=1, length=50):
    while True:
        jobs = _get_jobs(form, filters, offset, length)

        for job in jobs:
            yield job

        offset += length

        if len(jobs) < length:
            return


def get_workflows(filters, offset=1, length=50):
    return get_jobs(ArtifactType.Workflow, filters, offset, length)


def get_coordinators(filters, offset=1, length=50):
    return get_jobs(ArtifactType.Coordinator, filters, offset, length)


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


def get_job_info(job_id):
    response = requests.get(OOZIE_HOST + '/oozie/v2/job/{}'.format(job_id), params={
        'timezone': 'EST',
        'show': 'info'
    })

    response.raise_for_status
    return response.json()
