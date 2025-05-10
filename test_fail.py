from main import count_characters

def test_fail_count_characters():
    assert count_characters("Hello") == 999  # 故意錯
