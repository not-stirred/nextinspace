"""Pytest fixtures"""

import pytest

import nextinspace


@pytest.fixture
def example_launch_text():
    return open("tests/data/launch.json", "r").read()


@pytest.fixture
def example_rocket_text():
    return open("tests/data/rocket.json", "r").read()


@pytest.fixture
def example_event_text():
    return open("tests/data/event.json", "r").read()


@pytest.fixture
def example_launch_verbose(example_rocket):
    return nextinspace.Launch(
        name="New Shepard | NS-13",
        location="West Texas Suborbital Launch Site/ Corn Ranch, Corn Ranch, USA",
        description="This will be the 13th New Shepard mission...",
        date=nextinspace.date_str_to_datetime("2020-09-24T15:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        type_="Suborbital",
        rocket=example_rocket,
    )


@pytest.fixture
def example_launch_normal():
    return nextinspace.Launch(
        name="New Shepard | NS-13",
        location="West Texas Suborbital Launch Site/ Corn Ranch, Corn Ranch, USA",
        description="This will be the 13th New Shepard mission...",
        date=nextinspace.date_str_to_datetime("2020-09-24T15:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        type_="Suborbital",
        rocket=None,
    )


@pytest.fixture
def example_event():
    return nextinspace.Event(
        name="2017 NASA Astronaut class graduation ceremony",
        location="NASA's Johnson Space Center, Houston, TX, USA",
        description="NASA will honor the first class of astronaut...",
        date=nextinspace.date_str_to_datetime("2020-01-10T15:30:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        type_="Press Event",
    )


@pytest.fixture
def example_rocket():
    return nextinspace.Rocket(
        name="New Shepard",
        payload_leo=0,
        payload_gto=0,
        liftoff_thrust=490,
        liftoff_mass=75,
        max_stages=1,
        height=15.0,
        successful_launches=12,
        consecutive_successful_launches=12,
        failed_launches=0,
        maiden_flight_date=nextinspace.date_str_to_datetime("2015-04-29", "%Y-%m-%d"),
    )
