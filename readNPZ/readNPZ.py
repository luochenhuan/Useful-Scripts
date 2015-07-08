import base64
import metaseq
import os
import json
import numpy as np

curpath = os.path.dirname(os.path.realpath(__file__))
npzprefix = 'example'
arraykey = 'ip'
npzprefixfile_path = os.path.join(curpath, npzprefix)
print "please check if the following npzfile path with prefix is right: " + npzprefixfile_path
jsonfile_path = os.path.join(curpath, 'data/', arraykey)
jsonfile_path += '.json'
print "please check if the following json file path is right: " + jsonfile_path

"""
ref: http://stackoverflow.com/questions/3488934/simplejson-and-numpy-array/24375113#24375113
"""
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        if input object is a ndarray it will be converted into a dict holding dtype, shape and the data base64 encoded
        """
        if isinstance(obj, np.ndarray):
            data_b64 = base64.b64encode(obj.data)
            return dict(__ndarray__=data_b64,
                        dtype=str(obj.dtype),
                        shape=obj.shape)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder(self, obj)

def json_numpy_obj_hook(dct):
    """
    Decodes a previously encoded numpy ndarray
    with proper shape and dtype
    :param dct: (dict) json encoded ndarray
    :return: (ndarray) if input was an encoded ndarray
    """
    if isinstance(dct, dict) and '__ndarray__' in dct:
        data = base64.b64decode(dct['__ndarray__'])
        return np.frombuffer(data, dct['dtype']).reshape(dct['shape'])
    return dct


def save_array_to_json(jsonfile,array):
	dumped = json.dumps(array, cls=NumpyEncoder)
	with open(jsonfile, 'w') as f:
		f.write(dumped)



def load_array_from_json(jsonfile):
	with open(jsonfile) as json_data:
		dct = json.load(json_data)
		return json_numpy_obj_hook(dct)
		# return array

def arr2json(jsonfile_path, arr):
	with open(jsonfile_path, 'w') as outfile:
		json.dump(arr.tolist(), outfile)
    
def json2arr(jsonfile_path,dtype='float'):
	with open(jsonfile_path, 'r') as f:
		data = json.load(f)
	return np.fromiter(data, dtype)
    # return np.fromiter(json.loads(jsonfile_path),dtype)

def load_array_by_key(prefix, key):
	"""
    load features and NumPy arrays that were saved with `prefix`,
    return NumPy arrays that in arrays['key']
  	"""
	features, arrays = metaseq.persistence.load_features_and_arrays(prefix=prefix)
	return arrays[key]


"""
main function
"""
#load array from npzfile with key
arr = load_array_by_key(prefix=npzprefixfile_path, key=arraykey) # return <type 'numpy.ndarray'>
# assert arr.shape == (5708, 100)

# save np.array to json file 
save_array_to_json(jsonfile_path, arr)
# arr2json(jsonfile_path, arr)

# load json file to np.array
recover_arr = load_array_from_json(jsonfile_path)
# recover_arr = json2arr(jsonfile_path, dtype='float')

assert arr.shape == recover_arr.shape
