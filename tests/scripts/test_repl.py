import responses
from oozierepl.workflow import Workflow as WorkflowObject
from oozierepl.coordinator import Coordinator as CoordinatorObject
from oozierepl.scripts.repl import by_name, Coordinator, Workflow


@responses.activate
def test_by_name_workflow(flow_name, workflows_body, oozie_host, monkeypatch):
    monkeypatch.setenv('OOZIE_HOST', oozie_host)

    responses.add(
        responses.GET,
        'http://oozie-host/oozie/v2/jobs',
        json=workflows_body,
        status=200,
    )
    assert by_name(flow_name, form=Workflow) == [
        WorkflowObject(
            '0145308-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'RUNNING',
            'Sat, 07 May 2016 11:29:08 EST',
            None
        ),
        WorkflowObject(
            '0145241-160503113641960-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 10:05:32 EST',
            'Sat, 07 May 2016 11:29:08 EST'
        ),
        WorkflowObject(
            '0145122-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 08:29:06 EST',
            'Sat, 07 May 2016 10:05:32 EST'
        ),
        WorkflowObject(
            '0144994-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 06:55:33 EST',
            'Sat, 07 May 2016 08:29:06 EST'
        ),
        WorkflowObject(
            '0144892-160503113641936-oozie-oozi-W',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'SUCCEEDED',
            'Sat, 07 May 2016 04:54:14 EST',
            'Sat, 07 May 2016 06:55:33 EST'
        ),
    ]

@responses.activate
def test_by_name_coordinator(flow_name, coordinators_body, oozie_host, monkeypatch):
    monkeypatch.setenv('OOZIE_HOST', oozie_host)

    responses.add(
        responses.GET,
        'http://oozie-host/oozie/v2/jobs',
        json=coordinators_body,
        status=200,
    )
    actual = by_name(flow_name, form=Coordinator)
    assert actual == [
        CoordinatorObject(
            '0140935-160503113641936-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'RUNNING',
            'Wed, 04 May 2016 14:37:00 EST',
            'Mon, 04 May 2116 14:34:00 EST',
            'Sat, 07 May 2016 12:37:00 EST'
        ),
        CoordinatorObject(
            '0137532-160413133521481-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Mon, 02 May 2016 15:37:00 EST',
            'Sat, 02 May 2116 09:49:00 EST',
            'Wed, 04 May 2016 15:37:00 EST'
        ),
        CoordinatorObject(
            '0132000-160413133521481-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Thu, 28 Apr 2016 08:37:00 EST',
            'Tue, 28 Apr 2116 08:33:00 EST',
            'Mon, 02 May 2016 10:37:00 EST'
        ),
        CoordinatorObject(
            '0131036-160413133456556-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Wed, 27 Apr 2016 15:37:00 EST',
            'Mon, 27 Apr 2116 15:54:00 EST',
            'Thu, 28 Apr 2016 15:37:00 EST'
        ),
        CoordinatorObject(
            '0120789-160413133521481-oozie-oozi-C',
            'reportify-rdb-landing-pages-daily-rollup',
            'oozie',
            'KILLED',
            'Thu, 21 Apr 2016 12:37:00 EST',
            'Tue, 21 Apr 2116 11:45:00 EST',
            'Wed, 27 Apr 2016 16:37:00 EST'
        ),
    ]
