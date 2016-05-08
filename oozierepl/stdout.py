import re

from colorama import Fore as F, Style as S
from oozierepl.workflow import Workflow, Job


def time_from_datestring(date_str):
    if not date_str:
        return F.YELLOW + '--:--:--' + S.RESET_ALL

    match = re.match(r'.*(?P<time>\d{2}:\d{2}:\d{2}).*', date_str)
    return match.group('time')


def sort_jobs_by_start(flow):
    if not flow:
        return []
    return sorted(flow.jobs.items(), key=lambda i: i[1].start)


def color_status(status):
    max_len = len('SUCCEEDED') + 1
    color = F.WHITE

    if status in ['OK', 'SUCCEEDED']:
        color = F.GREEN
    if status == 'RUNNING':
        color = F.YELLOW
    if status in ['FAILED', 'ERROR', 'KILLED']:
        color = F.RED

    padding = (max_len - len(status)) * '-'
    return color + status + ' ' + padding + '>' + S.RESET_ALL


def color_name(name):
    if len(name) > 47:
        name = name[:47] + '...'
    formatted = '{:<50}'.format(name)
    return F.MAGENTA + formatted + S.RESET_ALL


def format_flow_header(flow):
    format_str = '{status} {name} {start} by {user}'
    return format_str.format(
        status=color_status(flow.status),
        name=color_name(flow.name),
        start=flow.start,
        user=flow.user)


def format_job(job, include_logs=False, prefix='  '):
    name_len = 52 - len(prefix)
    lines = [
        ('{prefix}{status} {name:<' + str(name_len) + '} {start} to {end}').format(
            prefix=prefix,
            status=color_status(job.status),
            name=job.name,
            start=time_from_datestring(job.start),
            end=time_from_datestring(job.end)),
    ]

    if include_logs and isinstance(job, Job):
        lines.append('{prefix}             {logs}'.format(
            prefix=prefix,
            logs=job.logs_link))

    if isinstance(job, Workflow):
        for (_, nested_job) in sort_jobs_by_start(job):
            lines.append(format_job(nested_job, include_logs, prefix + '  '))

    return '\n'.join(lines)


def format_jobs(flow, include_logs=False):
    return '\n'.join([format_job(job, include_logs=include_logs)
                      for (_, job) in sort_jobs_by_start(flow)])


def p(flows):
    if isinstance(flows, Workflow):
        flows = [flows]

    for flow in flows:
        print(format_flow_header(flow))


def pp(flows, logs=False):
    if isinstance(flows, Workflow):
        flows = [flows]

    for flow in flows:
        print(format_flow_header(flow))
        print(format_jobs(flow, include_logs=logs))
        print()
