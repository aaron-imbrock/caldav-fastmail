#### Why should you do this?

We all love Fastmail. Their product is fast and supports all email and calendar features we have ever wanted. Expect for Tasks!

Interestingly enough though, your iPhone Tasks app is also a calendar. How is that? 

The magic word is CalDAV. It's a boring and stable technology, used everywhere and in unexpected ways, but rarely mentioned.

Fastmail uses CalDAV for calendering. And in the same unexpected way that iMessage is a fancy UI for a sqlite database, Apple Tasks is a frontend for ... yeah, you get it.

With a little Python, you can create a Fastmail calendar to be both. You will have a calendar with a to-do list that your Apple product treats just like its own. 

Just as importantly, this calendar works on anything and everything else too: you're not tied to Mac or iPhone.

You'll end up with a calendar where you do Calendar things, and tasks where you do Tasks things. FastMail now offers Tasks.

#### Ok, let's do this

##### Prereqs

If necessary first install `uv`.

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

##### Setup

```
git clone git@github.com:aaron-imbrock/caldav-fastmail.git --depth 1
cd caldav-fastmail
cp env_example .env
uv sync
source .venv/bin/activate
```

##### Run

1. Go to Fastmail.com to get a CalDav URL for ANY existing calendar. The CalDav URLs can be found under Settings → Calendars, and click the Export link for any calendar. A small pop-up will appear with the URL.
1. Paste this value into the `.env CALDAV_URL` field. Note: We must provide an existing calendar URL to satisfy the CALDAV library requirements, however we never modify that calendar.
1. Separately create a new app password - make it for "CalDav" access - and paste this value into the `.env CALDAV_PASS` field.
1. The `.env CALDAV_USER` value is your Fastmail user name. This is the same as your email address.
1. The `.env CALENDAR_NAME` is whatever you want the new calendar title to be. I called it 'FASTMAIL/MAIN'. In `env_sample` it's called 'TODO'. 
1. Run `uv run main.py`. Fastmail does not surface The new calendar will be added on the webpage, and iOS will automatically list this calendar under `Reminders`.

I think that's cool.

##### Outcomes

![Screenshot of fastmail settings](images/fastmail.png)
![Screenshot of Task on iphone](images/iphone.png)
