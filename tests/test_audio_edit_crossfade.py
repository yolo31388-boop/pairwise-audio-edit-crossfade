import pytest
import media.audio_edit_crossfade as mod

CASES = [
    ("snap_zero_crossing", (1,)),
    ("fade_by_samples", (1,)),
    ("render_version_tag", (1,)),
    ("equal_power_curve", (1,)),
    ("fade_once_per_clip", (1,)),
    ("verify_after_splice", (1,)),
    ("cut", (1,)),
    ("fade", (1,)),
    ("mix", (1,)),
    ("export", (1,)),
    ("validate_crossfade", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
