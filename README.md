# update-jira-fields

#### Description

This is a workhorse script that is very simple, but very helpful. The script hits the Jira API using JQL to pull back a series of target tickets, it then pulls a field from each issue and reformats it, and then adds the newly formatted data back into the field. Not very complicated, but it is designed to handle a large quantity of Jira issues.

#### Time Saved

Over the course of the day, up to an hour can be spent manually updating these fields, which is effectively eliminated with this script. Up to 5 hours saved per week.

#### Troubleshooting

1. Be sure you are logged onto proper VPN

2. Jira credintials are up to date (changes every 90 days)

#### Future improvements 

This is currently run on an "ad-hoc" basis, at the discretion of the analyst. It would be great to find a way to set this on a cadence, potentially implement a CRON job or integrate with Active Batch scheduler.
