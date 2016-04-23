import api


class Job:

    @staticmethod
    def from_action(action):
        return Job(
            id=action['id'],
            name=action['name'],
            status=action['status'],
            start=action['startTime'],
            end=action['endTime']
        )

    def __init__(self, id, name, status, start, end):
        self.id = id
        self.name = name
        self.status = status
        self.start = start
        self.end = end


class Flow:

    @staticmethod
    def from_workflow_id(workflow_id):
        info = api.get_workflow_info(workflow_id)
        flow = Flow(
            id=info['id'],
            name=info['appName'],
            user=info['user'],
            status=info['status'],
            start=info['startTime'],
            end=info['endTime']
        )

        for action in info['actions']:
            name = action['name']

            if action['type'] == 'sub-workflow':
                flow.jobs[name] = Flow.from_workflow_id(action['externalId'])

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
