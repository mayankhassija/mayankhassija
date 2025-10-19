import datetime
import pytz
import re
from skyfield.api import load
from skyfield import almanac

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

# --- Astronomical Data Loader ---
# Load timescale and ephemeris (planetary position data from JPL)
ts = load.timescale()
# This file will be auto-downloaded on first run
eph = load('de421.bsp') 

def get_current_moon_emoji():
    """
    Calculate the current moon phase and return the corresponding emoji
    and the phase angle (in degrees).
    """
    t = ts.now()
    
    # Calculate the moon's phase angle (0-360 degrees)
    # 0 = New Moon, 90 = First Quarter, 180 = Full Moon, 270 = Last Quarter
    phase_angle = almanac.moon_phase(eph, t).degrees

    # We have 8 emojis, so we divide the 360 degrees into 8 slices (45 degrees each).
    # We use round() to find the nearest emoji index.
    emoji_index = round(phase_angle / 45) % 8
    
    emoji = MOON_EMOJIS[emoji_index]
    
    return emoji, phase_angle

# --- Update README ---
def update_readme():
    emoji, phase = get_current_moon_emoji()

    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: README.md not found. Make sure the file exists.")
        return

    # 1. Replace the first emoji (👋 or previous moon emoji)
    # The pattern matches the first instance of a waving hand or any moon emoji
    new_content = re.sub(
        r"(👋|🌑|🌒|🌓|🌔|🌕|🌖|🌗|🌘)",
        emoji,
        content,
        count=1
    )

    # 2. Add/update a hidden comment with the moon phase for reference
    phase_comment = f""
    
    # Define the pattern BEFORE its use in re.sub (This was the fix for NameError)
    # Pattern to find a previously existing moon phase comment
    phase_comment_pattern = r""

    # Try to replace an existing comment.
    # If a previous comment is found, re.sub replaces it with the new one.
    content_after_comment_replace = re.sub(
        phase_comment_pattern,
        phase_comment,
        new_content,
        count=1
    )
    
    # Check if a replacement occurred
    if content_after_comment_replace != new_content:
        # A replacement was made (an old comment existed)
        final_content = content_after_comment_replace
    else:
        # No old comment was found, so we append the new one to the end of the file.
        # We strip the content first to avoid excessive blank lines if the old content ended with whitespace.
        final_content = new_content.strip() + f"\n{phase_comment}\n"


    if final_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"Updated README: {emoji} ({phase:.1f} degrees)")
    else:
        print(f"No update needed. Current: {emoji} ({phase:.1f} degrees)")

if __name__ == "__main__":
    update_readme()
