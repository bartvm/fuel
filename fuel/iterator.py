import six


class DataIterator(six.Iterator):
    """An iterator over data, representing a single epoch.

    Parameters
    ----------
    data_stream : :class:`DataStream` or :class:`Transformer`
        The data stream over which to iterate.
    request_iterator : iterator
        An iterator which returns the request to pass to the data stream
        for each step.

    """
    def __init__(self, data_stream, request_iterator=None, as_dict=False):
        self.data_stream = data_stream
        self.request_iterator = request_iterator
        self.as_dict = as_dict

    def __iter__(self):
        return self

    def __next__(self):
        if self.request_iterator is not None:
            if self.data_stream.batch :
                data = self.data_stream.get_batch(next(self.request_iterator))
            else : 
                data = self.data_stream.get_example(next(self.request_iterator))
        else:
            if self.data_stream.batch :
                data = self.data_stream.get_batch()
            else :
                data = self.data_stream.get_example()
        if self.as_dict:
            return dict(zip(self.data_stream.sources, data))
        else:
            return data
