## caldav-fastmail


#
#  sudo apt install python3-caldav
#
# 1. Go to fastmail and get a CalDav URL for an existing calendar
# 2. Generate an app password - make it for "CalDav" access.
#
#  CALDAV_URL="<obtail from Fastmail export>" CALDAV_USER="you@domain.tld" CALDAV_PASS="<Fastmail app password>" python3 fastmail_create_todo_list.py
#
#  4. Go to Fastmail again and see that a calendar "TODO" is now shown
#  5. Export a CalDav URL for this calendar
#  6. Potentially, create a new app password for Thunderbird so we don't
#     reuse the one that we've just used in the command-line
