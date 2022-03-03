"""
DataFrame
---------
An efficient 2D container for potentially mixed-type time series or other
labeled data series.
Similar to its R counterpart, data.frame, except providing automatic data
alignment and a host of useful data manipulation methods having to do with the
labeling information
"""

class Person:
    """
    Two-dimensional, size-mutable, potentially heterogeneous tabular data.
    Data structure also contains labeled axes (rows and columns).
    Arithmetic operations align on both row and column labels. Can be
    thought of as a dict-like container for Series objects. The primary
    pandas data structure.
    Parameters
    ----------
    data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If
        data is a dict, column order follows insertion-order. If a dict contains Series
        which have an index defined, it is aligned by its index.
        .. versionchanged:: 0.25.0
           If data is a list of dicts, column order follows insertion-order.
    index : Index or array-like
        Index to use for resulting frame. Will default to RangeIndex if
        no indexing information part of input data and no index provided.
    columns : Index or array-like
        Column labels to use for resulting frame when data does not have them,
        defaulting to RangeIndex(0, 1, 2, ..., n). If data contains column labels,
        will perform column selection instead.
    dtype : dtype, default None
        Data type to force. Only a single dtype is allowed. If None, infer.
    copy : bool or None, default None
        Copy data from inputs.
        For dict data, the default of None behaves like ``copy=True``.  For DataFrame
        or 2d ndarray input, the default of None behaves like ``copy=False``.
        .. versionchanged:: 1.3.0
    See Also
    --------
    DataFrame.from_records : Constructor from tuples, also record arrays.
    DataFrame.from_dict : From dicts of Series, arrays, or dicts.
    read_csv : Read a comma-separated values (csv) file into DataFrame.
    read_table : Read general delimited file into DataFrame.
    read_clipboard : Read text from clipboard into DataFrame.
    Examples
    --------
    Constructing DataFrame from a dictionary.
    >>> d = {'col1': [1, 2], 'col2': [3, 4]}
    >>> df = pd.DataFrame(data=d)
    >>> df
       col1  col2
    0     1     3
    1     2     4
    Notice that the inferred dtype is int64.
    >>> df.dtypes
    col1    int64
    col2    int64
    dtype: object
    To enforce a single dtype:
    >>> df = pd.DataFrame(data=d, dtype=np.int8)
    >>> df.dtypes
    col1    int8
    col2    int8
    dtype: object
    Constructing DataFrame from a dictionary including Series:
    >>> d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
    >>> pd.DataFrame(data=d, index=[0, 1, 2, 3])
       col1  col2
    0     0   NaN
    1     1   NaN
    2     2   2.0
    3     3   3.0
    Constructing DataFrame from numpy ndarray:
    >>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ...                    columns=['a', 'b', 'c'])
    >>> df2
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    Constructing DataFrame from a numpy ndarray that has labeled columns:
    >>> data = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)],
    ...                 dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])
    >>> df3 = pd.DataFrame(data, columns=['c', 'a'])
    ...
    >>> df3
       c  a
    0  3  1
    1  6  4
    2  9  7
    Constructing DataFrame from dataclass:
    >>> from dataclasses import make_dataclass
    >>> Point = make_dataclass("Point", [("x", int), ("y", int)])
    >>> pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
       x  y
    0  0  0
    1  0  3
    2  2  3
    """

    # class variable: every instance will inherit this value
    nationality = "italy" 

    def __init__(self, name, job=None, pay=0):
        """Constructor. It runs every instance is created"""
        self.name = name
        self.job = job
        self.pay = pay

    # Behaviour Methods
    def lastName(self):
        """
        Return a list representing the axes of the DataFrame.
        It has the row axis labels and column axis labels as the only members.
        They are returned in that order.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.axes
        [RangeIndex(start=0, stop=2, step=1), Index(['col1', 'col2'],
        dtype='object')]
        """
        return self.name.split()[-1]  # self is implied subject

    def giveRaise(self, percent):
        """Give this object a raise"""
        self.pay = int(self.pay * (1 + percent))  # much change here only

    def __repr__(self):
        """"
        If you don't overload __str__ when running:
        >>> print(sue) # will show something like
        <__main__.Person object at 0x7fa3288ed9d0> 
        __repr__ and __str__ are run automatically everytime an instance is converted to its print string.
        o __str__ are used for more user friedly info
        o __repr__ is used to provide extra details to developers
        """
        return "[Person: %s, %s]" % (self.name, self.pay)  # string to print
    

class Manager(Person):
    # Inherit Person attrs
    def giveRaise(self, percent, bonus=0.10):  # Redefine method
        Person.giveRaise(self, percent+bonus)  # GOOD way: augment original

if __name__ == "__main__":  # when run for testing only

    # create object instances
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job='dev', pay=100)
    tom = Manager("Tom Jonen", 'mgr', 1000)
    for obj in (bob, sue, tom):
        obj.giveRaise(0.10)
        print(obj)

    # show special class attribute
    print(bob.__class__)                # Show bob's class and his name
    print(bob.__class__.__bases__)

    # show attribute (the one defined in __init__)
    for key in bob.__dict__:
        print(key, "=>", bob.__dict__[key]) # 1st way
        print(key, "=>", getattr(bob,key))  # 2nd way useful to catch exception