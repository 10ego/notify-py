# Notify-py wrapper
_repository data modified for github port_

## How To Use

### Import from another script
<pre>
import noti

model_name = "skynet"
model_performance = "99%"
team_member = "me" # array is okay for multiple users (e.g. ["me", "also_me"] )

notify( team_member = team_member,
        model_name = model_name,
        message = model_performance
        )
</pre>
### Run from the terminal

By default it is set to run the VM Reboot notification.
<pre>
root@terminal:~/notify-py$ python3 noti.py -u "me,also_me" -m `hostname`
</pre>


## Template
Extend the template UUID by revising/editing `template.json` as needed.

_NOTE_: the template must be creaetd on your service Templates list on https://notification.alpha.canada.ca/services

## Team
Extend the team members by revising/editing the `team.json` as needed.
_NOTE_: the team member must exist on your service Team members list on https://notification.alpha.canada.ca/services
