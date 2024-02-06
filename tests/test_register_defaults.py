import pytest

import jsonplus
from jsonplus import JSONEncoderPlus


class CustomType:
    """
    CustomType to test our implementation of the default method.
    Types supported by the standard JSONEncoder are encoded before our code run.
    """


class TestDefaultEncoderRegistration:
    @pytest.fixture
    def empty_encoder(self, monkeypatch):
        monkeypatch.setattr(jsonplus.JSONEncoderPlus, "default_functional_encoders", [])
        monkeypatch.setattr(jsonplus.JSONEncoderPlus, "default_typed_encoders", {})

    def test_register_default_encoder_with_module_api(self, empty_encoder):
        jsonplus.register_default_encoder(lambda o: "functional default encoder")
        jsonplus.register_default_encoder(lambda o: "typed default encoder", CustomType)

        assert jsonplus.dumps(CustomType()) == '"typed default encoder"'
        assert jsonplus.dumps(object()) == '"functional default encoder"'

    def test_register_default_encoder_with_classmethod(self, empty_encoder):
        JSONEncoderPlus.register_default_encoder(lambda o: "functional default encoder")
        JSONEncoderPlus.register_default_encoder(lambda o: "typed default encoder", CustomType)

        assert jsonplus.dumps(CustomType()) == '"typed default encoder"'
        assert jsonplus.dumps(object()) == '"functional default encoder"'