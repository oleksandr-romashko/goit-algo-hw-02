class Request:
    """
    Represents a service request with a unique identifier and data payload.
    """

    _id_counter = 0  # Static counter shared across all instances

    def __init__(self, data: dict) -> None:
        self._id = Request._id_counter
        self._data = data
        Request._id_counter += 1

    def __str__(self) -> str:
        return f"{self._id}"

    def __repr__(self) -> str:
        return f"Request(id={self._id}, data={self._data!r})"

    @property
    def id(self) -> int:
        return self._id

    @property
    def data(self) -> dict:
        return self._data
