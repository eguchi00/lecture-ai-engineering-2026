from types import SimpleNamespace

from google.genai import types

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    usage = types.GenerateContentResponseUsageMetadata(
        prompt_token_count=12,
        candidates_token_count=34,
    )
    response = SimpleNamespace(text="回答", usage_metadata=usage)

    class FakeModels:
        def generate_content(self, *, model, contents):
            return response

    monkeypatch.setattr(ask.genai, "Client", lambda api_key: SimpleNamespace(models=FakeModels()))
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")

    assert ask.ask("質問") == "回答"
    assert capsys.readouterr().out == "[tokens] 入力: 12, 出力: 34\n"
