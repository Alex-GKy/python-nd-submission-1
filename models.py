"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional),
    diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to
        the constructor.
        """
        # onto attributes named `designation`, `name`, `diameter`,
        # and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by
        # `None`
        # and a missing diameter being represented by `float('nan')`.

        self.designation = str(info['pdes'])

        if 'name' in info and info['name'] != '':
            self.name = info['name']
        else:
            self.name = None

        if 'diameter' in info and info['diameter'] != '':
            self.diameter = float(info['diameter'])
        else:
            self.diameter = float('nan')

        if info['hazardous'] == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f'{self.designation} {self.name}'

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the
        # __repr__
        # method for examples of advanced string formatting.
        return f"Designation: {self.designation}, name: {self.name}, " \
               f"diameter: {self.diameter}, " \
               f"hazardous: {self.hazardous}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation."""
        return (
            f"NearEarthObject(designation={self.designation!r}, "
            f"name={self.name!r}, "
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close
    approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to
        the constructor.
        """
        # onto attributes named `_designation`, `time`, `distance`,
        # and `velocity`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = str(info['des'])
        self.time = cd_to_datetime(info['time'])
        self.distance = float(info['dist'])
        self.velocity = float(info['vrel'])

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def designation(self):
        """Return the approach's designation."""
        return self._designation

    @property
    def time_str(self):
        """Return a formatted representation of this approach's time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # build a formatted representation of the approach time.
        return datetime_to_str(self.time)

    def serialize(self):
        """Return a human-readable repr. of this approach and its NEO."""
        # assuming that hazardous == None means non-hazardous
        hazardous = False if not self.neo.hazardous \
            else True

        name = '' if not self.neo.name \
            else self.neo.name

        diameter = '' if not self.neo.diameter \
            else self.neo.diameter

        serial = {
            'datetime_utc': self.time,
            'distance_au': self.distance,
            'velocity_km_s': self.velocity,
            'designation': self._designation,
            'name': name,
            'diameter_km': diameter,
            'potentially_hazardous': hazardous

        }

        return serial

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the
        # __repr__
        # method for examples of advanced string formatting.
        return f'Designation: {self._designation}, time: {self.time}, ' \
               f'distance: {self.distance}, ' \
               f'velocity: {self.velocity}'

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation."""
        return (
            f"CloseApproach(time={self.time_str!r}, distance="
            f"{self.distance:.2f}, "
            f"velocity={self.velocity:.2f}, neo={self.neo!r})")
