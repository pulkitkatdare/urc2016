"""autogenerated by genpy from navigation/rover_mobility_arduino.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class rover_mobility_arduino(genpy.Message):
  _md5sum = "5235661df0d289b478808517d3970358"
  _type = "navigation/rover_mobility_arduino"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Data Type for Speed given to each of the motors
float64 S1
float64 S2
float64 S3
float64 S4
float64 S5
float64 S6
# Data type for individual angle rotation
float64 A1
float64 A2
float64 A3
float64 A4


"""
  __slots__ = ['S1','S2','S3','S4','S5','S6','A1','A2','A3','A4']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       S1,S2,S3,S4,S5,S6,A1,A2,A3,A4

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(rover_mobility_arduino, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.S1 is None:
        self.S1 = 0.
      if self.S2 is None:
        self.S2 = 0.
      if self.S3 is None:
        self.S3 = 0.
      if self.S4 is None:
        self.S4 = 0.
      if self.S5 is None:
        self.S5 = 0.
      if self.S6 is None:
        self.S6 = 0.
      if self.A1 is None:
        self.A1 = 0.
      if self.A2 is None:
        self.A2 = 0.
      if self.A3 is None:
        self.A3 = 0.
      if self.A4 is None:
        self.A4 = 0.
    else:
      self.S1 = 0.
      self.S2 = 0.
      self.S3 = 0.
      self.S4 = 0.
      self.S5 = 0.
      self.S6 = 0.
      self.A1 = 0.
      self.A2 = 0.
      self.A3 = 0.
      self.A4 = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_10d.pack(_x.S1, _x.S2, _x.S3, _x.S4, _x.S5, _x.S6, _x.A1, _x.A2, _x.A3, _x.A4))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 80
      (_x.S1, _x.S2, _x.S3, _x.S4, _x.S5, _x.S6, _x.A1, _x.A2, _x.A3, _x.A4,) = _struct_10d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_10d.pack(_x.S1, _x.S2, _x.S3, _x.S4, _x.S5, _x.S6, _x.A1, _x.A2, _x.A3, _x.A4))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 80
      (_x.S1, _x.S2, _x.S3, _x.S4, _x.S5, _x.S6, _x.A1, _x.A2, _x.A3, _x.A4,) = _struct_10d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_10d = struct.Struct("<10d")
