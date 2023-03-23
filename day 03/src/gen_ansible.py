import yaml
import ansible
tasks = [
    {
        'apt': {'name': ['python3', 'nginx']},
        'state': 'latest'
    },
    {
        'name': 'Copy over files',
        'ansible.builtin.copy': {'src': ['exploit.py', 'consumer.py'],
                                 'dest': ['/etc/exploit.py', '/etc/consumer.py']},
        'become': 'yes',
    },
    {
        'name': 'Run files ',
        'shell': 'python /home/exploit.py',
        'become': 'yes'
    },
    {
        'name': 'Run consumer.py',
        'shell': 'python //home/consumer.py -e "{{ bad_guys }}"',
        'become': 'yes'
    }
]

playbook = {
    'hosts': 'localhost',
    'vars': {
        'bad_guys': ['4815162342', '3133780085']
    },
    'tasks': tasks
}

with open('deploy.yml', 'w') as f:
    yaml.dump(playbook, f)
