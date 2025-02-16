from file_organizer import FileOrganizer
from state_machine import StateMachine

def test_organize():
    state = StateMachine()
    organizer = FileOrganizer(state)

    organizer.organize()
    assert len(state.history) > 0  # At least one snapshot should exist
