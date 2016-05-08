import json
import pytest


@pytest.fixture
def oozie_host():
    return 'http://oozie-host'


@pytest.fixture
def history_server():
    return 'http://history-server'


@pytest.fixture
def workflows_body():
    with open('tests/data/workflows.json') as fixture:
        return json.loads(fixture.read())


@pytest.fixture
def coordinators_body():
    with open('tests/data/coordinators.json') as fixture:
        return json.loads(fixture.read())


@pytest.fixture
def workflow_body():
    with open('tests/data/workflow.json') as fixture:
        return json.loads(fixture.read())


@pytest.fixture
def coordinator_body():
    with open('tests/data/coordinator.json') as fixture:
        return json.loads(fixture.read())


@pytest.fixture
def workflow_id():
    return '0141964-160503113641936-oozie-oozi-W'


@pytest.fixture
def coordinator_id():
    return '0137532-160413133521481-oozie-oozi-C'


@pytest.fixture
def flow_name():
    return 'reportify-rdb-landing-pages-daily-rollup'
