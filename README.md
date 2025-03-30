#### Why

Stop juggling multiple task apps across your devices. With this tool, you can manage your tasks directly through your existing Fastmail account, ensuring your to-dos stay synchronized everywhere while maintaining your privacy. Setup takes less than five minutes.

Fastmail does not include a dedicated task management tool with their service. Fortunately, the CalDAV protocol (which Fastmail uses) supports tasks through the VTODO component of the iCalendar format. This project leverages Fastmail's CalDAV implementation to create a task management solution that works seamlessly across Android, Apple, and Windows devices. Any tool that supports CalDAV will work.

##### Prereqs

If necessary first install `uv`.

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

##### Setup

```
git clone git@github.com:aaron-imbrock/caldav-fastmail.git
cd caldav-fastmail
cp env_example .env
uv sync
source .venv/bin/activate
```

##### Run

1. Go to Fastmail.com to get a CalDav URL for ANY existing calendar. The CalDav URLs can be found under Settings → Calendars, and click the Export link for any calendar. A small pop-up will appear with the URL.
2. Paste this value into the `.env CALDAV_URL` field. This existing calendar will not be changed in any way.
3. Separately create a new app password - make it for "CalDav" access - and paste this value into the `.env CALDAV_PASS` field.
4. The `.env CALDAV_USER` value is your Fastmail user name. This is usually the same as your email address.
5. The `.env CALENDAR_NAME` is whatever you want the calendar title to be. The additional properties assigned will allow both tasks and events, although I haven't fully explored this. For now, this calendar is just for tasks.
5. Run `uv run main.py` 6. The new calendar will be listed, and iOS will automatically list this calendar under `Reminders`.
