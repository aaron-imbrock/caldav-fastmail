#!/usr/bin/env python3

import os
import caldav

from dotenv import load_dotenv
load_dotenv()

caldav_url = os.environ["CALDAV_URL"]
username = os.environ["CALDAV_USER"]
password = os.environ["CALDAV_PASS"]
calendar_name = os.environ["CALENDAR_NAME"]

if __name__ == "__main__":
    client = caldav.DAVClient(url=caldav_url, username=username, password=password)
    caldav.Principal(client).make_calendar(name=calendar_name, supported_calendar_component_set=["VTODO", "VEVENT",])
