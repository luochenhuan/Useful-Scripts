# Read .npz file and convert to numpy.ndarray & json
### example.npz & example.features are from [`metaseq` example 1](https://pythonhosted.org/metaseq/example_session.html)

The example.npz dictionary is like:
> arrays={'ip': ip_array, 'input': input_array}

By specifying `npzprefix` and `arraykey` variables, you can use your own .npz data.
The encrypted .json files are stored under `data` folder.