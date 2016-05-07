import api

class Coordinator:

    @staticmethod
    def from_coordinator_id(coordinator_id):
        info = api.get_job_info(coordinator_id)
        coordinator = Coordinator(
            id=coordinator_id,
            name=info['coordJobName'],
            user=info['user'],
            status=info['status'],
            start=info['startTime'],
            end=info['endTime'],
            nextMaterializedTime=info['nextMaterializedTime']
        )
        return coordinator

    def __init__(self, id, name, user, status, start, end, nextMaterializedTime):
        self.id = id
        self.name = name
        self.user = user
        self.status = status
        self.start = start
        self.end = end
        self.nextMaterializedTime = nextMaterializedTime

    def __repr__(self):
        return 'Coordinator {name} ({status})'.format(
            name=self.name,
            status=self.status
        )
