import pytest

from test_poetry.src.widget import get_data, masked_account_card


@pytest.mark.parametrize("entry, exit", [
    (

            "2222 3333 4444 5555",
            "2222 33** **** 5555"

    )
                                        ]
                         )
def test_masked_account_card(entry, exit):
    assert masked_account_card(entry) == exit


@pytest.mark.parametrize("entry, exit", [
    (

                "2019.07.03",

                "03.07.2019"

    )
]
                         )
def test_get_data(entry, exit):
    assert get_data(entry) == exit
