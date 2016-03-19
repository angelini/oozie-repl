import api
from colorama import Fore as F, Style as S
import re


def time_from_datestring(date_str):
    if not date_str:
        return F.YELLOW + '--:--:--' + S.RESET_ALL

    match = re.match(r'.*(?P<time>\d{2}:\d{2}:\d{2}).*', date_str)
    return match.group('time')


def sort_by_start(tree):
    if not tree:
        return []
    return sorted(tree.items(), key=lambda i: i[1]['start'])


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


def format_workflow_header(workflow):
    format_str = '{status} {name} {start} by {user}'
    return format_str.format(
        status=color_status(workflow['status']),
        name=color_name(workflow['appName']),
        start=workflow['startTime'],
        user=workflow['user'])


def format_workflow_action(name, action, prefix='  '):
    name_len = 52 - len(prefix)
    format_str = '{prefix}{status} {name:<' + str(name_len) + '} {start} to {end}'
    lines = [format_str.format(
        prefix=prefix,
        status=color_status(action['status']),
        name=name,
        start=time_from_datestring(action['start']),
        end=time_from_datestring(action['end']))]

    for child in sort_by_start(action.get('children')):
        lines.append(format_workflow_action(child[0], child[1], prefix + '  '))

    return '\n'.join(lines)


def format_workflow_tree(tree):
    return '\n'.join([format_workflow_action(n, a)
                      for (n, a) in sort_by_start(tree)])


def p(workflows):
    for workflow in workflows:
        print(format_workflow_header(workflow))


def pp(workflows):
    for workflow in workflows:
        tree = api.get_full_tree(workflow['id'])
        print(format_workflow_header(workflow))
        print(format_workflow_tree(tree))
        print()
