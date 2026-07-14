from datetime import datetime
from types import SimpleNamespace

from src.common.data_models.message_component_data_model import MessageSequence
from src.maisaka.builtin_tool.reply import _find_recent_reply_to_target
from src.maisaka.context.messages import SessionBackedMessage


def test_find_recent_reply_uses_stored_reply_to_without_quote_component() -> None:
    history_message = SessionBackedMessage(
        raw_message=MessageSequence([]),
        visible_text="previous reply",
        timestamp=datetime.now(),
        message_id="reply-message-id",
        original_message=SimpleNamespace(reply_to="target-message-id"),
        source_kind="guided_reply",
    )

    assert _find_recent_reply_to_target([history_message], "target-message-id") == "previous reply"
