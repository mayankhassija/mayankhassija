import datetime
import math
import pytz
import re

# --- Astronomical Constants ---
J2000 = 2451545.0
SYNODIC_MONTH = 29.530588861
LAST_NEW_MOON_EPOCH_UTC = datetime.datetime(2024, 12, 30, 22, 27, 0, tzinfo=pytz.utc)

# --- Core Function ---
def get_accurate_moon_phase_emoji(target_datetime):
    if target_datetime.tzinfo is None or target_datetime.tzinfo.utcoffset(target_datetime) is None:
        current_datetime_utc = target_datetime.replace(tzinfo=pytz.utc)
    else:
        current_datetime_utc = target_datetime.astimezone(pytz.utc)

    jd = current_datetime_utc.toordinal() + 1721424.5 + \
         (current_datetime_utc.hour + current_datetime_utc.minute/60.0 + current_datetime_utc.second/3600.0) / 24.0

    days_since_J2000 = jd - J2000
    new_moons = days_since_J2000 / SYNODIC_MONTH
    moon_age = (new_moons - math.floor(new_moons)) * SYNODIC_MONTH

    quarter = SYNODIC_MONTH / 4.0

    if moon_age < 0.5 or moon_age > SYNODIC_MONTH - 0.5:
        return "🌑"
    elif moon_age < quarter:
        return "🌒"
    elif moon_age < quarter * 2:
        return "🌓" if moon_age < quarter + 1.5 else "🌔"
    elif moon_age < quarter * 2 + 0.5:
        return "🌕"
    elif moon_age < quarter * 3:
        return "🌖"
    elif moon_age < quarter * 4:
        return "🌗" if moon_age < quarter * 3 + 1.5 else "🌘"
    return "🌑"

# --- Update README ---
def update_readme_with_moon():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time_local = datetime.datetime.now(ist_timezone)
    moon_emoji = get_accurate_moon_phase_emoji(current_time_local)

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Replace 👋 or any moon emoji with the current one
    new_content = re.sub(r"(👋|🌑|🌒|🌓|🌔|🌕|🌖|🌗|🌘)", moon_emoji, content, count=1)

    if new_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated README with moon phase: {moon_emoji}")
    else:
        print("No change needed (emoji already up-to-date).")

if __name__ == "__main__":
    update_readme_with_moon()
