import IPython
import itertools
import os
import subprocess
import tempfile

import oozierepl.api as api
from oozierepl.workflow import Workflow as WorkflowObject
from oozierepl.coordinator import Coordinator as CoordinatorObject
from oozierepl.stdout import p, pp  # NOQA

_tempfiles = []

Coordinator = api.ArtifactType.Coordinator
Workflow = api.ArtifactType.Workflow


def take(generator, n=5):
    return tuple(itertools.islice(generator, n))


def _get_jobs(form=Workflow, user=None, status=None, name=None, n=5):
    jobs = take(api.get_jobs(form=form, filters={'user': user, 'status': status, 'name': name}), n=n)
    if form == Workflow:
        return [WorkflowObject.from_workflow_data(job) for job in jobs]
    elif form == Coordinator:
        return [CoordinatorObject.from_coordinator_data(job) for job in jobs]
    else:
        raise ValueError('Unrecognized form %s' % form)


def failed(form=Workflow, user='oozie', n=5):
    return _get_jobs(form=form, user=user, status='FAILED', n=n)


def running(form=Workflow, user='oozie', n=5):
    return _get_jobs(form=form, user=user, status='RUNNING', n=n)


def all(form=Workflow, user='oozie', n=5):
    return _get_jobs(form=form, user=user, n=n)


def by_name(name, form=Workflow, user=None, status=None, n=5):
    return _get_jobs(form=form, user=user, status=status, name=name, n=n)


def open_graph(flow):
    temp_fd, path = tempfile.mkstemp()
    with os.fdopen(temp_fd, mode='bw') as temp_file:
        temp_file.write(api.get_graph_png(flow.id))

    _tempfiles.append(path)
    subprocess.check_output(['open', path])


def repl():
    try:
        IPython.start_ipython(user_ns=globals())
    finally:
        for path in _tempfiles:
            os.remove(path)
