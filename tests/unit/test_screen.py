import pytest

from retro_screen.screen import Screen


class TestScreen:
    def test_uninitialized_fails(self):
        with pytest.raises(RuntimeError) as e:
            _ = Screen()
        assert "pygame.display must be initialized" in str(e.value)
