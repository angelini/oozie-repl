#!/usr/bin/env python

import api
import IPython
import itertools
import os
import subprocess
import tempfile

from flow import Flow
from stdout import p, pp  # NOQA

_tempfiles = []


def take(generator, n=5):
    return tuple(itertools.islice(generator, n))


def _get_flows(user, status, n):
    workflows = take(api.get_workflows({'user': user, 'status': status}), n)
    return [Flow.from_workflow_id(w['id']) for w in workflows]


def failed(user='oozie', n=5):
    return _get_flows(user, 'FAILED', n)


def running(user='oozie', n=5):
    return _get_flows(user, 'RUNNING', n)


def all(user='oozie', n=5):
    return _get_flows(user, None, n)


def open_graph(workflow):
    temp_fd, path = tempfile.mkstemp()
    with os.fdopen(temp_fd, mode='bw') as temp_file:
        temp_file.write(api.get_graph_png(workflow))

    _tempfiles.append(path)
    subprocess.check_output(['open', path])


try:
    IPython.start_ipython(user_ns=globals())
finally:
    for path in _tempfiles:
        os.remove(path)
