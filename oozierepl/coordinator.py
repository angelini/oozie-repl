import oozierepl.api as api


class Coordinator:

    @staticmethod
    def from_coordinator_id(coordinator_id):
        return Coordinator.from_coordinator_data(api.get_job_info(coordinator_id))

    @staticmethod
    def from_coordinator_data(data):
        job_strings = api.JOB_TYPE_STRINGS[api.ArtifactType.Coordinator]
        coordinator = Coordinator(
            id=data[job_strings.id],
            name=data['coordJobName'],
            user=data['user'],
            status=data['status'],
            start=data['startTime'],
            end=data['endTime'],
            nextMaterializedTime=data['nextMaterializedTime']
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

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
