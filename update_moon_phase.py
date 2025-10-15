import datetime
import math
import pytz
import re

# --- Astronomical Constants ---
J2000 = 2451545.0           # Julian Day for Jan 1, 2000 12:00 UTC
SYNODIC_MONTH = 29.530588861  # Average length of lunar cycle in days

# --- Moon Phase Emoji Mapping ---
MOON_EMOJIS = [
    "🌑",  # New Moon
    "🌒",  # Waxing Crescent
    "🌓",  # First Quarter
    "🌔",  # Waxing Gibbous
    "🌕",  # Full Moon
    "🌖",  # Waning Gibbous
    "🌗",  # Last Quarter
    "🌘",  # Waning Crescent
]

def get_moon_age(dt_utc):
    """Return the moon age in days for a given UTC datetime."""
    if dt_utc.tzinfo is None or dt_utc.tzinfo.utcoffset(dt_utc) is None:
        dt_utc = dt_utc.replace(tzinfo=pytz.utc)
    else:
        dt_utc = dt_utc.astimezone(pytz.utc)

    jd = dt_utc.toordinal() + 1721424.5 + \
         (dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600) / 24

    days_since_J2000 = jd - J2000
    new_moons = days_since_J2000 / SYNODIC_MONTH
    age = (new_moons - math.floor(new_moons)) * SYNODIC_MONTH
    return age

def get_moon_emoji(age):
    """Map moon age in days to one of 8 emojis."""
    quarter = SYNODIC_MONTH / 4
    if age < 0.5 or age > SYNODIC_MONTH - 0.5:
        return MOON_EMOJIS[0]
    elif age < quarter:
        return MOON_EMOJIS[1]
    elif age < 2*quarter:
        return MOON_EMOJIS[2] if age < quarter + 1.5 else MOON_EMOJIS[3]
    elif age < 2*quarter + 0.5:
        return MOON_EMOJIS[4]
    elif age < 3*quarter:
        return MOON_EMOJIS[5]
    elif age < 4*quarter:
        return MOON_EMOJIS[6] if age < 3*quarter + 1.5 else MOON_EMOJIS[7]
    return MOON_EMOJIS[0]

# --- Update README ---
def update_readme():
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.datetime.now(ist)
    now_utc = now_ist.astimezone(pytz.utc)

    age = get_moon_age(now_utc)
    emoji = get_moon_emoji(age)

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Replace the first emoji (👋 or previous moon emoji) with the current moon emoji
    new_content = re.sub(
        r"(👋|🌑|🌒|🌓|🌔|🌕|🌖|🌗|🌘)",
        emoji,
        content,
        count=1
    )

    # Add/update a hidden comment with the moon age for reference
    age_comment = f"<!-- Moon age: {age:.1f} days -->"
    if "<!-- Moon age:" in new_content:
        new_content = re.sub(r"<!-- Moon age:.*?-->", age_comment, new_content)
    else:
        new_content += f"\n{age_comment}\n"

    if new_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated README: {emoji} ({age:.1f} days)")
    else:
        print("No update needed; emoji already current.")

if __name__ == "__main__":
    update_readme()
