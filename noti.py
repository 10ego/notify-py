import json
#from notifications_python_client.base import BaseAPIClient
from notifications_python_client.notifications import NotificationsAPIClient
import argparse
from os import path
import re

cwd = path.dirname(path.abspath(__file__))
cwd = re.search(r'.*\/notify-py\/?', cwd).group()


base_url = "https://api.notification.alpha.canada.ca"
with open(cwd+"/data/keys.json") as f:
    key_chain = json.load(f)
api_key = key_chain['default']
with open(cwd+"data/template.json") as f:
    template = json.load(f)
with open(cwd+"data/team.json") as f:
    team = json.load(f)

notifications_client = NotificationsAPIClient(base_url=base_url, api_key=api_key)

def notify(team_member, template_name, *args):
    assert type(team_member) is list, "Expected a list"
    template_id = template[template_name]['id']
    keys = template[template_name]['msg']
    personalisation = {}
    assert len(keys)==len(args), "Length of provided arguments does not match the template size"
    for key, msg in zip(keys, args):
        personalisation[key] = msg
    for member in team_member:
        assert team[member], "Not a proper team member"
        response = notifications_client.send_sms_notification(
            phone_number = team[member],
            template_id = template_id,
            personalisation = personalisation
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', help='message value')
    parser.add_argument('-u', help='users list to send message to (comma separate multiple users)')
    args = parser.parse_args()
    message = args.m
    assert message, "Expected message value"
    members = args.u
    if members:
        members = members.split(',')
    else:
        members = ['warren', 'erico', 'dan', 'ted']
    notify(members, 'vm_reboot', message)
