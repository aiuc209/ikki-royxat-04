import pytest
from your_module import describe_weather

def test_describe_weather():
    temperatures = [25, 10, 30]
    humidities = [60, 40, 80]
    expected_results = ["Issiq va nam", "Sovuq", "Issiq va nam"]
    results = describe_weather(temperatures, humidities)
    assert results == expected_results

def test_describe_weather_empty_lists():
    temperatures = []
    humidities = []
    expected_results = []
    results = describe_weather(temperatures, humidities)
    assert results == expected_results

def test_describe_weather_different_list_lengths():
    temperatures = [25, 10, 30]
    humidities = [60, 40]
    with pytest.raises(ValueError):
        describe_weather(temperatures, humidities)
