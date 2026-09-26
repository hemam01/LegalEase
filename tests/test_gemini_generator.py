from ai_core.gemini_generator import GeminiDocumentGenerator


def test_generator_returns_document_from_user_input_when_api_is_unavailable(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    generator = GeminiDocumentGenerator()
    document = generator.generate_document(
        document_type="Employment Contract",
        parties="Alice and Bob",
        terms="Salary: $100,000 annually",
        dates="2026-09-26",
    )

    assert "Employment Contract" in document
    assert "Alice and Bob" in document
    assert "Salary: $100,000 annually" in document
    assert "2026-09-26" in document
