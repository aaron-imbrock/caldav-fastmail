## Documentation

### Setup

```
git clone git@github.com:aaron-imbrock/caldav-fastmail.git
cd caldav-fastmail
uv sync
source .venv/bin/activate
```

### Run

1. Go to Fastmail.com to get a CalDav URL for ANY existing calendar. The caldav urls can be found under Settings → Calendars and clicking the Export link for any calendar. A little pop-up will appear with the url.
2. Paste that value into the `.env CALDAV_URL` field. This existing calendar will not be modified in any way.
3. Seperately, generate a new app password - make it for "CalDav" access - and paste that value into the `.env CALDAV_PASS` field.
4. The `.env CALDAV_USER` value will be your Fastmail username. This value is usually the same as your email address.
5. `env CALENDAR_NAME` is the name of the new calendar. The additional properties assigned will allow Tasks and Events, though I've not explored this fully.
5. Run `uv run main.py`
6. The new calendar will be listed, and iOS will list that calendar under `Reminders` automatically.
