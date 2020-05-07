def load_mock(filename: str, encoding="utf-8"):
    with open(f"tests/mocks/{filename}", mode="r", encoding=encoding) as f:
        return f.read()
