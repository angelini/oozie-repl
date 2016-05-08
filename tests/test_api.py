import responses
from oozierepl.api import get_job_info


@responses.activate
def test_get_job_info_workflow(workflow_id, workflow_body, oozie_host, monkeypatch):
    monkeypatch.setenv('OOZIE_HOST', oozie_host)

    responses.add(
        responses.GET,
        'http://oozie-host/oozie/v2/job/' + workflow_id,
        json=workflow_body,
        status=200,
    )

    data = get_job_info(workflow_id)
    assert data == workflow_body


@responses.activate
def test_get_job_info_coordinator(coordinator_id, coordinator_body, oozie_host, monkeypatch):
    monkeypatch.setenv('OOZIE_HOST', oozie_host)

    responses.add(
        responses.GET,
        'http://oozie-host/oozie/v2/job/' + coordinator_id,
        json=coordinator_body,
        status=200,
    )

    data = get_job_info(coordinator_id)
    assert data == coordinator_body
