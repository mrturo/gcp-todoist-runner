"""Tests for 'every weekday' recurrence pattern."""

from src.core.processing import infer_next_recurrence


def test_every_weekday_monday_to_tuesday():
    """Test that Monday (weekday 0) advances to Tuesday (+1 day)."""
    due_dict = {
        "date": "2026-02-02",  # Monday
        "frequency": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-03"  # Tuesday


def test_every_weekday_tuesday_to_wednesday():
    """Test that Tuesday (weekday 1) advances to Wednesday (+1 day)."""
    due_dict = {
        "date": "2026-02-03",  # Tuesday
        "frequency": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-04"  # Wednesday


def test_every_weekday_wednesday_to_thursday():
    """Test that Wednesday (weekday 2) advances to Thursday (+1 day)."""
    due_dict = {
        "date": "2026-02-04",  # Wednesday
        "frequency": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-05"  # Thursday


def test_every_weekday_thursday_to_friday():
    """Test that Thursday (weekday 3) advances to Friday (+1 day)."""
    due_dict = {
        "date": "2026-02-05",  # Thursday
        "frequency": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-06"  # Friday


def test_every_weekday_friday_to_monday():
    """Test that Friday (weekday 4) advances to Monday (+3 days)."""
    due_dict = {
        "date": "2026-02-06",  # Friday
        "frequency": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-09"  # Monday


def test_every_weekday_saturday_to_monday():
    """Test that Saturday (weekday 5) advances to Monday (+2 days)."""
    due_dict = {
        "date": "2026-02-07",  # Saturday
        "frequency": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-09"  # Monday


def test_every_weekday_sunday_to_monday():
    """Test that Sunday (weekday 6) advances to Monday (+1 day)."""
    due_dict = {
        "date": "2026-02-08",  # Sunday
        "frequency": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-09"  # Monday


def test_every_weekday_spanish():
    """Test that Spanish 'cada día laboral' pattern works."""
    due_dict = {
        "date": "2026-02-02",  # Monday
        "frequency": "cada día laboral",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-03"  # Tuesday


def test_every_weekday_with_string_key():
    """Test that 'every weekday' works with 'string' key (fallback)."""
    due_dict = {
        "date": "2026-02-02",  # Monday
        "string": "every weekday",
        "recurring": True,
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-03"  # Tuesday


def test_every_weekday_exact_example_from_issue():
    """Test the exact example from the user's report."""
    # User reported: date "2026-02-02" (Monday) was getting "2026-02-09"
    # Expected: "2026-02-03" (Tuesday)
    due_dict = {
        "lang": "en",
        "date": "2026-02-02",
        "is_recurring": True,
        "timezone": None,
        "frequency": "every weekday",
    }
    result = infer_next_recurrence(due_dict)
    assert result == "2026-02-03"  # Next business day (Tuesday)
