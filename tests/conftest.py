import json
import pytest

from oozierepl.workflow import Workflow
from oozierepl.coordinator import Coordinator


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
def workflows():
    return [
        Workflow(
            '0145308-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'RUNNING',
            'Sat, 07 May 2016 11:29:08 EST',
            None
        ),
        Workflow(
            '0145241-160503113641960-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 10:05:32 EST',
            'Sat, 07 May 2016 11:29:08 EST'
        ),
        Workflow(
            '0145122-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 08:29:06 EST',
            'Sat, 07 May 2016 10:05:32 EST'
        ),
        Workflow(
            '0144994-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 06:55:33 EST',
            'Sat, 07 May 2016 08:29:06 EST'
        ),
        Workflow(
            '0144892-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 04:54:14 EST',
            'Sat, 07 May 2016 06:55:33 EST'
        ),
    ]


@pytest.fixture
def coordinators_body():
    with open('tests/data/coordinators.json') as fixture:
        return json.loads(fixture.read())


@pytest.fixture
def coordinators():
    return [
        Coordinator(
            '0140935-160503113641936-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'RUNNING',
            'Wed, 04 May 2016 14:37:00 EST',
            'Mon, 04 May 2116 14:34:00 EST',
            'Sat, 07 May 2016 12:37:00 EST'
        ),
        Coordinator(
            '0137532-160413133521481-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Mon, 02 May 2016 15:37:00 EST',
            'Sat, 02 May 2116 09:49:00 EST',
            'Wed, 04 May 2016 15:37:00 EST'
        ),
        Coordinator(
            '0132000-160413133521481-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Thu, 28 Apr 2016 08:37:00 EST',
            'Tue, 28 Apr 2116 08:33:00 EST',
            'Mon, 02 May 2016 10:37:00 EST'
        ),
        Coordinator(
            '0131036-160413133456556-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Wed, 27 Apr 2016 15:37:00 EST',
            'Mon, 27 Apr 2116 15:54:00 EST',
            'Thu, 28 Apr 2016 15:37:00 EST'
        ),
        Coordinator(
            '0120789-160413133521481-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Thu, 21 Apr 2016 12:37:00 EST',
            'Tue, 21 Apr 2116 11:45:00 EST',
            'Wed, 27 Apr 2016 16:37:00 EST'
        ),
    ]


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
