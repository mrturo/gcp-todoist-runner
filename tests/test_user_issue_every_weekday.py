"""Integration test for the exact case reported by the user."""

from src.core.processing import infer_next_recurrence


def test_user_reported_issue_every_weekday():
    """Test the exact case reported by the user.

    User reported task:
        "id": "6f6gfRPp38Vrq4pR",
        "content": "🔵(B02-03-00)💻Update work macbook OS & apps",
        "due": {
            "date": "2026-02-02",  (Monday)
            "lang": "en",
            "is_recurring": true,
            "timezone": null,
            "next_recurrence_date": "2026-02-09",  (Wrong: next Monday)
            "frequency": "every weekday"
        }

    Expected: next_recurrence_date should be "2026-02-03" (Tuesday)
    """
    due_dict = {
        "date": "2026-02-02",  # Monday
        "lang": "en",
        "is_recurring": True,
        "timezone": None,
        "frequency": "every weekday",
    }

    result = infer_next_recurrence(due_dict)

    # Should be the next business day (Tuesday), not next Monday
    assert result == "2026-02-03", (
        f"Expected '2026-02-03' (Tuesday, next business day), " f"but got '{result}'"
    )
