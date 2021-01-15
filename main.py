#     __  ___
#    /  |/  /___ _____  ____  ___  _____        This is designed to be run at the discretion of the fulfillment analyst. Jira is queried and mapping field
#   / /|_/ / __ `/ __ \/ __ \/ _ \/ ___/        is updated so that the auto-verification tool can run and automatically progress tickets to a closed
#  / /  / / /_/ / /_/ / /_/ /  __/ /            status.
# /_/  /_/\__,_/ .___/ .___/\___/_/
#             /_/   /_/                         Written by Caleb Moore

from jira.client import JIRA  # --> installed with `pip install jira` in the terminal
import re  # Regex component

count = 0

# Jira auth
options = {'server': 'https://jira.server.com'}
jira = JIRA(options, basic_auth=('username', 'pass'))

# JQL Query
issues_in_proj = jira.search_issues('project = ABC AND issuetype = "Ticket Type" '
                                    'AND status = Open AND "Fulfill Channel ID" ~ "123" AND labels is EMPTY',
                                    maxResults=50)

# List to append regex-ed ids into
legacy_id = []

print('Pin Tickets Updated: \n')

# Loop that pulls original id map, subs in (788) using regex and then updates the field
for issue in issues_in_proj:
    print('Strategy Ticket: https://jira.server.com/browse/' + str(issue))
    print('Original Mapping: ' + issue.fields.customfield_12345)
    mapping =(re.sub(r'\((\d+)*\)', "(788)", issue.fields.customfield_12345))
    legacy_id.append(mapping)
    issue.update(fields={'customfield_12345': (str(legacy_id)[2:-2])})
    print('Updated Mapping: ' + (str(legacy_id)[2:-2]))
    legacy_id.clear()
    issue.update(fields={"labels": ['av.mapped']})
    print('Added av.mapped label to ticket\n')
    count += 1

print('You have updated the mapping on ' + str(count) + ' Pin tickets')
