import responses
from oozierepl.workflow import Workflow as WorkflowObject
from oozierepl.coordinator import Coordinator as CoordinatorObject
from oozierepl.scripts.repl import by_name, Coordinator, Workflow


@responses.activate
def test_by_name_workflow(flow_name, workflows_body, workflows, oozie_host, monkeypatch):
    monkeypatch.setenv('OOZIE_HOST', oozie_host)
    responses.add(
        responses.GET,
        'http://oozie-host/oozie/v2/jobs?len=50&filter=name%3Dreportify-rdb-landing-pages-daily-rollup&jobtype=wf&timezone=EST&offset=1',
        json=workflows_body,
        status=200,
        match_querystring=True,
    )
    assert by_name(flow_name, form=Workflow) == workflows


@responses.activate
def test_by_name_coordinator(flow_name, coordinators_body, coordinators, oozie_host, monkeypatch):
    monkeypatch.setenv('OOZIE_HOST', oozie_host)
    responses.add(
        responses.GET,
        'http://oozie-host/oozie/v2/jobs?timezone=EST&offset=1&jobtype=coordinator&len=50&filter=name%3Dreportify-rdb-landing-pages-daily-rollup',
        json=coordinators_body,
        status=200,
        match_querystring=True,
    )
    assert by_name(flow_name, form=Coordinator) == coordinators
