---
title: Aveva.Pdms.Maths.Geometry Namespace
namespace: Aveva.Pdms.Maths.Geometry
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry Namespace

## Classes

| 类型 | 描述 |
|------|------|
| [D2Angle](Aveva.Pdms.Maths.Geometry.D2Angle.md) | Class definition for an angle An object of this class represents an angle. The angle can be specified either in radians or degrees, and it can be queried in either units (irrespective of the units that were used to specify it). The functions sin() cos() belonging to this class have the property that when the angle is close to some integer multiple of PI/2 radians (90 degrees), the result is EXACTLY 0.0 , 1.0 or -1.0 as appropriate. The tolerance used for the test can be specified, but otherwise defaults to 1.0e-6 radians. Some operators are also defined. |
| [D2Arc](Aveva.Pdms.Maths.Geometry.D2Arc.md) | A directed arc class An arc can run either anticlockwise or clockwise from the start to the end angle. The direction is defined by the user. Input angles will be normalized to lie between 0 and 2pi If start and end angles are EXACTLY EQUAL then the arc will be treated as a FULL CIRCLE. All Angles are measured anticlockwise from the x axis. |
| [D2Circle](Aveva.Pdms.Maths.Geometry.D2Circle.md) | A 2-D Circle N.B. all ANGLES measured ANTI-CLOCKWISE from X-AXIS |
| [D2DivideLine](Aveva.Pdms.Maths.Geometry.D2DivideLine.md) | A 2-D Line Class, With normal n and dist d, point x is: on the line if: n.x + d = 0 above the line if: n.x + d > 0 Alternative format is (a,b;c) - point (x,y) is above the line if: ax + by + c > 0 The normal (as stored internally) always has magnitude 1. |
| [D2FiniteLine](Aveva.Pdms.Maths.Geometry.D2FiniteLine.md) | Finite line |
| [D2IrregularCartesianGrid](Aveva.Pdms.Maths.Geometry.D2IrregularCartesianGrid.md) | Class definition of a an Irregular Cartesian Grid. The members of this class are: 1) a mthOrientedPlane representing the origin and orientation of the grid, 2) a validity flag, 3) an array containing the x spacings for the grid definition, and 4) an array containing the y spacings for the grid definition. The x and y spacings must be non-zero and positive for this type of grid to be valid. Empty vectors will result in an invalid grid. |
| [D2IrregularPolarGrid](Aveva.Pdms.Maths.Geometry.D2IrregularPolarGrid.md) | Class definition of a an Irregular Polar Grid. An invalid grid will occur if any radii value is negative. If either the angular or radial vectors are empty a valid grid is defined, however, if both the angular and radial vectors are empty an invalid grid is defined. |
| [D2Limits](Aveva.Pdms.Maths.Geometry.D2Limits.md) | 2-D Limits Box |
| [D2Line](Aveva.Pdms.Maths.Geometry.D2Line.md) | 2 D Line class |
| [D2Matrix](Aveva.Pdms.Maths.Geometry.D2Matrix.md) | 2x2 matrix This matrix class can represent a 2x2 matrix of douuble precision quantities. The elements are indexed from (zero,zero). |
| [D2Point](Aveva.Pdms.Maths.Geometry.D2Point.md) | D2Point - a 2-D point class |
| [D2PolyLine](Aveva.Pdms.Maths.Geometry.D2PolyLine.md) | 2-D polyline sequence of straight line segments connected end to end |
| [D2Profile](Aveva.Pdms.Maths.Geometry.D2Profile.md) | 2-D profile This class represents a sequence of spans connected end to end. Each span is either a finite straight line or a circular arc. The number of nodes for a profile is always one more than the number of spans. A closed profile is represented by having the last node equal to the first. The constructors (apart from the copy constructor) generate an 'open-ended' profile consisting of a single node and with no spans. (If the first node is not known when the constructor is invoked, it can be set later by calling setNode() .) The function addSpan() should be called succesively to extend an open-ended profile one span at a time. The function close() may be called to add the final span for what is to be a closed profile. |
| [D2RegularCartesianGrid](Aveva.Pdms.Maths.Geometry.D2RegularCartesianGrid.md) | Class definition of a Regular Cartesian Grid. The x and y spacings must be non-zero and positive for this type of grid to be valid. |
| [D2Span](Aveva.Pdms.Maths.Geometry.D2Span.md) | Span class - consists of a line or arc, and is used by D2Profile |
| [D2Transform](Aveva.Pdms.Maths.Geometry.D2Transform.md) | D2Transform - solid body transformations |
| [D2Vector](Aveva.Pdms.Maths.Geometry.D2Vector.md) | 2-D vector class |
| [D3Arc](Aveva.Pdms.Maths.Geometry.D3Arc.md) | A directed 3-D arc |
| [D3FiniteLine](Aveva.Pdms.Maths.Geometry.D3FiniteLine.md) | Finite line in 3D space |
| [D3Limits](Aveva.Pdms.Maths.Geometry.D3Limits.md) | 3-D limits This object can be in one of 2 states: - unset: origin at ( DBL_MAX, DBL_MAX, DBL_MAX) extent at (-DBL_MAX, -DBL_MAX, -DBL_MAX) - set: xMin <= xMax, yMin <= yMax, zMin <= zMax |
| [D3Line](Aveva.Pdms.Maths.Geometry.D3Line.md) | Finite, Semi-infinite or infinite line in 3D space |
| [D3Matrix](Aveva.Pdms.Maths.Geometry.D3Matrix.md) | 3x3 matrix This matrix class can represent a 3x3 matrix of double recision quantities. The elements are indexed from (zero,zero,zero). |
| [D3OrientedPlane](Aveva.Pdms.Maths.Geometry.D3OrientedPlane.md) | Class definition for an oriented plane This class is intended for use as a local coordinate system so that plane coordinate geometry can be performed. Conceptually it has a one-to-one correspondence with PDMS's orientated plane. Apart from its direct use for the 2-d geometry constructor, it is intended that arcs, planar curves and lines in 3-d are reduced to 2-d via mth2<obj>(const mth3<obj>, const D3OrientedPlane); To create the plane you need to supply an origin (D3Point) and two axes u,v - both D3Vector. The plane normal is then defined by u x v. This class always creates a plane with right-handed orthonormal axes. An internal flag is set if the data is invalid (e.g. the input vectors are null or colinear) and an attempt to use an invalid class will result in an assertion failure. Applications should use the 'inValid()' method to preemptively trap this condition. A cast to a D3Plane exists so that geometric operations on a D3Plane will also work on an D3OrientedPlane; you can also cast to a D3Transform. |
| [D3Plane](Aveva.Pdms.Maths.Geometry.D3Plane.md) | A 3-D Plane Class (with double values) With normal n and dist d, point x is: on the plane if: n.x + d = 0 above the plane if: n.x + d > 0 Alternative format is (a,b,c;d) - point (x,y,z) is above the plane if: ax + by + cz + d > 0 normal always has magnitude 1. |
| [D3Point](Aveva.Pdms.Maths.Geometry.D3Point.md) | 3D Point class |
| [D3Transform](Aveva.Pdms.Maths.Geometry.D3Transform.md) | D3Transform - solid body transformations |
| [D3Vector](Aveva.Pdms.Maths.Geometry.D3Vector.md) | 3D Vector class |

## Interfaces

| 类型 | 描述 |
|------|------|
| [D2PointFactory](Aveva.Pdms.Maths.Geometry.D2PointFactory.md) | D2PointFactory |

## Enumerations

| 类型 | 描述 |
|------|------|
| [D2Angle.angleUnits](Aveva.Pdms.Maths.Geometry.D2Angle.angleUnits.md) | enum to define units as radians or degrees |
| [D2Line.LTYPE](Aveva.Pdms.Maths.Geometry.D2Line.LTYPE.md) | four possible line types |
| [D3Line.LTYPE](Aveva.Pdms.Maths.Geometry.D3Line.LTYPE.md) | four possible line types |
