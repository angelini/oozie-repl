import responses
from oozierepl.api import get_job_info


@responses.activate
def test_get_job_info(workflow_id, workflow_body, oozie_host, monkeypatch):
    monkeypatch.setenv('OOZIE_HOST', oozie_host)

    responses.add(
        responses.GET,
        'http://oozie-host/oozie/v2/job/0141964-160503113641936-oozie-oozi-W',
        json=workflow_body,
        status=200,
    )

    data = get_job_info(workflow_id)
    assert data == workflow_body
