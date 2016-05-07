import json
import pytest


@pytest.fixture
def oozie_host():
    return 'http://oozie-host'


@pytest.fixture
def history_server():
    return 'http://history-server'


@pytest.fixture
def workflow_body():
    with open('tests/data/workflow.json') as workflow_file:
        return json.loads(workflow_file.read())


@pytest.fixture
def workflow_id():
    return '0141964-160503113641936-oozie-oozi-W'
