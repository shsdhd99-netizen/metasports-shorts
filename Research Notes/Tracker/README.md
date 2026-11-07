# Shorts Tracker (owner, Nov 7, 2026)
Inside both Hubs (sections "How the Shorts are doing" and "Coming up"; NBA https://claude.ai/artifact/SAWcHwuAwBxJuyBQSs8a8U, FC https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3; block added by `Tools/hub_tracker_block.py`; data = each Hub's db doc `tracker/current` pointing at the uploaded hub_<ch>.json). Both-channel dashboard: https://claude.ai/artifact/6kpu5HUkFtCzyFNjNCTPVv ("MetaSports Shorts Tracker", both channels).
Built by `python Tools/short_tracker.py` from: the PC's YouTube Analytics pulls (`Studio exports/api*/daily|retention <date>.csv`),
Studio exports (the only source of "Stayed to watch"), public view counts (yt-dlp, logged in `public_views_log.csv`) and
`Scheduled Uploads.csv`. Refreshed twice a day by the scheduled task "MetaSports tracker refresh" (8:37 AM and 7:13 PM ET):
it re-runs the tool, uploads the 4 JSON files to the dashboard and repoints its datasets (shorts, history, retention, upcoming).
New Studio export (owner, weekly zip into `Research Notes/Studio exports/`): stayed % fills in at the next refresh.
