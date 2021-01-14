#     __  ___
#    /  |/  /___ _____  ____  ___  _____
#   / /|_/ / __ `/ __ \/ __ \/ _ \/ ___/
#  / /  / / /_/ / /_/ / /_/ /  __/ /
# /_/  /_/\__,_/ .___/ .___/\___/_/
#             /_/   /_/

from jira.client import JIRA  # --> installed with `pip install jira` in the terminal
import re  # Regex component

count = 0

# Jira auth
options = {'server': 'https://jira.server.com'}
jira = JIRA(options, basic_auth=('username', 'pass'))

# JQL Query
issues_in_proj = jira.search_issues('project = CAM AND issuetype = "Targeting Strategy" '
                                    'AND status = Fulfillment AND "Fulfill Channel ID" ~ "788" AND labels is EMPTY',
                                    maxResults=50)

# List to append regex-ed ids into
legacy_id = []

print('Pin Tickets Updated: \n')

# Loop that pulls original id map, subs in (788) and then updates the field
for issue in issues_in_proj:
    print('Strategy Ticket: https://jira.server.com/browse/' + str(issue))
    print('Original Mapping: ' + issue.fields.customfield_11502)
    mapping =(re.sub(r'\((\d+)*\)', "(788)", issue.fields.customfield_11502))
    legacy_id.append(mapping)
    issue.update(fields={'customfield_11502': (str(legacy_id)[2:-2])})
    print('Updated Mapping: ' + (str(legacy_id)[2:-2]))  # The [2:-2] may break the logic
    legacy_id.clear()
    issue.update(fields={"labels": ['av.mapped']})
    print('Added av.mapped label to ticket\n')
    count += 1

print('You have updated the mapping on ' + str(count) + ' Pin tickets')
