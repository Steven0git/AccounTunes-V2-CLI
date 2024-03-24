from itertools import groupby 

class Storage:
    def __init__(self):
      pass
    def save(self) -> bool:
        """
        Saves all prompt data for execution.
        """
        if self._temp_store:
            for key, group in groupby(self._temp_store, key=lambda x: x[0]):
                self._data_store[key] = next(group)[1]
            return True
        else:
            return False

    def _save(self, data: tuple) -> bool:
        """
        Saves temporary data.

        Args:
            data(tuple): It only accepts tuples of length 2.
        """
        if len(data) == 2:
            self._temp_store.append(data)
            return True
        else:
            self.error_message("Error: Invalid data format.", False)
            return False
