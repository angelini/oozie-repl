import oozierepl.api as api


class Job:

    @staticmethod
    def from_action(action):
        return Job(
            id=action['id'],
            yarn_id=action['externalId'],
            name=action['name'],
            status=action['status'],
            start=action['startTime'],
            end=action['endTime'],
            application_uri=action['consoleUrl'],
        )

    def __init__(self, id, yarn_id, name, status, start, end, application_uri):
        self.id = id
        self.yarn_id = yarn_id
        self.name = name
        self.status = status
        self.start = start
        self.end = end
        self.application_uri = application_uri
        self._logs_link = None

    @property
    def logs_link(self):
        if not self._logs_link:
            self._logs_link = api.get_logs_link(self.application_uri, self.yarn_id, self.status)
        return self._logs_link

    def __repr__(self):
        return 'Job {name} ({status})'.format(
            name=self.name,
            status=self.status
        )


class Workflow:

    @staticmethod
    def from_workflow_id(workflow_id):
        return Workflow.from_workflow_data(api.get_job_info(workflow_id))

    @staticmethod
    def from_workflow_data(data):
        job_strings = api.JOB_TYPE_STRINGS[api.ArtifactType.Workflow]
        flow = Workflow(
            id=data[job_strings.id],
            name=data['appName'],
            user=data['user'],
            status=data['status'],
            start=data['startTime'],
            end=data['endTime']
        )

        for action in data['actions']:
            name = action['name']

            if action['type'] == 'sub-workflow':
                flow.jobs[name] = Workflow.from_workflow_id(action['externalId'])

            if action['type'] == 'shell':
                if name.startswith('notify-joining-') or \
                   (name.startswith('notify') and action['transition'] == 'kill'):
                    # Skip status=ignore nodes
                    continue

                flow.jobs[name] = Job.from_action(action)

        return flow

    def __init__(self, id, name, user, status, start, end):
        self.id = id
        self.name = name
        self.user = user
        self.status = status
        self.start = start
        self.end = end
        self.jobs = {}

    def __repr__(self):
        return 'Workflow {name} ({status})'.format(
            name=self.name,
            status=self.status
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
