import datetime
import pytz
import re
from skyfield.api import load
from skyfield import almanac

# --- Moon Phase Emoji Mapping (same as yours) ---
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
eph = load('de421.bsp')  # This file will be auto-downloaded on first run

def get_current_moon_emoji():
    """
    Calculate the current moon phase and return the corresponding emoji
    and the phase angle (in degrees).
    """
    t = ts.now()
    
    # Calculate the moon's phase angle (0-360 degrees)
    # 0 = New Moon, 90 = First Quarter, 180 = Full Moon, 270 = Last Quarter
    phase_angle = almanac.moon_phase(eph, t).degrees

    # We have 8 emojis, so we divide the 360 degrees into 8 slices.
    # Each slice is 360 / 8 = 45 degrees.
    # We use round() to find the nearest emoji index.
    # The final '% 8' handles the wrap-around from 360° back to 0°.
    emoji_index = round(phase_angle / 45) % 8
    
    emoji = MOON_EMOJIS[emoji_index]
    
    return emoji, phase_angle

# --- Update README ---
def update_readme():
    emoji, phase = get_current_moon_emoji()

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Replace the first emoji (👋 or previous moon emoji)
    new_content = re.sub(
        r"(👋|🌑|🌒|🌓|🌔|🌕|🌖|🌗|🌘)",
        emoji,
        content,
        count=1
    )

    # Add/update a hidden comment with the moon phase for reference
    phase_comment = f""
    if "", phase_comment, new_content)
    else:
        new_content += f"\n{phase_comment}\n"

    if new_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated README: {emoji} ({phase:.1f} degrees)")
    else:
        print(f"No update needed. Current: {emoji} ({phase:.1f} degrees)")

if __name__ == "__main__":
    update_readme()
